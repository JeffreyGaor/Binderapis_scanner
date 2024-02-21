import time
from utils.url_validator import is_valid_url
from utils.req_methods import req_methods

def check_api_4(endpoint, method='GET', token=None):
  vulnerabilities = []
  logs = []

  if not is_valid_url(endpoint):
    logs.append(f'Invalid URL: {endpoint}')
    return 'Invalid URL', logs

  num_requests = 10
  response_size_threshold = 1024 * 500
  response_time_threshold = 15.0

  total_response_time = 0
  total_response_size = 0

  for _ in range(num_requests):
    start_time = time.time()
    response = req_methods(endpoint, method, token)
    end_time = time.time()

    if response.status_code // 100 in {2, 4}:
      response_time = end_time - start_time
      total_response_time += response_time

      response_size = len(response.content)
      total_response_size += response_size

      logs.append(f"API 4: Request {_ + 1:>2}: Response time: {response_time:.4f} seconds, Response size: {response_size} bytes")

      if response_time > response_time_threshold:
        logs.append(f'API 4: Request {_ + 1:>2}: Unrestricted Resource Consumption Detected - Response time is too high!')

      if response_size > response_size_threshold:
        logs.append(f'API 4: Request {_ + 1:>2}: Unrestricted Resource Consumption Detected - Response size is too large!')

    else:
      logs.append(f"API 4: Error accessing API at {endpoint}. Status code: {response.status_code}")
      break

  avg_response_time = total_response_time / num_requests
  avg_response_size = total_response_size / num_requests

  logs.append(f"API 4: Average Response Time: {avg_response_time:.4f} seconds")
  logs.append(f"API 4: Average Response Size: {avg_response_size} bytes")

  if avg_response_time > response_time_threshold or avg_response_size > response_size_threshold:
    message = 'Overall Unrestricted Resource Consumption Detected'
    logs.append('API 4: ' + message)
    vulnerabilities.append(message)

  else:
    logs.append('API 4: Resource consumption is within acceptable limits.')

  for log in logs:
    print(log)
    time.sleep(0.5)

  return vulnerabilities
