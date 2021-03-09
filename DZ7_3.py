import os.path
from shutil import copy2, SameFileError

proj_dir = "my_project"
for cur_path, dirs, elements in os.walk(proj_dir):
    if "base.html" and "index.html" in elements:
        dest_path = os.path.join(proj_dir, "templates", os.path.basename(cur_path))
        if not os.path.exists(dest_path):
            os.makedirs(dest_path)
        try:
            copy2(os.path.join(cur_path, "base.html"), os.path.join(dest_path, "base.html"))
            copy2(os.path.join(cur_path, "index.html"), os.path.join(dest_path, "index.html"))
        except SameFileError:
            print("Такие файлы уже есть в папке!")
