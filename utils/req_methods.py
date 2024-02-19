import requests

def req_methods(endpoint, method='GET', token=None, payload=None):
  headers = {'Authorization': f'Bearer {token}'} if token else {}
  response = requests.request(method, endpoint, headers=headers, data=payload)
  return response