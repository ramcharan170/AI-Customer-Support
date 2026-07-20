MOCK_DATABASE={
    "users":{
        "U101":{"name":"Alice Smith","email":"alice@example.com","plan":"Premium"},
        "U103":{"name":"Bob Jones","email":"bob@example.com","plan":"Free"},
    },
    "orders": {
        "O5001": {"user_id": "U101", "item": "Wireless Mouse", "amount": 25.00, "status": "Delivered"},
        "O5002": {"user_id": "U101", "item": "Wireless Mouse", "amount": 25.00, "status": "Duplicate Charge"},
        "O5003": {"user_id": "U102", "item": "Mechanical Keyboard", "amount": 80.00, "status": "Shipped"}
    },
    "tickets": {
        "T900": {"user_id": "U101", "issue": "Double charge on mouse", "status": "Open"}
    }
}