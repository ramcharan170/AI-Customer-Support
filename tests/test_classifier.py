from agents.classifier_agent import classify_ticket

state = {
    "raw_email": """
Hi,

I was charged twice for my Wireless Mouse.

Please refund the extra amount immediately.

Thanks.
"""
}

updated_state = classify_ticket(state)

print(updated_state)