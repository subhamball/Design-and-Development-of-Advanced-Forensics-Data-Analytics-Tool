'''
import os
import re

def remove_comments_from_file(file_path):
    """
    Remove C/C++ style comments from a file.

    :param file_path: Path to the file to process.
    """
    with open(file_path, 'r') as file:
        content = file.read()

    # Remove all multiline comments
    content = re.sub(r'/\*.*?\*/', '', content, flags=re.DOTALL)

    # Remove all single line comments
    content = re.sub(r'//.*', '', content)

    # Write the processed content back to the file
    with open(file_path, 'w') as file:
        file.write(content)

def remove_comments_from_directory(directory):
    """
    Remove comments from all files in a directory that end with .c, .cpp, .h, or .nc

    :param directory: Directory to process files in.
    """
    for filename in os.listdir(directory):
        if filename.endswith(('.c', '.cpp', '.h', '.nc')):
            file_path = os.path.join(directory, filename)
            print(f"Processing {file_path}...")
            remove_comments_from_file(file_path)
            print(f"Comments removed from {file_path}")

# Specify the directory containing the source files
source_dir = "/home/subham/all_os_code"

# Call the function to start processing files
remove_comments_from_directory(source_dir)
'''

import os
import re

def remove_comments_from_file(file_path):
    """
    Remove C/C++ style comments from a file and handle different encodings.

    :param file_path: Path to the file to process.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
    except UnicodeDecodeError:
        # Try reading with a different encoding if UTF-8 fails
        with open(file_path, 'r', encoding='iso-8859-1') as file:
            content = file.read()

    # Remove all multiline comments
    content = re.sub(r'/\*.*?\*/', '', content, flags=re.DOTALL)

    # Remove all single line comments
    content = re.sub(r'//.*', '', content)

    # Write the processed content back to the file
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(content)

def remove_comments_from_directory(directory):
    """
    Remove comments from all files in a directory that end with .c, .cpp, .h, or .nc

    :param directory: Directory to process files in.
    """
    for filename in os.listdir(directory):
        if filename.endswith(('.c', '.cpp', '.h', '.nc')):
            file_path = os.path.join(directory, filename)
            print(f"Processing {file_path}...")
            remove_comments_from_file(file_path)
            print(f"Comments removed from {file_path}")

# Specify the directory containing the source files
source_dir = "/home/subham/all_os_code"

# Call the function to start processing files
remove_comments_from_directory(source_dir)

