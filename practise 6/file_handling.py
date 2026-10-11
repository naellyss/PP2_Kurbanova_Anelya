with open("sample.txt", "w", encoding="utf-8") as file:
    file.write("First line.\n")
    file.write("Second line.\n")


with open("sample.txt", "r", encoding="utf-8") as file:
    content = file.read()

print(content)


with open("sample.txt", "a", encoding="utf-8") as file:
    file.write("Third line.\n")

with open("sample.txt", "r", encoding="utf-8") as file:
    print(file.read())


import shutil
shutil.copy("sample.txt", "sample_backup.txt")


import os
filename = "sample_backup.txt"

if os.path.exists(filename):
    os.remove(filename)
    print(f"File {filename} is found.")
else:
    print(f"File {filename} was not found")


