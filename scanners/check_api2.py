import json
from utils.url_validator import is_valid_url
from utils.req_methods import req_methods

def check_invalid_url(endpoint, logs):
  if not is_valid_url(endpoint):
    logs.append(f'Invalid URL: {endpoint}')
    return ['Invalid URL']
  return []

def check_token_issues(response, logs):
  vulnerabilities = []
  try:
    json_data = response.json()
    if 'error' in json_data:
      if json_data['error'] == 'Invalid Token':
        message = 'Broken Authentication Detected - Invalid Token'
        logs.append('API 2: ' + message)
        vulnerabilities.append(message)
    elif 'expiration' not in json_data:
      message = 'Broken Authentication Detected - Token Expiration Missing'
      logs.append('API 2: ' + message)
      vulnerabilities.append(message)
  except json.JSONDecodeError:
    logs.append('API 2: Error decoding JSON response.')
  return vulnerabilities

def perform_sql_injection(endpoint, method, token, logs):
  vulnerabilities = []
  max_attempts = 10
  payload = {
      'email': "' OR 1=1;",
      'username': "' OR 1=1;",
      'password': 'password'
  }

  for attempt in range(1, max_attempts + 1):
    response = req_methods(endpoint, method, token, payload)
    if response.status_code // 100 == 2:
      try:
          json_data = response.json()
          logs.append(json.dumps(json_data, indent=2))  
          message = 'Broken Authentication Detected - SQL Injectable'
          logs.append('API 2: ' + message)
          vulnerabilities.append(message)
          break
      except json.JSONDecodeError:
          logs.append('Error decoding JSON response.')
    elif response.status_code == 401:
      logs.append(f'Unauthorized Access - Attempt {attempt} of {max_attempts}')
      if attempt == max_attempts:
        message = 'Broken Authentication Detected - Lockdown Missing'
        logs.append('API 2: ' + message)
        vulnerabilities.append(message)
        break
    elif response.status_code == 403:
      try:
        json_data = response.json()
        if json_data.get('status') in ['locked', 'blocked']:
            logs.append("API 2: Authentication is locked or blocked. Exiting.")
            break
      except json.JSONDecodeError:
        logs.append('API 2: Error decoding JSON response.')
    else:
      logs.append(f'API 2: Error accessing API at {endpoint} Status code: {response.status_code}')
  
  return vulnerabilities

def check_api_2(endpoint, method='GET', token=None):
  vulnerabilities = []
  logs = []
  vulnerabilities.extend(check_invalid_url(endpoint, logs))

  if token:
    response = req_methods(endpoint, method, token)
    if response.status_code // 100 == 2:
      vulnerabilities.extend(check_token_issues(response, logs))
    if response.status_code // 100 == 4:
      if 'auth' in endpoint or 'login' in endpoint:
        vulnerabilities.extend(perform_sql_injection(endpoint, method, token, logs))
      else:
        logs.append(f'API 2: Not a Login/Auth Endpoint, Status code: {response.status_code}')
    else:
      logs.append(f'API 2: Error accessing API at {endpoint} Status code: {response.status_code}')
  else:
    vulnerabilities.extend(perform_sql_injection(endpoint, method, token, logs))

  for log in logs:
    print(log)

  return vulnerabilities
