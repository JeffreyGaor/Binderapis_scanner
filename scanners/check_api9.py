import time
from utils.url_validator import is_valid_url
from utils.req_methods import req_methods

#API9:2023 - Improper Inventory Management
def check_api_9(endpoint, method='GET', token=None):
  vulnerabilities = []
  logs = []

  if not is_valid_url(endpoint):
    logs.append(f'Invalid URL: {endpoint}')
    return 'Invalid URL', logs

  parts = endpoint.split('/')

  if 'api' not in parts:
    message = 'Improper Inventory Management - Missing API indicator.'
    logs.append('API 9: Warning ' + message)
    vulnerabilities.append(message)

  if not any(part.startswith('v') for part in parts):
    message = 'Improper Inventory Management - No proper Version identifier.'
    logs.append('API 9: Warning ' + message)
    vulnerabilities.append(message)

  if len(parts) < 6:
    message = 'Improper Inventory Management - Missing Dependency names.'
    logs.append('API 9: Warning ' + message)
    vulnerabilities.append(message)

  if len(vulnerabilities) == 0:
    logs.append('API 9: API Inventory is properly managed.')

  for log in logs:
    print(log)
    time.sleep(0.5)

  return vulnerabilities
