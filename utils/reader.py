def load_apis(filename):
  try:
    with open(filename, 'r') as file:
      configurations = []
      for line in file:
        config_dict = eval(line.strip())
        configurations.append(config_dict)
      return configurations
  except Exception as e:
    print(f"An error occurred while reading the file: {e}")
    return None
  
def load_sensitive_data(filename):
  sensitive_data = []
  with open(filename, 'r') as file:
    for line in file:
      sensitive_data.append(line.strip())
  return sensitive_data

def list_sensitive_data(filename):
    print("Available sensitive data:")
    sensitive_data = load_sensitive_data(filename)
    print(sensitive_data)