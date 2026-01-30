create_file_schema = {
    "type": "function",
    "function": {
        "name": "create_file",
        "description": "Creates file in sandbox folder",
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
        "description": "Reads a file in sandbox folder",
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
        "description": "Deletes a file in sandbox folder",
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

list_files_schema = {
    "type": "function",
    "function": {
        "name": "list_files",
        "description": "Lists the folders and files in sandbox folder",
        "parameters": {
            "type": "object",
            "properties": {}
        }
    }
}

rename_file_schema = {
    "type": "function",
    "function": {
        "name": "rename_file",
        "description": "Renames a file or folder in sandbox folder",
        "parameters": {
            "type": "object",
            "properties": {
                "oldname": {
                    "type": "string",
                    "description": "Mevcut dosya veya klasör adı"
                },
                "newname": {
                    "type": "string",
                    "description": "Yeni ad"
                }
            },
            "required": ["oldname", "newname"]
        }
    }
}

TOOLS = [
    create_file_schema,
    read_file_schema,
    delete_file_schema,
    list_files_schema,
    rename_file_schema
]