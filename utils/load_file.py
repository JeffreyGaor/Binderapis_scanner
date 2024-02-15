def load_apis(filename):
  try:
    with open(filename, 'r') as file:
      configurations = []
      for line in file:
        # Convert each line into a dictionary
        config_dict = eval(line.strip())
        configurations.append(config_dict)
      return configurations
  except Exception as e:
    print(f"An error occurred while reading the file: {e}")
    return None