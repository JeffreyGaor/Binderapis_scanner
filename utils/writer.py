import os
from utils.reader import load_sensitive_data

def save_apis(api):
  try:
    folder_path = "files"
    if not os.path.exists(folder_path):
      os.makedirs(folder_path)

    filename = os.path.join(folder_path, "api.txt")
    with open(filename, 'a') as file:
      for item in api:
        file.write(str(item) + '\n')
    print("API configurations have been saved to the file.")

  except Exception as e:
    print(f"An error occurred: {e}")

def save_sensitive_data(filename, sensitive_data):
  with open(filename, 'w') as file:
      for data in sensitive_data:
          file.write(data + '\n')

def add_sensitive_data(filename, new_data):
  sensitive_data = load_sensitive_data(filename)
  sensitive_data.append(new_data)
  save_sensitive_data(filename, sensitive_data)
  print(f"Added '{new_data}' to sensitive data list.")