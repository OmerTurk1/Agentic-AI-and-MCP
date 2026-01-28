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
