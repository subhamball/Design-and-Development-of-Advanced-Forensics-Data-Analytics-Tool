'''
import os
import subprocess

def run_rats_on_file(file_path, output_file):
    # Run rats tool on the file and append output to output_file
    with open(output_file, 'a') as output:
        output.write(f"========== Output for {file_path} ==========\n")
        try:
            result = subprocess.run(['rats', file_path], capture_output=True, text=True)
            output.write(result.stdout)
            output.write('\n')
        except Exception as e:
            output.write(f"Error processing {file_path}: {str(e)}\n")
            output.write('\n')

def run_rats_on_directory(directory, output_file):
    # Recursively search for *.c files and run rats tool on each of them
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.h'):
                file_path = os.path.join(root, file)
                run_rats_on_file(file_path, output_file)

def main():
    # Define the directory containing the source files
    source_directory = '/home/subham/mtp2/tinyos-main'
    # Define the output file
    output_file = '/home/subham/Documents/analysis_file/tinyos/rats/h_output.txt'

    # Clear previous content of output file
    with open(output_file, 'w') as f:
        pass

    # Run rats on all *.c files in the source directory
    run_rats_on_directory(source_directory, output_file)

if __name__ == "__main__":
    main()
    
'''

import os
import subprocess

def run_rats_on_file(file_path, output_file):
    # Run rats tool on the file and append output to output_file
    with open(output_file, 'a') as output:
        output.write(f"========== Output for {file_path} ==========\n")
        try:
            result = subprocess.run(['rats', file_path], capture_output=True, text=True)
            output.write(result.stdout)
            output.write('\n')
        except Exception as e:
            output.write(f"Error processing {file_path}: {str(e)}\n")
            output.write('\n')

def run_rats_on_directory(directory, output_file):
    # Recursively search for files with the specified extensions and run rats tool on each of them
    extensions = ('.c', '.cpp', '.h', '.nc')  # File extensions to include in the scan
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(extensions):
                file_path = os.path.join(root, file)
                run_rats_on_file(file_path, output_file)

def main():
    # Define the directory containing the source files
    source_directory = '/home/subham/output'
    # Define the output file
    output_file = '/home/subham/output/demo.txt'

    # Clear previous content of output file
    with open(output_file, 'w') as f:
        pass

    # Run rats on all files with specified extensions in the source directory
    run_rats_on_directory(source_directory, output_file)

if __name__ == "__main__":
    main()


