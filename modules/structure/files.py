import os
from modules.utils import write_file

def read_template(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        return f.read()

def create_files(project_path):
    print("\n📝 Membuat file-template...")

    # Baca semua template dari folder modules/templates
    app_jsx      = read_template("modules/templates/App.jsx")
    home_jsx     = read_template("modules/templates/Home.jsx")
    env_content  = read_template("modules/templates/env.template")
    firebase_js  = read_template("modules/templates/firebase.js")

    files = {
        "src/App.jsx": app_jsx,
        "src/pages/Home.jsx": home_jsx,
        ".env": env_content,
        "src/utils/firebase.js": firebase_js,
    }

    for relative_path, content in files.items():
        full_path = os.path.join(project_path, relative_path)
        write_file(full_path, content)

