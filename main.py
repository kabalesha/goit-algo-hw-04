from pathlib import Path

## 1
# parent_folder_path = Path(".")
#
# def parse_folder(path):
#     for element in path.iterdir():
#         if element.is_dir():
#             print(f"This is folder - {element.name}")
#             parse_folder(element)
#         if element.is_file():
#             print(f"This is file - {element.name}")
#
# parse_folder(parent_folder_path)

## 2
file_name = Path("./Temp")

try:
    with open(file_name / "test.txt", "r", encoding="utf-8") as file:
        for line in file:
            print(line, end='')

except Exception as e:
    print(f"{e} with file")
