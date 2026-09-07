import asyncio
from .mcp_client import tool_calling

async def get_categories(type: str = "json") -> dict:
    result = await tool_calling("list_categories", {"depth": 1}, type)
    return result


