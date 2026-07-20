from data.mock_db import MOCK_DATABASE
def fetch_user_orders(user_id:str)->list:
    user_orders=[
        order for order_id,order in MOCK_DATABASE["orders"].items()
        if order["user_id"]==user_id
    ]
    if not user_orders:
        return [f"No orders found for User ID:{user_id}"]
    if not user_orders:
        return[f"No orders found for User ID:{user_id}"]
    return user_orders

def fetch_user_profile(user_id:str)->dict:
    user=MOCK_DATABASE["users"].get(user_id)
    if not user:
        return {"error":"User not found"}
    return user

if __name__ =="__main__":
    print("Testing fetch_user_orders for U101:")
    print(fetch_user_orders("U101"))
