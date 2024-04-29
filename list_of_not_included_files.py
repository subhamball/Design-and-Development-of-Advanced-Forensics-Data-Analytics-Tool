import os

def read_unique_file_paths(file_path):
    with open(file_path, 'r') as file:
        return set(line.strip() for line in file)

def find_unlisted_files(directory, unique_paths, output_file_path):
    not_included_files = []
    # Tuple of the file extensions to look for
    extensions = ('.c', '.cpp', '.h', '.nc')

    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(extensions):
                full_path = os.path.join(root, file)
                if full_path not in unique_paths:
                    not_included_files.append(full_path)

    with open(output_file_path, 'w') as outfile:
        for path in sorted(not_included_files):
            outfile.write(path + '\n')

# Define the paths
input_unique_file_path = '/home/subham/MTP_script/flawfinder_unique_hits.txt'
directory_to_search = '/home/subham/all_os_code'
output_not_included_file_path = '/home/subham/MTP_script/flawfinder_no_hits.txt'

# Read the unique paths from the provided file
unique_paths = read_unique_file_paths(input_unique_file_path)

# Find and save the unlisted file paths
find_unlisted_files(directory_to_search, unique_paths, output_not_included_file_path)

