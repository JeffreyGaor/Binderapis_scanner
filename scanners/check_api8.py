import time
from utils.url_validator import is_valid_url
from utils.req_methods import req_methods

def get_api_config(endpoint, method, token):
  response = req_methods(endpoint, method, token)
  response.raise_for_status()
  api_config = response.headers
  logs = []

  if response.status_code // 100 == 5:
    logs.append(f"API Error accessing API at {endpoint}. Status code: {response.status_code}")

  return api_config, logs

#API8:2023 - Security Misconfiguration
def check_api_8(endpoint, method='GET', token=None):
  owasp = "Security Misconfiguration - "
  vulnerabilities = []
  logs = []

  if not is_valid_url(endpoint):
    logs.append(f'Invalid URL: {endpoint}')
    return 'Invalid URL', logs

  api_headers, api_logs = get_api_config(endpoint, method, token)
  logs.extend(api_logs)

  if 'Strict-Transport-Security' not in api_headers:
    vul_1 = 'Strict-Transport-Security header is missing. Consider adding it.'
    vulnerabilities.append(owasp + vul_1)
    logs.append('API 8: ' + vul_1)
    vul_2 = 'Transport Layer Security (TLS) is missing. Consider enabling it.'
    vulnerabilities.append(owasp + vul_2)
    logs.append('API 8: ' + vul_2)

  if 'Cache-Control' in api_headers and 'private' not in api_headers['Cache-Control']:
    vul_3 = 'Cache-Control header may expose sensitive information.'
    vulnerabilities.append(owasp + vul_3)
    vulnerabilities.append(vul_3)

  if 'Content-Type' in api_headers and api_headers['Content-Type'] != 'application/json':
    vul_4 = 'Unexpected Content-Type. Expected: application/json'
    logs.append('API 8: ' + vul_4)
    vulnerabilities.append(owasp + vul_4)
    if 'Content-Disposition' in api_headers:
      content_disposition = api_headers['Content-Disposition']
      if 'attachment' in content_disposition.lower():
        vul_5 = 'The response appears to be a file attachment. Validate file handling.'
        logs.append('API 8: ' + vul_5)
        vulnerabilities.append(owasp + vul_5)

  if 'X-Powered-By' in api_headers:
    vul_6 = 'X-Powered-By header is present, consider removing it.'
    logs.append('API 8: ' + vul_6)
    vulnerabilities.append(owasp + vul_6)

  if 'X-Content-Type-Options' not in api_headers:
    vul_7 = 'X-Content-Type-Options header is missing. Consider adding "nosniff".'
    logs.append('API 8: ' + vul_7)
    vulnerabilities.append(owasp + vul_7)

  if 'Access-Control-Allow-Origin' not in api_headers:
    vul_8 = 'Access-Control-Allow-Origin header is missing.'
    logs.append('API 8: ' + vul_8)
    vulnerabilities.append(owasp + vul_8)

  elif api_headers['Access-Control-Allow-Origin'] == '*':
    vul_9 = 'Access-Control-Allow-Origin header allows any origin.'
    logs.append('API 8: ' + vul_9)
    vulnerabilities.append(owasp + vul_9)

  if len(vulnerabilities) == 0:
    logs.append('API 9: Security is properly configured')

  for log in logs:
    print(log)
    time.sleep(0.5)
    
  return vulnerabilities
