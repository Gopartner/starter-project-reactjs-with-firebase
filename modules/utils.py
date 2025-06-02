import subprocess

def run(command, cwd=None):
    subprocess.run(command, cwd=cwd, shell=True, check=True)

def write_file(path, content):
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)

