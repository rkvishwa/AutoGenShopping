import asyncio
from mcp_client import tool_calling

def get_categories() -> str:
    result = asyncio.run(tool_calling("list_categories", {"depth": 1}, "markdown"))
    return result['message']

def delivery_cities(query: str) -> str:
    result = asyncio.run(tool_calling("delivery_cities", {"query": query, "limit": 25}, "markdown"))
    return result['message']

def search_products(search_query: str, max_price: float, category: str = "", limit: int = 10, currency : str = "LKR", in_stock : bool = 0,  sort: str = "relevance", include_stubs : bool = 0) -> str:
    result = asyncio.run(tool_calling("search_products", {"q": search_query, "category": category, "limit": limit,
"cursor": "a", "currency": currency, "min_price": 0.0, "max_price": max_price, "in_stock_only": in_stock, "sort": sort, "include_stubs": include_stubs}, "markdown"))
    return result['message']

def get_product(p_id: str, currency : str = "LKR", type : str = "") -> str:
    result = asyncio.run(tool_calling("get_product", {"product_id": p_id, "currency": currency, "type": type}, "markdown"))
    return result['message']

def create_order(p_id: str, recipient: str,address: str, city: str, date: str, sender: str, location_type: str = "house", msg: str = "", quantity: int = 1, instructions: str = "", icing_text: str = "", gift_message: str = "", currency : str = "LKR") -> str:
    cart = [{"product_id": p_id, "quantity": quantity, "icing_text": icing_text}]
    kcity = delivery_cities(city)
    delivery = address + kcity + location_type + date + instructions

    result = asyncio.run(tool_calling("create_order", {"cart": cart, "recipient": recipient, "delivery": delivery, "sender": sender, "gift_message": gift_message, "currency": currency}, "markdown"))

    return result['message']

print(create_order("EF_PC_FLOW0V841POD00089P", "Ashen", "wadada", "kurunegala", "2026-01-09", "Tharindu" ))