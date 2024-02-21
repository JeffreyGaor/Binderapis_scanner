import json
from utils.url_validator import is_valid_url
from utils.req_methods import req_methods

#API5:2023 - Broken Function Level Authorization
def check_api_5(endpoint, method='GET', token=None):
  vulnerabilities = []
  if not is_valid_url(endpoint):
    print(f'Invalid URL: {endpoint}')
    return 'Invalid URL'
  
  response = req_methods(endpoint, method, token)
    
  return vulnerabilities
