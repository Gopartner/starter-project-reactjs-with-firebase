def get_user_input():
    project_name = input("Masukkan nama project: ").strip()
    install_scope = input("Install firebase secara [l]okal atau [g]lobal? (l/g): ").strip().lower()
    if install_scope not in ['l', 'g']:
        install_scope = 'l'
    return project_name, install_scope

