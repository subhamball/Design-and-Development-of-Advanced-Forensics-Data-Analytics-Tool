import pandas as pd

def remove_duplicates(input_file, output_file):
    # Load the data from the input CSV file
    data = pd.read_csv(input_file)

    # Remove duplicate rows
    data_cleaned = data.drop_duplicates()

    # Save the cleaned data to the output CSV file
    data_cleaned.to_csv(output_file, index=False)

# Specify the input and output file paths
input_file_path = '/home/subham/MTP_script/flawfinder.csv'
output_file_path = '/home/subham/output/remove_fuplicates_flawfinder.csv'

# Call the function to remove duplicates
remove_duplicates(input_file_path, output_file_path)

