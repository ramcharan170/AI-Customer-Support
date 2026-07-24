from agents.response_agent import generate_response

state = {
    "raw_email": """
Hi,

I was charged twice for my Wireless Mouse.

Please refund the extra amount immediately.

Thanks.
""",

    "customer_info": {
        "name": "Alice Smith",
        "email": "alice@example.com",
        "plan": "Premium",
    },

    "ticket_details": [
        {
            "item": "Wireless Mouse",
            "status": "Duplicate Charge",
        }
    ],

    "category": "Refund",
    "sentiment": "Frustrated",
    "urgency": "High",
}

updated_state = generate_response(state)

print(updated_state["draft_response"])