from utils.writer import save_apis
from utils.writer import add_sensitive_data
from utils.reader import load_apis
from utils.reader import list_sensitive_data
from utils.url_validator import is_valid_url
from scanners.check_api1 import check_api_1
from scanners.check_api2 import check_api_2
from scanners.check_api3 import check_api_3
from scanners.check_api4 import check_api_4
from scanners.check_api5 import check_api_5
from scanners.check_api6 import check_api_6
from scanners.check_api7 import check_api_7
from scanners.check_api8 import check_api_8
from scanners.check_api9 import check_api_9
from scanners.check_api10 import check_api_10
import shlex

def scan_endpoints():
  filename = "files/api.txt"
  configurations = load_apis(filename)
  config_list = []
  if configurations:
    for config in configurations:
      config_str = str(config).replace("'", "\"").replace("\\", "")
      config_dict = eval(config_str)
      config_list.append(config_dict)
    return config_list

  else:
    print("No existing endpoints found.")

def validate_endpoint(endpoint_input):
  endpoint = method = token = None
  parts = shlex.split(endpoint_input)

  if len(parts) < 2:
    print("Invalid input. Please provide endpoint and method.")
    return None, None, None
  
  endpoint = parts[0]

  for i in range(1, len(parts) - 1, 2):
    if parts[i] == "--method":
      method = parts[i + 1]
    elif parts[i] == "--token":
      token = parts[i + 1]

  if method is None:
    print("Invalid input. Please provide endpoint and method.")
  
  return endpoint, method, token

def process_endpoint(endpoint_details):
  endpoint = endpoint_details['endpoint']
  method = endpoint_details['method']
  token = endpoint_details['token']

  if not is_valid_url(endpoint):
    print(f"Invalid URL: {endpoint}")
    return []

  vulnerabilities = []
  for check_func in [check_api_1, check_api_2, check_api_3, check_api_4, check_api_5, check_api_6, check_api_7, check_api_8, check_api_9, check_api_10]:
    vulnerabilities.extend(check_func(endpoint, method, token))
  return vulnerabilities

def main():
  while True:
    print("\nOptions:")
    print("1. Scan existing endpoints")
    print("2. Add new endpoint")
    print("3. Change list of sensitve data")
    print("4. Quit")
    choice = input("Enter your choice: ")

    if choice == '1':
      vulnerabilities = []
      endpoints = scan_endpoints()
      for endpoint_details in endpoints:
        print('\n')
        vulnerabilities.extend(process_endpoint(endpoint_details))
        print(vulnerabilities)
        vulnerabilities = []

    elif choice == '2':
      configurations = []
      while True:
        endpoint_input = input("Enter API endpoint (or type 'quit' to exit) [sample: http://example.com/api --method GET --token myapitoken]: ")
        if endpoint_input.lower() == 'quit':
            break

        endpoint, method, token = validate_endpoint(endpoint_input)
        if not endpoint or not method:
            continue
        
        config = {"endpoint": endpoint, "method": method, "token": token}
        configurations.append(config)

      save_apis(configurations)

    elif choice == '3':
      list_sensitive_data("files/sensitive_data.txt")
      new_data = input("Enter new sensitive data to add: ")
      add_sensitive_data("files/sensitive_data.txt", new_data)

    elif choice == '4':
      print("Exiting...")
      break

    else:
      print("Invalid choice. Please choose a valid option.")

if __name__ == "__main__":
  main()