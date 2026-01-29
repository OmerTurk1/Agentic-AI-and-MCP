# 🧠 Python MCP (Model Context Protocol) Agent

This project is an example of a Python-based MCP (Model Context Protocol) agent.
The goal is to enable an LLM (OpenAI) to use computer resources in a controlled and secure way
through tools.

This agent:
- Uses tool calling
- Can create files
- Implements an MCP-compliant agent loop
- Follows a sandbox (isolated file system) approach

## 📁 Project Structure
```bash
MCP_Project/
│
├── main.py                 # Agent loop (MCP flow)
├── client.py               # OpenAI API adapter
├── tools.py                # Real system operations
├── tool_registry.py        # Tool → function mapping
├── schemas.py              # Tool JSON schemas
├── config.py               # Configuration & security
│
├── mcp_workspace/          # Sandbox (AI-accessible area)
│   └── (generated files)
│
├── requirements.txt        # Python dependencies
└── README.md               # Project documentation
```

## 🧩 MCP Architecture (Overview)

🔐 The model never accesses the file system directly.
All permissions and execution are controlled by the MCP server.

### Features of MCP Server

- add file: using add_file schema, Agent can add files in mcp_workspace folder.
- read file: using read_file schema, Agent can read files in mcp_workspace folder.
- delete file: using delete_file schema, Agent can delete files in mcp_workspace folder.
- list files: using list_files schema, Agent can list files and folders in mcp_workspace folder.
- rename file: using rename_file schema, Agent can rename files and folders in mcp_workspace folder.
