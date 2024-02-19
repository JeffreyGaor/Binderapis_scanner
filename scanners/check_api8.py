import json
from utils.url_validator import is_valid_url
from utils.req_methods import req_methods

#API8:2023 - Security Misconfiguration
def check_api_8(endpoint, method='GET', token=None):
  vulnerabilities = []
  if not is_valid_url(endpoint):
    print(f'Invalid URL: {endpoint}')
    return 'Invalid URL'
  
  response = req_methods(endpoint, method, token)
  if response.status_code == 500:
    print(f"Error accessing API at {endpoint}. Status code: {response.status_code}")
    
  vulnerabilities.append('this is a test')
  return vulnerabilities
