import json
import os

def set_scripts_package(project_path):
    package_json_path = os.path.join(project_path, "package.json")

    if not os.path.exists(package_json_path):
        print("❌ package.json tidak ditemukan.")
        return

    try:
        with open(package_json_path, "r") as f:
            data = json.load(f)

        # Script baru yang mau ditambahkan/diupdate
        new_scripts = {
            "dev": "vite --host",
            "build": "vite build",
            "deploy": "firebase deploy",
            "lint": "eslint .",
            "preview": "vite preview"
        }

        # Jika key "scripts" belum ada, buat baru
        if "scripts" not in data or not isinstance(data["scripts"], dict):
            data["scripts"] = {}

        # Update/merge scripts
        data["scripts"].update(new_scripts)

        # Tulis ulang dengan indentasi rapi
        with open(package_json_path, "w") as f:
            json.dump(data, f, indent=2)

        print("✅ Scripts di package.json berhasil diperbarui.")

    except Exception as e:
        print(f"❌ Gagal memproses package.json: {e}")

