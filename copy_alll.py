import os
import shutil

def copy_files(src_directory, dst_directory, extensions):
    """
    Copies files from src_directory to dst_directory based on the given extensions.

    :param src_directory: Source directory to search files in.
    :param dst_directory: Destination directory to copy files to.
    :param extensions: Tuple of file extensions to include.
    """
    # Ensure the destination directory exists
    if not os.path.exists(dst_directory):
        os.makedirs(dst_directory)

    # Walk through the source directory
    for root, dirs, files in os.walk(src_directory):
        for file in files:
            # Check if the file ends with a valid extension
            if file.endswith(extensions):
                # Construct full file path
                src_file_path = os.path.join(root, file)
                dst_file_path = os.path.join(dst_directory, file)
                # Copy file
                shutil.copy2(src_file_path, dst_file_path)
                print(f"Copied: {src_file_path} to {dst_file_path}")

# Specify source and destination directories
source_dir = "/home/subham/mtp2"
destination_dir = "/home/subham/all_os_code"

# Define file extensions to copy
file_extensions = ('.c', '.cpp', '.h', '.nc')

# Call the function to start copying files
copy_files(source_dir, destination_dir, file_extensions)

