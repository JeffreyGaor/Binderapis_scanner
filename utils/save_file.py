import os

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