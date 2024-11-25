import os
from datetime import datetime

# Specify the directory path
directory = r"https://github.com/tiyegordon/LUIT-PYTH.git"

# Check if the directory exists
if not os.path.exists(directory):
    print(f"Directory does not exist: {directory}")
else:
    # Get a list of files in the specified directory
    file_list = []
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)  # Get the full path
        if os.path.isfile(file_path):  # Check if it's a file
            file_info = {
                "name": filename,
                "size": os.path.getsize(file_path),
                "creation_date": datetime.fromtimestamp(os.path.getctime(file_path)).strftime('%Y-%m-%d %H:%M:%S'),
            }
            file_list.append(file_info)

    # Check if files were found
    if file_list:
        print("Files found in the directory:")
        for file in file_list:
            print(file)
    else:
        print(f"No files found in the directory: {directory}")
