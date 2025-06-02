from modules.prompt import get_user_input
from modules.vite_react import setup_vite_react, install_dependencies
from modules.tailwind import configure_tailwind
from modules.structure.index import create_project_structure
import os

def main():
    project_name, install_scope = get_user_input()
    setup_vite_react(project_name)
    project_path = os.path.abspath(project_name)
    install_dependencies(project_path, install_scope)
    configure_tailwind(project_path)
    create_project_structure(project_path)

    print("\n✅ Project berhasil dibuat!")
    print(f"\n➡️ Jalankan dengan:\ncd {project_name}\nnpm run dev")

if __name__ == "__main__":
    main()

