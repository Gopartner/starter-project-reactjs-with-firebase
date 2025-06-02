from .utils import run

def setup_vite_react(project_name):
    print("\n🚀 Membuat project dengan Vite + React...")
    run(f"npm create vite@latest {project_name} -- --template react")

def install_dependencies(project_path, install_scope):
    print("\n📦 Install dependencies...")
    run("npm install", cwd=project_path)
    run("npm install -D tailwindcss@3 postcss autoprefixer", cwd=project_path)
    run("npx tailwindcss init -p", cwd=project_path)
    run("npm install react-router-dom", cwd=project_path)
    if install_scope == 'l':
        run("npm install firebase", cwd=project_path)
    else:
        run("npm install -g firebase")

