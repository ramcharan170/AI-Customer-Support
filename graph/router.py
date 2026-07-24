"""
Router for executing database tools based on
the classifier's decision.
"""

from state import TicketState

from tools.db_tools import (
    fetch_user_orders,
    fetch_user_profile,
)

# Tool Registry
TOOLS = {
    "fetch_user_orders": fetch_user_orders,
}


def execute_tool(state: TicketState) -> TicketState:
    """
    Executes database tools and updates the shared state.
    """

    customer_id = state.get("customer_id")

    if not customer_id:
        print("Warning: customer_id is missing.")
        return state

    # Always fetch customer profile
    state["customer_info"] = fetch_user_profile(customer_id)

    # If no additional lookup is needed, return
    if not state.get("requires_tool"):
        return state

    tool_name = state.get("tool_name")

    tool = TOOLS.get(tool_name)

    if tool:
        state["ticket_details"] = tool(customer_id)
    else:
        print(f"Warning: Unknown tool '{tool_name}'")

    return state