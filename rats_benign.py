'''
import os
import csv

def extract_code_from_file(filepath, excluded_lines):
    """Extracts lines of code from files excluding specified lines."""
    extracted_code = []
    with open(filepath, 'rb') as file:
        lines = file.readlines()
        for idx, line in enumerate(lines):
            try:
                decoded_line = line.decode('utf-8')
                if idx + 1 not in excluded_lines:
                    extracted_code.append(decoded_line.strip())
            except UnicodeDecodeError:
                pass
    return extracted_code

def main():
    input_file_path = "/home/subham/output/rats_analysis_output.txt"
    output_csv_path = "/home/subham/output/rats_benign_code.csv"

    excluded_lines = {}  # Dictionary to keep track of excluded lines per file type

    with open(input_file_path, 'r') as file:
        lines = file.readlines()
        for line in lines:
            for ext in ['.c', '.h', '.cpp', '.nc']:
                if ext + ":" in line:
                    line_number = int(line.split(ext + ":")[1].split(":")[0])
                    if ext not in excluded_lines:
                        excluded_lines[ext] = set()
                    excluded_lines[ext].add(line_number)

    extracted_code = []
    root_dir = "/home/subham/output/"
    for dirpath, _, filenames in os.walk(root_dir):
        for filename in filenames:
            ext = os.path.splitext(filename)[1]
            if ext in ['.c', '.h', '.cpp', '.nc']:
                file_path = os.path.join(dirpath, filename)
                if os.path.isfile(file_path):
                    lines_to_exclude = excluded_lines.get(ext, set())
                    extracted_code.extend(extract_code_from_file(file_path, lines_to_exclude))

    with open(output_csv_path, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['Code', 'isMalicious']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for code in extracted_code:
            writer.writerow({'Code': code, 'isMalicious': 'Benign code'})

if __name__ == "__main__":
    main()
    
'''

import os
import csv

def extract_code_from_file(filepath, excluded_lines):
    """Extracts lines of code from files excluding specified lines."""
    extracted_code = []
    with open(filepath, 'rb') as file:
        lines = file.readlines()
        for idx, line in enumerate(lines):
            try:
                decoded_line = line.decode('utf-8')
                if idx + 1 not in excluded_lines:
                    extracted_code.append(decoded_line.strip())
            except UnicodeDecodeError:
                pass
    return extracted_code

def main():
    input_file_path = "/home/subham/output/rats_analysis_output.txt"
    output_csv_path = "/home/subham/output/rats_benign_code.csv"

    excluded_lines = {}  # Dictionary to keep track of excluded lines per file type

    with open(input_file_path, 'r') as file:
        lines = file.readlines()
        for line in lines:
            try:
                for ext in ['.c', '.h', '.cpp', '.nc']:
                    if ext + ":" in line:
                        parts = line.split(ext + ":")
                        if len(parts) > 1 and parts[1].strip().isdigit():
                            line_number = int(parts[1].strip())
                            if ext not in excluded_lines:
                                excluded_lines[ext] = set()
                            excluded_lines[ext].add(line_number)
            except ValueError:
                print(f"Skipping malformed line: {line}")

    extracted_code = []
    root_dir = "/home/subham/all_os_code/"
    for dirpath, _, filenames in os.walk(root_dir):
        for filename in filenames:
            ext = os.path.splitext(filename)[1]
            if ext in ['.c', '.h', '.cpp', '.nc']:
                file_path = os.path.join(dirpath, filename)
                if os.path.isfile(file_path):
                    lines_to_exclude = excluded_lines.get(ext, set())
                    extracted_code.extend(extract_code_from_file(file_path, lines_to_exclude))

    with open(output_csv_path, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['Code', 'isMalicious']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for code in extracted_code:
            writer.writerow({'Code': code, 'isMalicious': 'Benign code'})

if __name__ == "__main__":
    main()


