import os

def combine_files(directory, output_file):
    """Combine text from files with specific extensions into a single output file."""
    extensions = ('.c', '.h', '.cpp', '.nc')  # Extensions to look for
    with open(output_file, 'w', encoding='utf-8') as outfile:
        for root, _, files in os.walk(directory):
            for file in files:
                if file.endswith(extensions):
                    file_path = os.path.join(root, file)
                    try:
                        with open(file_path, 'r', encoding='utf-8') as infile:
                            contents = infile.read()
                            outfile.write(f"--- File: {file_path} ---\n")
                            outfile.write(contents + "\n")
                    except UnicodeDecodeError:
                        print(f"Skipping file due to encoding issues: {file_path}")
                    except Exception as e:
                        print(f"Error processing file {file_path}: {e}")

def main():
    source_directory = '/home/subham/output'  # Modify this path to your source directory
    output_file = '/home/subham/output/demo2.txt'   # Modify this path to where you want the output file

    combine_files(source_directory, output_file)

if __name__ == "__main__":
    main()

