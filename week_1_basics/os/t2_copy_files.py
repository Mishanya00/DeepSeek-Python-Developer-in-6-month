import os
import sys
import shutil  # high-level file operations

"""
Create a script that copies all files from one directory to another,
excluding files with a specific extension.
"""

if len(sys.argv) < 2:
    print(
        "Usage: py -3 t2_copy_files.py <destination folder> [<source folder>] [<excluded extension>]"
    )
    print(
        "If <source folder> is not provided, it defaults to the current working directory."
    )
    print("If <excluded extension> is not provided, all files will be copied.")
    sys.exit(1)

dest_path = os.path.abspath(sys.argv[1])

if len(sys.argv) >= 3:
    source_path = os.path.abspath(sys.argv[2])
else:
    source_path = os.getcwd()

excluded_extension = ""

if len(sys.argv) == 4:
    excluded_extension = sys.argv[3]
    if not excluded_extension.startswith("."):
        excluded_extension = "." + excluded_extension

if not os.path.exists(source_path):
    print("Error: non-existent source path ({})".format(source_path))
    exit(1)

if not os.path.exists(dest_path):
    print(f"Warning: non-existent destination path ({dest_path})")
    os.mkdir(dest_path)
    print(f"Folder {dest_path} has beed created.")

print("- - - - - - - - - - - - - - - - - - - - - - - - - - -")
print("Hello, " + os.getlogin() + "!")
print("Directory to copy from:", source_path)
print("Directory to copy into:", dest_path)
print(
    "Excluded file extension:",
)
print("- - - - - - - - - - - - - - - - - - - - - - - - - - -")

for file in os.listdir(source_path):
    path = source_path + "/" + file
    if os.path.isfile(path):
        if len(excluded_extension) > 0:
            if path.endswith(excluded_extension):
                continue
        try:
            shutil.copy(path, dest_path)
            print("File {} copied to {}".format(path, dest_path))
        except Exception:
            print("Error trying to copy from {} to {}".format(path, dest_path))
            print(Exception)
