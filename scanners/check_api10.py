import time
from utils.url_validator import is_valid_url
from utils.req_methods import req_methods

#API10:2023 - Unsafe Consumption of APIs
def check_api_10(endpoint, method='GET', token=None):
  vulnerabilities = []
  logs = []
  headers = {'Authorization': f'Bearer {token}'} if token else {}
  
  if not is_valid_url(endpoint):
    logs.append(f'Invalid URL: {endpoint}')
    return 'Invalid URL'

  if not endpoint.startswith('https://'):
    message = 'Unsafe Consumption of APIs - API interacts over an unencrypted channel.'
    logs.append('API 10: Warning ' + message)
    vulnerabilities.append(message)

  response = req_methods(endpoint, method, token)

  if response.status_code // 100 == 2:   
    response = req_methods(endpoint, method, token)
    if response.history:
      message = 'Unsafe Consumption of APIs - API blindly follows redirections.'
      logs.append('API 10: Warning ' + message)
      vulnerabilities.append(message)

    response = req_methods(endpoint, method, token)
    if len(response.content) > 200:
      message = 'API does not limit the number of resources available.'
      logs.append('API 10: Warning ' + message)
      vulnerabilities.append(message)

    response = req_methods(endpoint, method, token)
    if response.status_code == 408: 
      message = 'API does not implement timeouts for interactions with third-party services.'
      logs.append('API 10: Warning ' + message)
      vulnerabilities.append(message)

  else:
    logs.append(f'API 10: Error accessing API at {endpoint}. Status code: {response.status_code}')

  for log in logs:
    print(log)
    time.sleep(0.5)

  return vulnerabilities
