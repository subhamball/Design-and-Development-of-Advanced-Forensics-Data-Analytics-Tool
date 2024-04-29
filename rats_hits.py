def extract_relevant_lines(source_file, output_file):
    # Keywords to search for in each line
    keywords = ('.cpp:', '.c:', '.h:', '.nc:')
    
    # Open the source file and output file
    with open(source_file, 'r') as src, open(output_file, 'w') as out:
        # Read through each line in the source file
        for line in src:
            # Check if the line contains any of the keywords
            if any(keyword in line for keyword in keywords):
                # Write the line to the output file
                out.write(line)

def main():
    # Path to the source file containing the analysis results
    source_file = '/home/subham/output/rats_analysis_output.txt'
    
    # Path to the output file where filtered results will be saved
    output_file = '/home/subham/output/output_hit_by_rat.txt'
    
    # Extract relevant lines and save to the output file
    extract_relevant_lines(source_file, output_file)

if __name__ == "__main__":
    main()

