import os
import re

def process_file(file_path):
    """
    Removes all newlines, blank spaces, white spaces, and tabs between commas in the file.

    :param file_path: Path to the file to process.
    """
    # Read the file content
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()

        # Remove newlines, spaces, and tabs between commas
        processed_content = re.sub(r',\s+', ',', content)

        # Write the processed content back to the file
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(processed_content)

        print(f"File processed: {file_path}")
    except UnicodeDecodeError:
        print(f"Encoding issue with file: {file_path}")
    except Exception as e:
        print(f"Error processing file {file_path}: {e}")

def process_directory(directory):
    """
    Process all .c, .cpp, .h, and .nc files in the specified directory.

    :param directory: Directory to process files in.
    """
    # Iterate over all files in the directory
    for filename in os.listdir(directory):
        if filename.endswith(('.c', '.cpp', '.h', '.nc')):
            file_path = os.path.join(directory, filename)
            process_file(file_path)

# Directory containing the source files
source_dir = "/home/subham/all_os_code"

# Call the function to start processing files
process_directory(source_dir)


