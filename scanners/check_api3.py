import json
from utils.url_validator import is_valid_url
from utils.req_methods import req_methods

#API3:2023 - Broken Object Property Level Authorization
def check_api_3(endpoint, method='GET', token=None):
  vulnerabilities = []
  if not is_valid_url(endpoint):
    print(f'Invalid URL: {endpoint}')
    return 'Invalid URL'
  
  malicious_payload  = {
    'item': 'this is a payload implant',
  }

  response = req_methods(endpoint, method, token)
  if response.status_code // 100 == 2:
    try:
      json_data = response.json()
      if isinstance(json_data, dict) and malicious_payload:
        json_data.update(malicious_payload)
      else:
        json_data = malicious_payload

    except json.JSONDecodeError:
      print('API 3: Error decoding JSON response.')
    modified_response = req_methods(endpoint, method, token, json_data)
    if modified_response.status_code // 100 == 2:
      message = 'Broken Object Property Level Authorization Detected'
      print('API 3: ' + message)
      vulnerabilities.append(message)
    else:
      print('API 3: Endpoint processed the modified payload, but did not detect the broken object property level')
  else:
    print(f"API 3: Error accessing API at {endpoint}. Status code: {response.status_code}")
    
  return vulnerabilities
