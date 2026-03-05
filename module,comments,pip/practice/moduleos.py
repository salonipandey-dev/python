import os

# Specify the directory path
path = "/"

# Get list of files and directories
contents = os.listdir(path)

# Print each item
for item in contents:
    print(item)
