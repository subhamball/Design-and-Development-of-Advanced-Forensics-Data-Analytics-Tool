import csv

def process_files_to_csv(input_file_list, output_csv_path):
    with open(input_file_list, 'r') as file_paths:
        with open(output_csv_path, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['Code', 'isMalicious'])  # Writing the header of CSV file

            for file_path in file_paths:
                file_path = file_path.strip()  # Remove any surrounding whitespace or newlines
                try:
                    with open(file_path, 'r') as file:
                        for line in file:
                            writer.writerow([line.strip(), 'Benign Code'])  # Write each line of code with the label
                except Exception as e:
                    print(f"An error occurred while processing {file_path}: {e}")

# Define the paths
input_file_list_path = '/home/subham/MTP_script/flawfinder_no_hits.txt'
output_csv_path = '/home/subham/MTP_script/benign_code_for_no_hits_detect_by_flawfinder.csv'

# Process the files and write to CSV
process_files_to_csv(input_file_list_path, output_csv_path)

