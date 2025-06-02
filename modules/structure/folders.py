import os

def create_folders(project_path):
    print("\n📁 Membuat struktur folder...")
    folders = [
        "src/pages",
        "src/components",
        "src/utils"
    ]
    for folder in folders:
        os.makedirs(os.path.join(project_path, folder), exist_ok=True)

