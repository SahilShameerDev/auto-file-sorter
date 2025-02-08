import os
import shutil
from collections import defaultdict

# Define categories for file extensions
CATEGORIES = {
    "Documents": [".pdf", ".docx", ".doc", ".txt", ".rtf", ".xlsx", ".ppt", ".pptx", ".md", ".csv", ".xml", ".sql", ".sqlite"],
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg", ".webp", ".heic", ".avif", ".ico"],
    "Videos": [".mp4", ".webm", ".avi", ".mkv", ".mov"],
    "Audio": [".mp3", ".wav", ".opus"],
    "Archives": [".zip", ".rar", ".gz", ".7z", ".tar"],
    "Executables": [".exe", ".msi", ".bat", ".cmd", ".jar", ".apk"],
    "Code": [".py", ".js", ".html", ".css", ".pl", ".xml", ".xsl", ".properties", ".pom"],
    "Others": []  # Fallback for uncategorized files
}

# Threshold for creating subfolders
FILES_THRESHOLD = 100

def categorize_file(ext):
    """Categorize a file based on its extension."""
    for category, extensions in CATEGORIES.items():
        if ext in extensions:
            return category
    return "Others"

def organize_files(directory):
    # Dictionary to hold the count of files for each category
    category_count = defaultdict(int)
    
    # Walk through the directory
    for root, dirs, files in os.walk(directory):
        for file in files:
            # Get the file extension
            _, ext = os.path.splitext(file)
            ext = ext.lower()  # Normalize to lowercase
            
            # Categorize the file
            category = categorize_file(ext)
            
            # Create the category folder if it doesn't exist
            category_folder = os.path.join(directory, category)
            if not os.path.exists(category_folder):
                os.makedirs(category_folder)
            
            # If the number of files in the category exceeds the threshold, create subfolders
            if category_count[category] >= FILES_THRESHOLD:
                subfolder = os.path.join(category_folder, f"Subfolder_{category_count[category] // FILES_THRESHOLD}")
                if not os.path.exists(subfolder):
                    os.makedirs(subfolder)
                dest_folder = subfolder
            else:
                dest_folder = category_folder
            
            # Move the file to the appropriate folder
            src_path = os.path.join(root, file)
            dest_path = os.path.join(dest_folder, file)
            shutil.move(src_path, dest_path)
            
            # Update the count for the category
            category_count[category] += 1

def main():
    # Use fixed downloads directory path
    directory = r"C:\Users\smsah\Downloads"
    
    # Organize the files
    organize_files(directory)

if __name__ == "__main__":
    main()
