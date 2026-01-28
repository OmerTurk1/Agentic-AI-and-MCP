import json
from client import send_to_model
from tool_registry import TOOL_REGISTRY

messages = [
    {"role": "system", "content": "You are an MCP Agent. If necessary, use tool."}
]

print("MCP Agent is ready. Press Ctrl+C to exit")

while True:
    user_input = input(">>> ")
    messages.append({"role": "user", "content": user_input})

    while True:
        response = send_to_model(messages)
        message = response.choices[0].message

        # If model calls tool
        if message.tool_calls:
            messages.append(message)  # !!! important

            for call in message.tool_calls:
                tool_name = call.function.name
                args = json.loads(call.function.arguments)

                tool_fn = TOOL_REGISTRY[tool_name]
                result = tool_fn(**args)

                messages.append({
                    "role": "tool",
                    "tool_call_id": call.id,
                    "content": json.dumps(result)
                })

            # call model again after tool
            continue

        # if normal answer is came
        print(message.content)
        messages.append(message)
        break
