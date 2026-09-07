from mcp_tools.functions import get_categories

async def show_categories():
    '''Fetch available category'''
    
    result = await get_categories("json")
    
    if result['status'] != "success":
        return "I'm sorry, I couldn't get the categories right now. Please try again."
    
    category_json = result['message']['categories']
    categories = [category['name'] for category in category_json]
    category_string = "\n ▶︎ ".join(categories)
    
    
    
    return f"Available categories: \n {category_string} \n\nSo what you want to buy? I am here to help you.😊"
    
    