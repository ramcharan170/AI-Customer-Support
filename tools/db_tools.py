from data.mock_db import MOCK_DATABASE
def fetch_user_orders(user_id:str)->list:
    #the Green one is the Doc string used for Documentation
    """Retrieves all order history assossiated with a specific user ID.
    Args:
    user_id (str): The unique identifier for the user (e.g 'U101').
    Returns:
    list:A list of dictionaries containing order details, or an empty list if no orders exist.
    """
    user_orders=[
        order for order_id,order in MOCK_DATABASE["orders"].items()
        if order["user_id"]==user_id
    ]
    return user_orders

def fetch_user_profile(user_id:str)->dict:
    """Retrieves user profile information (name,email,membership tier) using their user ID.
    Args:
    user_id(str): The unique identifier fpr the user (e.g,'U101').
    Returns:
    dict:User profile Data if founnd, or an error dictionary if the user ID is invalid.
    """
    user=MOCK_DATABASE["users"].get(user_id)
    if not user:
        return {"error":"User not found"}
    return user

if __name__ =="__main__":
    print("Testing fetch_user_orders for U101:")
    print(fetch_user_orders("U101"))
    print("\n Testing fetch_user_profile for U101:")
    print(fetch_user_profile("U101"))
