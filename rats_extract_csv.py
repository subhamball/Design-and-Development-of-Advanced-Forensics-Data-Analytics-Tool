import csv
import re

# Define the path to the text file containing the paths and line numbers
input_file_path = '/home/subham/output/demo.txt'

# Define the path for the output CSV file
output_csv_path = '/home/subham/output/demo.csv'

# Regex to match lines with file paths and line numbers for .c, .h, .cpp, .nc files
path_regex = re.compile(r'(/home/subham/output/.+\.(c|cpp|h|nc)):(\d+)')

# Function to extract the line of code from a given file at a specific line number
def get_line_of_code(file_path, line_number):
    try:
        with open(file_path, 'r') as file:
            for current_line_number, line in enumerate(file, 1):
                if current_line_number == line_number:
                    return line.strip()
    except Exception as e:
        print(f"Error reading file {file_path} at line {line_number}: {e}")
        return None

# Open the CSV file for writing
with open(output_csv_path, mode='w', newline='') as file:
    writer = csv.writer(file)
    # Write the header
    writer.writerow(["Code", "isMalicious"])

    # Read the input file to find paths and line numbers
    with open(input_file_path, 'r') as file:
        for line in file:
            match = path_regex.search(line)
            if match:
                file_path = match.group(1)
                line_number = int(match.group(3))
                code_line = get_line_of_code(file_path, line_number)
                if code_line:
                    # Write to CSV: the line of code and label it as 'Vulnerable Code'
                    writer.writerow([code_line, 'Vulnerable Code'])

print("CSV file has been created successfully.")

