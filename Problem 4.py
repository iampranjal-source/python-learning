import os

# Print the current working directory
print("Current Directory:", os.getcwd())

# Print all files and folders in the current directory
print("\nContents of the Directory:")
for item in os.listdir():
    print(item)


import os

# specify the directory you want to list 
directory_path = '/CHAPTER 1'

# list all files amd directories in the specific path
contents = os.listdir(directory_path)

# Print each file and directory name
for item in contents:
    print(item)

