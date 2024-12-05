from pathlib import Path

parent_folder_path = Path(".")

def parse_folder(path):
    for element in path.iterdir():
        if element.is_dir():
            print(f"This is folder - {element.name}")
            parse_folder(element)
        if element.is_file():
            print(f"This is file - {element.name}")

parse_folder(parent_folder_path)