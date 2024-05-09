import pandas as pd

# Load the data
df = pd.read_csv('/home/subham/analysis_data/final_dataset/rats_final_dataset.csv')

# List of keywords to filter out
keywords = ['char', 'unsigned char', 'short', 'unsigned short', 'int', 'unsigned int', 'long', 'unsigned long', 'float', 'double']

# Ensure that the 'Code' column is a string and replace NaN with an empty string
df['Code'] = df['Code'].fillna('').astype(str)

# Filter out the rows where 'Code' starts with any of the keywords
df_filtered = df[~df['Code'].str.strip().str.startswith(tuple(keywords))]

# Save the filtered DataFrame to a new CSV file
df_filtered.to_csv('/home/subham/analysis_data/final_dataset/final_filterd_dataset_rats.csv', index=False)

