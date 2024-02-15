import json
import requests
from urllib.parse import urlparse

def is_valid_url(url):
  parsed_url = urlparse(url)
  return parsed_url.scheme in ['http', 'https'] and parsed_url.netloc != ''

def check_api3_broken_object_property_level_authorization(endpoint, token=None):
  headers = {'Authorization': f'Bearer {token}'} if token else {}
  if not is_valid_url(endpoint):
    print(f"Invalid URL: {endpoint}")
    return
  
  malicious_payload  = {
    'item': 'this is a payload implant',
  }


  response = requests.get(endpoint, headers=headers)
  if response.status_code == 200:
    try:
      json_data = response.json()
      json_data.update(malicious_payload)
      
    except json.JSONDecodeError:
      print('Error decoding JSON response.')
    
    modified_response = requests.post(endpoint, json=json_data, headers=headers)
    if modified_response.status_code == 200:
      print('Broken Object Property Level Authorization Detected')
    else:
      print('Endpoint processed the modified payload, but did not detect the broken object property level')
  else:
    print(f"Error accessing API at {endpoint}. Status code: {response.status_code}")
    return


