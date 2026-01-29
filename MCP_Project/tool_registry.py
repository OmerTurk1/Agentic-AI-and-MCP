from tools import create_file, read_file, delete_file, list_files, rename_file

TOOL_REGISTRY = {
    "create_file": create_file,
    "read_file": read_file,
    "delete_file": delete_file,
    "list_files":list_files,
    "rename_file":rename_file
}
