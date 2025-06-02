from .folders import create_folders
from .files import create_files
from .delete_file import delete_file
from .set_scripts_package_json import set_scripts_package
import os

def create_project_structure(project_path):
    path_src = os.path.join(project_path, "src")
    create_folders(project_path)
    create_files(project_path)
    delete_file(path_src, "App.css")
    set_scripts_package(project_path)

