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

TOOLS = [create_file_schema]
