import os

def delete_file(path: str, nama_file: str):
    """
    Menghapus file berdasarkan path dan nama file.

    Args:
        path (str): Direktori tempat file berada.
        nama_file (str): Nama file yang akan dihapus.

    Returns:
        bool: True jika berhasil dihapus, False jika gagal atau file tidak ada.
    """
    full_path = os.path.join(path, nama_file)

    if os.path.exists(full_path):
        try:
            os.remove(full_path)
            print(f"File '{nama_file}' berhasil dihapus.")
            return True
        except Exception as e:
            print(f"Gagal menghapus file: {e}")
            return False
    else:
        print(f"File '{nama_file}' tidak ditemukan di {path}.")
        return False

