import os
import shutil

# Define the directory to clean (Change this to your path)
directory = r"C:\Users\ammyj\Desktop\Files"

# Map extensions to folder names
extensions = {
    '.jpg': 'Images', '.png': 'Images', '.jpeg': 'Images',
    '.pdf': 'Documents', '.docx': 'Documents', '.txt': 'Documents',
    '.ppt': 'Presentations', '.pptx': 'Presentations',
    '.mp4': 'Videos', '.mov': 'Videos', '.srt': 'Subtitles',
    '.exe': 'Applications', '.msi': 'Applications',
    '.zip': 'Archives', '.rar': 'Archives'
}


def organize_files():
    if not os.path.exists(directory):
        print("Path not found!")
        return

    for filename in os.listdir(directory):
        filepath = os.path.join(directory, filename)

        # Skip if it's a folder
        if os.path.isdir(filepath):
            continue

        file_ext = os.path.splitext(filename)[1].lower()

        if file_ext in extensions:
            folder_name = extensions[file_ext]
            folder_path = os.path.join(directory, folder_name)

            # Create folder if it doesn't exist
            os.makedirs(folder_path, exist_ok=True)

            # Move the file
            shutil.move(filepath, os.path.join(folder_path, filename))
            print(f"Moved: {filename} -> {folder_name}")


if __name__ == "__main__":
    organize_files()
    print("Cleanup complete!")
