import re

def extract_unique_file_paths(input_file_path, output_file_path):
    unique_paths = set()
    file_path_regex = re.compile(r'^(.*):\d+$')  # Regex to extract file paths before the colon followed by line number

    with open(input_file_path, 'r') as file:
        for line in file:
            match = file_path_regex.match(line.strip())
            if match:
                file_path = match.group(1)
                unique_paths.add(file_path)

    with open(output_file_path, 'w') as outfile:
        for path in sorted(unique_paths):
            outfile.write(path + '\n')

# Define the paths for the input and output files
input_file_path = '/home/subham/MTP_script/flawfinder_hits.txt'
output_file_path = '/home/subham/MTP_script/flawfinder_not_hits.txt'

# Extract unique file paths and write them to the output file
extract_unique_file_paths(input_file_path, output_file_path)

