'''
import pandas as pd

def filter_code_snippets(file_path, output_path):
    # Load the CSV file
    data = pd.read_csv(file_path)

    # Filter rows where the 'Code' field starts with "#" and ends with ";"
    filtered_data = data[data['Code'].apply(lambda x: x.startswith('#') and x.endswith(';'))]

    # Save the filtered data to a new CSV file
    filtered_data.to_csv(output_path, index=False)

# Define file paths
input_file_path = '/home/subham/analysis_data/final_filterd_dataset_flawfinder.csv'
output_file_path = '/home/subham/analysis_data/filtered_top_2000.csv'

# Filter the code snippets
filter_code_snippets(input_file_path, output_file_path)

'''

import pandas as pd

def filter_code_snippets(file_path, output_path):
    # Load the CSV file
    data = pd.read_csv(file_path)

    # Ensure the 'Code' column is treated as a string and filter rows
    filtered_data = data[data['Code'].astype(str).apply(lambda x: x.strip().startswith('#') and x.strip().endswith(';'))]

    # Save the filtered data to a new CSV file
    filtered_data.to_csv(output_path, index=False)

# Define file paths
input_file_path = '/home/subham/analysis_data/final_filterd_dataset_flawfinder.csv'
output_file_path = '/home/subham/analysis_data/filtered.csv'

# Filter the code snippets
filter_code_snippets(input_file_path, output_file_path)

