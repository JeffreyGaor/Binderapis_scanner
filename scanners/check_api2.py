import json
import requests
from urllib.parse import urlparse

def is_valid_url(url):
  parsed_url = urlparse(url)
  return parsed_url.scheme in ['http', 'https'] and parsed_url.netloc != ''

def check_api2_broken_authentication(endpoint, token=None):
  if not is_valid_url(endpoint):
    print(f"Invalid URL: {endpoint}")
    return
  
  if token:
    return check_api2_with_token(endpoint, token)
  else:
    return check_api2_without_token(endpoint)

def check_api2_with_token(endpoint, token):
  headers = {'Authorization': f'Bearer {token}'}
  response = requests.get(endpoint, headers=headers)

  if response.status_code == 200:
    try:
      json_data = response.json()
      if 'error' in json_data and json_data['error'] == 'InvalidToken':
        print('Broken Authentication Detected - Invalid Token')
      
      elif 'expiration' not in json_data:
        print('Broken Authentication Detected - Token Expiration Missing')

    except json.JSONDecodeError:
      print('Error decoding JSON response.')

  else:
    print(f"Error accessing API at {endpoint}. Status code: {response.status_code}")

def check_api2_without_token(endpoint, max_attempts = 10):
  payload = {
    'email': f"' OR 1=1;",
    'username': f"' OR 1=1;",
    'password': 'password'
  }
  for attempt in range(1, max_attempts + 1):
    response = requests.post(endpoint, json=payload)
    if response.status_code == 200:
      try:
        json_data = response.json()
        print(json.dumps(json_data, indent=2))  
        print('Broken Authentication Detected - SQL Injectable')
      except json.JSONDecodeError:
         print('Error decoding JSON response.')

    elif response.status_code == 401 or response.status_code == 500:
      print(f'Unauthorized Access - Attempt {attempt} of {max_attempts}')
      if attempt == max_attempts:
          print(f'Authentication Broken After {max_attempts} Attempts')
          print('Broken Authentication Detected - Lockdown Missing')
    else:
      print(f"Error accessing API at {endpoint}. Status code: {response.status_code}")
      return