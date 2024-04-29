import os
import subprocess

def run_flawfinder(file_path):
    """
    Run flawfinder on a given C/C++ file and return line numbers with vulnerabilities.
    """
    command = ["flawfinder", "--quiet", "--csv", "--columns", "1", file_path]
    result = subprocess.run(command, capture_output=True, text=True)
    vulnerabilities = []
    if result.stdout:
        lines = result.stdout.splitlines()
        for line in lines:
            parts = line.split(",")
            if len(parts) >= 2:  # Check if parts contains at least two elements
                file_path, line_number = parts[0], parts[1]
                vulnerabilities.append((file_path, line_number))
    return vulnerabilities

def find_vulnerabilities(directory):
    """
    Recursively search for C, C++, and header files in the given directory, run flawfinder on each,
    and collect line numbers with vulnerabilities.
    """
    vulnerabilities = []
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(('.c', '.cpp', '.h', '.nc')):  # Checking for multiple file extensions
                file_path = os.path.join(root, file)
                file_vulnerabilities = run_flawfinder(file_path)
                vulnerabilities.extend(file_vulnerabilities)
    return vulnerabilities

def save_vulnerabilities(vulnerabilities, output_file):
    """
    Save the list of vulnerabilities into the specified output file.
    """
    with open(output_file, "w") as f:
        for file_path, line_number in vulnerabilities:
            f.write(f"{file_path}:{line_number}\n")

if __name__ == "__main__":
    directory = "/home/subham/all_os_code"
    output_file = "/home/subham/output/flawfinder_output.txt"

    vulnerabilities = find_vulnerabilities(directory)
    save_vulnerabilities(vulnerabilities, output_file)

    print("Vulnerabilities saved to", output_file)

