from utils.reader import load_sensitive_data
from utils.url_validator import is_valid_url
from utils.req_methods import req_methods

#API6:2023 - Unrestricted Access to Sensitive Business Flows
def check_api_6(endpoint, method='GET', token=None):
  vulnerabilities = []
  logs = []

  if not is_valid_url(endpoint):
    logs.append(f'Invalid URL: {endpoint}')
    return 'Invalid URL', logs
  
  sensitive_keywords = load_sensitive_data('files/sensitive_data.txt')
  response = req_methods(endpoint, method, token)
  if response.status_code // 100 in {2, 4}:
    for keyword in sensitive_keywords:
      if keyword in response.text:
        message = f'Potential Vulnerability Detected - Sensitive business flow "{keyword}" exposed without appropriate access restrictions.'
        logs.append('API 6: ' + message)
        vulnerabilities.append(message)
  else:
    logs.append(f'API 6: Error accessing API at {endpoint}. Status code: {response.status_code}')
    
  if len(vulnerabilities) == 0:
    logs.append('API 6: No Sensitive Data exposed.')

  for log in logs:
    print(log)

  return vulnerabilities
