from pathlib import Path
folder_path=input("Enter the folder path : ")
folder=Path(folder_path)
if folder.exists():
    print("File found")
else:
    print("File not found")
for item in folder.iterdir():
    if item.is_file():
        extension=item.suffix.lower()
        category=get_category(extension)
        move_file(item,category)
