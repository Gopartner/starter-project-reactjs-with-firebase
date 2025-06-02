from .utils import write_file
import os

def configure_tailwind(project_path):
    print("\n🎨 Setup TailwindCSS...")
    write_file(os.path.join(project_path, "tailwind.config.js"), '''/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {},
  },
  plugins: [],
}
''')

    write_file(os.path.join(project_path, "src/index.css"), '''@tailwind base;
@tailwind components;
@tailwind utilities;
''')

