import os
import shutil


user_folder = os.path.expanduser("~")

source_folder = os.path.join(user_folder, "Downloads")

destinations = {
    ".pdf": os.path.join(user_folder, "Documents", "PDFs"),
    ".docx": os.path.join(user_folder, "Documents", "WordDocs"),
    ".xlsx": os.path.join(user_folder, "Documents", "ExcelSheets"),
    ".jpg": os.path.join(user_folder, "Pictures", "Images"),
    ".png": os.path.join(user_folder, "Pictures", "Images"),
    ".mp4": os.path.join(user_folder, "Videos"),
    ".mp3": os.path.join(user_folder, "Music")
}

for file in os.listdir(source_folder):
    file_path = os.path.join(source_folder, file)
    if os.path.isfile(file_path):
        file_ext = os.path.splitext(file)[1].lower()
        if file_ext in destinations:
            dest_path = destinations[file_ext]
            os.makedirs(dest_path, exist_ok=True)
            shutil.move(file_path, os.path.join(dest_path, file))
            print(f'Moved: {file} to {dest_path}')

os.system('schtasks /Change /TN "OrganizerBot" /Disable')
