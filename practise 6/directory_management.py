import os
nested_path = os.path.join("main_folder", "sub_folder", "nested")
os.makedirs(nested_path, exist_ok=True)

import os
path = "."  
items = os.listdir(path)

for item in items:
    print(item)


import os
extension = ".txt"
txt_files = [f for f in os.listdir(".") if f.endswith(extension)]

print(f"Files with extensions: {extension}:")
print(txt_files)


import os
import shutil

os.makedirs("destination_folder", exist_ok=True)
shutil.move("sample.txt", os.path.join("destination_folder", "sample.txt"))



