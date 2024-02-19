import json
from utils.url_validator import is_valid_url
from utils.req_methods import req_methods

#API9:2023 - Improper Inventory Management
def check_api_9(endpoint, method='GET', token=None):
  vulnerabilities = []
  if not is_valid_url(endpoint):
    print(f'Invalid URL: {endpoint}')
    return 'Invalid URL'
  
  parts = endpoint.split('/')

  if 'api' not in parts:
    message = 'Improper Inventory Management - Missing API Indicator.'
    print('API 9: Warning ' + message)
    vulnerabilities.append(message)

  if not any(part.startswith('v') for part in parts):
    message = 'Improper Inventory Management - Missing Version.'
    print('API 9: Warning ' + message)
    vulnerabilities.append(message)

  if len(parts) < 6:
    message = 'Improper Inventory Management - Missing Dependencies.'
    print('API 9: Warning ' + message)
    vulnerabilities.append(message)

  if len(vulnerabilities) == 0:
    print('API 9: API Inventory is properly managed.')

  return vulnerabilities
