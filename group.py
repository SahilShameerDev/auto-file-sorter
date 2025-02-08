import os
from collections import defaultdict

def group_extensions(directory):
    # Dictionary to hold the count of files for each extension
    extension_count = defaultdict(int)
    
    # Walk through the directory
    for root, dirs, files in os.walk(directory):
        for file in files:
            # Get the file extension
            _, ext = os.path.splitext(file)
            ext = ext.lower()  # Normalize to lowercase
            
            # Update the count for the extension
            extension_count[ext] += 1
    
    return extension_count

def save_to_file(extension_count, output_file):
    with open(output_file, 'w') as f:
        for ext, count in extension_count.items():
            f.write(f"Extension: {ext}, Number of files: {count}\n")

def main():
    # Provide the directory path here
    directory = input("Enter the directory path: ")
    
    # Get the extension count
    extension_count = group_extensions(directory)
    
    # Display the results
    for ext, count in extension_count.items():
        print(f"Extension: {ext}, Number of files: {count}")
    
    # Save the results to a text file
    output_file = "extension_report.txt"
    save_to_file(extension_count, output_file)
    print(f"Report saved to {output_file}")

if __name__ == "__main__":
    main()