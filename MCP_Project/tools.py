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