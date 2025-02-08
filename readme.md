# Automatic File Organizer

A Python script that automatically organizes files in your Downloads folder by categorizing them into different folders based on their file extensions.

## Features

- Automatically categorizes files into:
  - Documents (pdf, docx, txt, etc.)
  - Images (jpg, png, gif, etc.)
  - Videos (mp4, webm, avi, etc.)
  - Audio (mp3, wav, opus)
  - Archives (zip, rar, 7z, etc.)
  - Executables (exe, msi, bat, etc.)
  - Code (py, js, html, etc.)
  - Others (uncategorized files)

- Creates subfolders automatically when a category exceeds 100 files
- Handles file organization recursively through the directory

## Requirements

- Python 3.x
- No additional dependencies required (uses built-in libraries only)

## Installation

1. Clone or download this repository
2. Navigate to the project directory

## Usage

1. By default, the script is configured to organize files in the Windows Downloads folder:
   ```python
   python sorter.py
   ```

2. To change the target directory, modify the `directory` variable in the `main()` function:
   ```python
   directory = r"Your\Path\Here"
   ```

## How It Works

1. The script defines categories and their associated file extensions
2. When run, it:
   - Scans the specified directory
   - Categorizes each file based on its extension
   - Creates category folders if they don't exist
   - Creates subfolders if a category has more than 100 files
   - Moves files to their respective folders

## Warning

Always backup your files before running any automated file organization tool.

## Contributing

Feel free to submit issues, fork the repository, and create pull requests for any improvements.