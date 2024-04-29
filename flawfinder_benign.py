import os
import csv

# Path to the text file that contains the vulnerable line information
input_txt_path = '/home/subham/MTP_script/flawfinder_no_hits.txt'

# Output CSV file path
output_csv_path = '/home/subham/MTP_script/benign_code_for_no_hits.csv'

# Dictionary to store file paths and their corresponding lines to exclude
exclude_lines = {}

# Read the input file and populate the exclude_lines dictionary
with open(input_txt_path, 'r') as file:
    for line in file:
        if ':' in line:
            file_path, line_number = line.strip().split(':')
            try:
                line_number = int(line_number)
                if file_path in exclude_lines:
                    exclude_lines[file_path].add(line_number)
                else:
                    exclude_lines[file_path] = set([line_number])
            except ValueError:
                print(f"Warning: Invalid line number found in input file: {line}")

# Prepare to write to the CSV file
with open(output_csv_path, 'w', newline='') as csvfile:
    fieldnames = ['Code', 'isMalicious']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

    # Process each file and extract non-vulnerable lines
    for file_path, lines_to_exclude in exclude_lines.items():
        if os.path.exists(file_path):
            with open(file_path, 'r') as code_file:
                for line_number, code_line in enumerate(code_file, 1):
                    if line_number not in lines_to_exclude:
                        writer.writerow({'Code': code_line.strip(), 'isMalicious': 'Benign code'})
        else:
            print(f"Warning: The file {file_path} does not exist.")

print("Processing complete. The non-vulnerable code lines have been written to the CSV file.")

