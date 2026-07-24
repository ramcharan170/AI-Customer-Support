"""
Customer Response Agent.

This agent generates a professional customer support reply
based on the current TicketState.
"""

from state import TicketState

from agents.llm import invoke_structured_llm
from agents.models import DraftResponse
from agents.prompts import RESPONSE_SYSTEM_PROMPT


def generate_response(state: TicketState) -> TicketState:
    """
    Generate a customer support response using the current ticket state.
    """

    customer = state.get("customer_info", {})
    orders = state.get("ticket_details", [])

    customer_name = customer.get("name", "Customer")
    customer_plan = customer.get("plan", "Unknown")

    order_summary = ""

    for order in orders:
        order_summary += (
            f"- Item: {order['item']}\n"
            f"  Status: {order['status']}\n"
            f"  Amount: ${order['amount']}\n\n"
        )

    user_prompt = f"""
Customer Email:
{state.get("raw_email")}

Customer Name:
{customer_name}

Membership Plan:
{customer_plan}

Order Information:
{order_summary if order_summary else "No order information available."}

Classification:
Category: {state.get("category")}
Sentiment: {state.get("sentiment")}
Urgency: {state.get("urgency")}
"""

    draft = invoke_structured_llm(
        system_prompt=RESPONSE_SYSTEM_PROMPT,
        user_prompt=user_prompt,
        output_model=DraftResponse,
    )

    return {
        **state,
        "draft_response": draft.response,
    }