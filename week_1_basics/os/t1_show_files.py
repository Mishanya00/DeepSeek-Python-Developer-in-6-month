import os
import sys

"""
Write a script that recursively traverses a directory
and lists all files with a specific extension (e.g., `.txt`).
"""

if len(sys.argv) < 2:
    print("Usage: py -3 t1_show_files.py <file extension> [<directory>]")
    print(
        "If <directory> is not provided, it defaults to the current working directory."
    )
    sys.exit(1)

file_ext = sys.argv[1]

if not file_ext.startswith("."):
    file_ext = "." + file_ext

if len(sys.argv) == 3:
    search_path = os.path.abspath(sys.argv[2])
else:
    search_path = os.getcwd()

if not os.path.exists(search_path):
    print("Error: directory not exist")
    exit(1)

print("- - - - - - - - - - - - - - - - - - - - - - - - - - -")
print("Hello, " + os.getlogin() + "!")
print("Directory to search:", search_path)
print("- - - - - - - - - - - - - - - - - - - - - - - - - - -")

for path, _, files in os.walk(search_path):
    for file in files:
        if file.endswith(file_ext):
            print(os.path.basename(path) + "/" + file)
print("- - - - - - - - - - - - - - - - - - - - - - - - - - -")
