import pandas as pd

def combine_csv_files(file1, file2, file3, output_file):
    # Read the CSV files
    df1 = pd.read_csv(file1)
    df2 = pd.read_csv(file2)
    df3 = pd.read_csv(file3)

    # Combine all three DataFrames into one
    combined_df = pd.concat([df1, df2, df3], ignore_index=True)

    # Write the combined DataFrame to a new CSV file
    combined_df.to_csv(output_file, index=False)

# Define the file paths
file1 = '/home/subham/MTP_script/Vulnerable_code_detect_by_flawfinder.csv'
file2 = '/home/subham/MTP_script/benign_code_for_hits_detect_by_flawfinder.csv'
file3 = '/home/subham/MTP_script/benign_code_for_no_hits_detect_by_flawfinder.csv'
output_file = '/home/subham/analysis_data/flawfinder.csv'

# Combine the files
combine_csv_files(file1, file2, file3, output_file)

