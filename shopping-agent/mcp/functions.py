import asyncio
from mcp_client import TOOLS, tool_calling

result = asyncio.run(tool_calling(TOOLS[0], {"depth": 1}, "markdown"))
print(result['message'])

def get_categories() -> str:
    result = asyncio.run(tool_calling(TOOLS["list_categories"], {"depth": 1}, "markdown"))
    return result['message']