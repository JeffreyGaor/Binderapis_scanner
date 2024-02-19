import json
from utils.url_validator import is_valid_url
from utils.req_methods import req_methods

#API10:2023 - Unsafe Consumption of APIs
def check_api_10(endpoint, method='GET', token=None):
  vulnerabilities = []
  headers = {'Authorization': f'Bearer {token}'} if token else {}
  if not is_valid_url(endpoint):
    print(f'Invalid URL: {endpoint}')
    return 'Invalid URL'
  
  if not endpoint.startswith('https://'):
    message = 'Unsafe Consumption of APIs - API interacts over an unencrypted channel.'
    print('API 10: Warning ' + message)
    vulnerabilities.append(message)

  response = req_methods(endpoint, method, token)

  if response.status_code // 100 == 2:   
    response = req_methods(endpoint, method, token)
    if response.history:
      message = 'Unsafe Consumption of APIs - API blindly follows redirections.'
      print('API 10: Warning ' + message)
      vulnerabilities.append(message)

    response = req_methods(endpoint, method, token)
    if len(response.content) > 200:
      message = 'API does not limit the number of resources available.'
      print('API 10: Warning ' + message)
      vulnerabilities.append(message)

    response = req_methods(endpoint, method, token)
    if response.status_code == 408: 
      message = 'API does not implement timeouts for interactions with third-party services.'
      print('API 10: Warning ' + message)
      vulnerabilities.append(message)

  else:
    print(f'API 10: Error accessing API at {endpoint}. Status code: {response.status_code}')

  return vulnerabilities
