import json
from utils.url_validator import is_valid_url
from utils.req_methods import req_methods

#API1:2023 - Broken Object Level Authorization
def check_api_1(endpoint, method='GET', token=None):
  vulnerabilities = []
  logs = []

  if not is_valid_url(endpoint):
    logs.append(f'Invalid URL: {endpoint}')
    return 'Invalid URL'
  
  if method in ['POST', 'PUT', 'PATCH', 'DELETE']:
    payload = {
      'user': 1,
      'user_id': 1,
      'id': 1,
      'reference': 'Attacker updated the user with ID 23 contact details'
    }
    response = req_methods(endpoint, method, token, payload)
    
    if response.status_code // 100 == 2:
      message = f'Broken Object Level Authorization on {method}'
      logs.append(f'API 1: {message}')
      vulnerabilities.append(message)

    elif response.status_code // 100 == 4:
      logs.append(f'API 1: {endpoint} is cleared for OWASP 1')

    else:
      logs.append(f'API 1: Error accessing API at {endpoint} Status code: {response.status_code}')

  else:
    endpoint = endpoint + '/1'
    response = req_methods(endpoint, method, token)

    if response.status_code // 100 == 2:
      message = 'Broken Object Level Authorization on GET'
      logs.append('AP1 1: ' + message)
      vulnerabilities.append(message)

    elif response.status_code // 100 == 4:
      logs.append(f"API 1: {endpoint} is cleared for OWASP 1")
      
    else:
      logs.append(f'API 1: Error accessing API at {endpoint} Status code: {response.status_code}')

  for log in logs:
    print(log)
  
  return vulnerabilities
