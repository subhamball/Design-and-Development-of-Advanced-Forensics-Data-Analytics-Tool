def read_file_paths(file_path):
    """ Read file paths from a given file. """
    with open(file_path, 'r') as file:
        return {line.strip() for line in file if line.strip()}

def filter_unique_paths(source_paths_file, filtered_paths_file, output_file):
    """ Filter out paths that are not in the filtered paths file from the source paths file. """
    # Read paths from both files
    source_paths = read_file_paths(source_paths_file)
    filtered_paths = read_file_paths(filtered_paths_file)
    
    # Determine which paths are unique to the source file
    unique_paths = source_paths - filtered_paths

    # Write unique paths to the output file
    with open(output_file, 'w') as out:
        for path in unique_paths:
            out.write(path + '\n')

def main():
    # File containing all paths
    source_paths_file = '/home/subham/output/rats_analysis_output.txt'
    
    # File containing the paths to filter out
    filtered_paths_file = '/home/subham/output/output_hit_by_rat.txt'
    
    # Output file for unique paths
    output_file = '/home/subham/output/not_hit_paths.txt'

    # Filter and save unique paths
    filter_unique_paths(source_paths_file, filtered_paths_file, output_file)

if __name__ == "__main__":
    main()

