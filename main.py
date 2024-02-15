from utils.save_file import save_apis
from utils.load_file import load_apis
import shlex
import json

def scan_endpoints():
  filename = "files/api.txt"
  configurations = load_apis(filename)
  config_list = []
  if configurations:
    for config in configurations:
      config_str = str(config).replace("'", "\"").replace("\\", "")
      config_dict = eval(config_str)
      config_list.append(config_dict)
      print(config_list)
  
  else:
    print("No existing endpoints found.")

def main():
  configurations = []
  while True:
    print("\nOptions:")
    print("1. Scan existing endpoints")
    print("2. Add new endpoint")
    print("3. Quit")
    choice = input("Enter your choice: ")

    if choice == '1':
       scan_endpoints()

    elif choice == '2':
      while True:
        endpoint = input("Enter API endpoint (or type 'quit' to exit) [sample: http://example.com/api --method GET --token myapitoken]: ")
        if endpoint.lower() == 'quit':
          break

        parts = shlex.split(endpoint)
        if len(parts) < 2:
            print("Invalid input. Please provide endpoint and method.")
            continue
        
        endpoint = parts[0]
        method = None
        token = None

        for i in range(1, len(parts) - 1, 2):
          if parts[i] == "--method":
            method = parts[i + 1]
          elif parts[i] == "--token":
            token = parts[i + 1]

        if method is None:
          print("Invalid input. Please provide endpoint and method.")
          continue
        
        config = {
          "endpoint": endpoint,
          "method": method,
          "token": token
        }
        configurations.append(config)
        save_apis(configurations)

    elif choice == '3':
      print("Exiting...")
      break

    else:
      print("Invalid choice. Please choose a valid option.")

if __name__ == "__main__":
  main()