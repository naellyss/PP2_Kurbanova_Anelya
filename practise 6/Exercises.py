# 1
import os
path = "."  

all_items = os.listdir(path)
directories = [item for item in all_items if os.path.isdir(os.path.join(path, item))]
files = [item for item in all_items if os.path.isfile(os.path.join(path, item))]

print("Only Directories: ", directories)
print("Only files: ", files)
print("All: ", all_items)


# 2
import os

path = "sample.txt"  

print(f"Access: {path}")
print("Existing (F_OK):", os.access(path, os.F_OK))
print("Read (R_OK):", os.access(path, os.R_OK))
print("Write (W_OK):", os.access(path, os.W_OK))
print("Execution (X_OK):", os.access(path, os.X_OK))


# 3
import os

path = "./destination_folder/sample.txt"

if os.path.exists(path):
    directory_name = os.path.dirname(path)
    file_name = os.path.basename(path)
    
    print("Directory: ", directory_name)
    print("File: ", file_name)
else:
    print("Path does not exist.")


# 4
def count_lines(filepath):
    try:
        with open(filepath, "r", encoding="utf-8") as file:
            line_count = sum(1 for _ in file)
        return line_count
    except FileNotFoundError:
        return "File was not found"

with open("data.txt", "w", encoding="utf-8") as f:
    f.write("Line 1\nLine2\nLine 3\n")

print(count_lines("data.txt"))


# 5
my_list = ["Apple", "Banana", "Pear", "Orange"]

with open("fruits.txt", "w", encoding="utf-8") as file:
    for item in my_list:
        file.write(f"{item}\n")


#6
import string

for letter in string.ascii_uppercase:
    filename = f"{letter}.txt"
    with open(filename, "w", encoding="utf-8") as file:
        file.write(f"This file {filename}\n")


# 7
source_file = "fruits.txt"
destination_file = "fruits_copy.txt"

with open(source_file, "r", encoding="utf-8") as src, open(destination_file, "w", encoding="utf-8") as dest:
    dest.write(src.read())


# 8 
import os

target_path = "fruits_copy.txt"

if os.path.exists(target_path):

    if os.access(target_path, os.W_OK):
        os.remove(target_path)
        print(f"File '{target_path}' is successfully deleted.")
    else:
        print(f"No rights for deleting '{target_path}'.")
else:
    print(f"File '{target_path}' does not exist.")

