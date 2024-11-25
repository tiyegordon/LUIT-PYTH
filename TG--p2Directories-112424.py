import os
from datetime import datetime
from typing import List, Dict

# Specify the directory path
directory: str = r"C:\Users\tiyea\documents\LUIT-PYTH"

def get_file_info(directory: str) -> List[Dict[str, str]]:
    """
    This function checks if a specified directory exists, and if it does,
    it retrieves information about the files in that directory (name, size, and creation date).
    
       
    Returns:
        List[Dict[str, str]]: A list of dictionaries where each dictionary contains 
                               information about a file in the directory, including:
                               - "name": the filename
                               - "size": the size of the file in bytes
                               - "creation_date": the creation date of the file in 'YYYY-MM-DD HH:MM:SS' format.
    """
    # List to store information about files
    file_list: List[Dict[str, str]] = []

    # Check if the directory exists
    if not os.path.exists(directory):
        print(f"Directory does not exist: {directory}")
        return file_list

    # Loop through each file in the directory
    for filename in os.listdir(directory):
        # Get the full path of the file
        file_path: str = os.path.join(directory, filename)

        # Check if the current path is a file (not a directory)
        if os.path.isfile(file_path):
            # Collect file information
            file_info: Dict[str, str] = {
                "name": filename,
                "size": str(os.path.getsize(file_path)),  # Convert size to string for consistent format
                "creation_date": datetime.fromtimestamp(os.path.getctime(file_path)).strftime('%Y-%m-%d %H:%M:%S'),
            }
            # Add the file information to the list
            file_list.append(file_info)

    # Return the list of file information
    return file_list

# Call the function and get file information
file_list = get_file_info(directory)

# Check if files were found
if file_list:
    print("Files found in the directory:")
    for file in file_list:
        print(file)
else:
    print(f"No files found in the directory: {directory}")
