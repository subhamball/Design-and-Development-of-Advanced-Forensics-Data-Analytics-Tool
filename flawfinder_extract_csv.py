import re
import csv

def extract_line_from_file(file_path, line_number):
    """
    Extracts a specific line from a file based on the given line number.
    """
    try:
        with open(file_path, 'r') as file:
            for current_line_number, line in enumerate(file, 1):
                if current_line_number == line_number:
                    return line.strip()  # Strip newlines or trailing spaces
    except FileNotFoundError:
        print(f"File not found: {file_path}")
    except Exception as e:
        print(f"An error occurred while reading {file_path}: {e}")
    return None

def process_input_file(input_file, output_file):
    """
    Process the specified input file to extract lines from mentioned files and line numbers,
    and writes the results to an output CSV file with indications of potential vulnerabilities.
    """
    # Updated regex to match files with extensions .c, .cpp, .h, and .nc
    line_regex = re.compile(r'^(.*\.(?:c|cpp|h|nc)):(\d+)$')

    try:
        with open(input_file, 'r') as file:
            with open(output_file, 'w', newline='') as outfile:
                writer = csv.writer(outfile)
                writer.writerow(["Code", "isMalicious"])  # Write headers

                for line in file:
                    match = line_regex.search(line)
                    if match:
                        file_path, line_number_str = match.groups()
                        line_number = int(line_number_str)
                        extracted_line = extract_line_from_file(file_path, line_number)
                        if extracted_line:
                            writer.writerow([extracted_line, "Vulnerable Code"])
                        else:
                            writer.writerow([f"Line {line_number} not found in file {file_path}", "Vulnerable Code"])
    except FileNotFoundError:
        print(f"Input file not found: {input_file}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Define paths for the input and output files
input_file_path = '/home/subham/output/flawfinder_output.txt'
output_file_path = '/home/subham/output/Vulnerable_code.csv'

# Process the input file and write the results to the output file
process_input_file(input_file_path, output_file_path)

