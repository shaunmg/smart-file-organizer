from pathlib import Path
import shutil

CATEGORY_MAP = {
    "Images": [".jpg", ".jpeg", ".png"],
    "Documents": [".pdf", ".doc", ".txt"],
    "Audio": [".mp3"],
    "Videos": [".mp4", ".mov"]
}


def get_category(extension):
    extension = extension.lower()

    for category, extensions in CATEGORY_MAP.items():
        for ext in extensions:
            if extension == ext:
                return category

    return "Other"

def move_file(item, category):
    destination_folder = item.parent / category

    if not destination_folder.exists():
        destination_folder.mkdir()

    destination=destination_folder/item.name

    shutil.move(item,destination)


folder_path = input("Enter the folder path: ")
folder = Path(folder_path)

if folder.exists():
    print("Folder found")

    for item in folder.iterdir():
        if item.is_file():
            extension = item.suffix
            category = get_category(extension)
            move_file(item, category)
            print(item)
            print(item.parent)
            print(item.name)
            print(item.suffix)
            print()

else:
    print("Folder not found")