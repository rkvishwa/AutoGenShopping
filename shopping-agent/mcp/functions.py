import asyncio
from mcp_client import tool_calling

def get_categories() -> str:
    result = asyncio.run(tool_calling("list_categories", {"depth": 1}, "markdown"))
    return result['message']

print(get_categories())