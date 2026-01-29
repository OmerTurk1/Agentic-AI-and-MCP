import os
from config import BASE_DIR

def create_file(filename: str, content: str):
    path = os.path.abspath(os.path.join(BASE_DIR, filename))

    if not path.startswith(os.path.abspath(BASE_DIR)):
        raise ValueError("Yetkisiz dosya yolu")

    with open(path, "w", encoding="utf-8") as f:
        f.write(content)

    return {
        "status": "ok",
        "message": f"{filename} oluşturuldu"
    }

def read_file(filename: str):
    filename = os.path.basename(filename)
    path = os.path.join(BASE_DIR, filename)

    if not os.path.exists(path):
        return {"status": "error", "message": "Dosya bulunamadı"}

    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    return {
        "status": "ok",
        "content": content
    }

def delete_file(filename: str):
    filename = os.path.basename(filename)
    path = os.path.join(BASE_DIR, filename)

    if not os.path.exists(path):
        return {
            "status": "error",
            "message": "Dosya bulunamadı"
        }

    os.remove(path)

    return {
        "status": "ok",
        "message": f"{filename} silindi"
    }

def list_files():
    try:
        items = os.listdir(BASE_DIR)
    except FileNotFoundError:
        return {
            "status": "error",
            "message": "Workspace bulunamadı"
        }

    files = []
    directories = []

    for item in items:
        path = os.path.join(BASE_DIR, item)
        if os.path.isfile(path):
            files.append(item)
        elif os.path.isdir(path):
            directories.append(item)

    return {
        "status": "ok",
        "files": files,
        "directories": directories
    }


def rename_file(oldname: str, newname: str):
    oldname = os.path.basename(oldname)
    newname = os.path.basename(newname)

    old_path = os.path.join(BASE_DIR, oldname)
    new_path = os.path.join(BASE_DIR, newname)

    if not os.path.exists(old_path):
        return {
            "status": "error",
            "message": "Kaynak dosya veya klasör bulunamadı"
        }

    if os.path.exists(new_path):
        return {
            "status": "error",
            "message": "Hedef isim zaten mevcut"
        }

    os.rename(old_path, new_path)

    return {
        "status": "ok",
        "message": f"{oldname} → {newname} olarak yeniden adlandırıldı"
    }