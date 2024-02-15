import json
import requests
from urllib.parse import urlparse

def is_valid_url(url):
  parsed_url = urlparse(url)
  return parsed_url.scheme in ['http', 'https'] and parsed_url.netloc != ''

def check_api1_broken_object_level_authorization(endpoint,  token=None):
  vulnerabilities = []
  headers = {'Authorization': f'Bearer {token}'} if token else {}
  if not is_valid_url(endpoint):
    print(f"Invalid URL: {endpoint}")
    return
  
  url = f"{endpoint}/1"
  response = requests.get(url, headers=headers)

  if response.status_code == 200:
    try:
      json_data = response.json()
    except json.JSONDecodeError:
      print('Error decoding JSON response.')

    if 'id' in json_data:
      print(json.dumps(json_data, indent=2))  
      print('Broken Object Leval Authorization Detected')

    else:
      malicious_payload  = {
        'id': 2,
      }

      modified_response = requests.post(endpoint, json=malicious_payload, headers=headers)
      if modified_response.status_code != 200:
        print(f"Unexpected status code: {modified_response.status_code}")

      else:
        modified_response_json = modified_response.json()
        if 'id' in modified_response_json:
          print(json.dumps(modified_response_json, indent=2))
          print('Unexpected Broken Object Level Authorization Detected')

      modified_response_invalid_json = requests.post(endpoint, data="invalid_json", headers=headers)
      if modified_response_invalid_json.status_code == 200:
        try:
          json_data_invalid = modified_response_invalid_json.json()
          print(json.dumps(json_data_invalid, indent=2))
          print('Unexpected Broken Object Level Authorization Detected - Invalid JSON')
        
        except json.JSONDecodeError:
          pass

  elif response.status_code == 401:
    return print('No Broken Object Leval Authorization Detected')
  
  else:
    print(f"Error accessing API at {endpoint}. Status code: {response.status_code}")
    return
