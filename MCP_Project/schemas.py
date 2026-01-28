create_file_schema = {
    "type": "function",
    "function": {
        "name": "create_file",
        "description": "Güvenli klasör içinde dosya oluşturur",
        "parameters": {
            "type": "object",
            "properties": {
                "filename": {
                    "type": "string"
                },
                "content": {
                    "type": "string"
                }
            },
            "required": ["filename", "content"]
        }
    }
}

read_file_schema = {
    "type": "function",
    "function": {
        "name": "read_file",
        "description": "Sandbox içindeki bir dosyanın içeriğini okur",
        "parameters": {
            "type": "object",
            "properties": {
                "filename": {
                    "type": "string",
                    "description": "Okunacak dosya adı"
                }
            },
            "required": ["filename"]
        }
    }
}

delete_file_schema = {
    "type": "function",
    "function": {
        "name": "delete_file",
        "description": "Sandbox içindeki bir dosyayı siler",
        "parameters": {
            "type": "object",
            "properties": {
                "filename": {
                    "type": "string",
                    "description": "Silinecek dosya adı"
                }
            },
            "required": ["filename"]
        }
    }
}

TOOLS = [
    create_file_schema,
    read_file_schema,
    delete_file_schema
]