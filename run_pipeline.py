"""
Main entry point for the Multi-Agent Customer Ticket Router System.
"""

from agents.classifier_agent import classify_ticket
from agents.response_agent import generate_response
from graph.router import execute_tool


def main():

    state = {
        "raw_email": """
Hi,

I was charged twice for my Wireless Mouse.

Please refund the extra amount immediately.

Thanks.
""",
        # Demo customer
        "customer_id": "U101",
    }

    print("=" * 60)
    print("📩 Incoming Ticket")
    print("=" * 60)
    print(state["raw_email"])

    # -----------------------------
    # Step 1 - Classification Agent
    # -----------------------------
    print("\n🔹 Running Classification Agent...")

    state = classify_ticket(state)

    print("✅ Classification Complete")
    print(f"Category       : {state['category']}")
    print(f"Sentiment      : {state['sentiment']}")
    print(f"Urgency        : {state['urgency']}")
    print(f"Requires Tool  : {state['requires_tool']}")
    print(f"Tool Selected  : {state['tool_name']}")

    # -----------------------------
    # Step 2 - Tool Execution
    # -----------------------------
    print("\n🔹 Running Tool Router...")

    state = execute_tool(state)

    print("✅ Tool Execution Complete")

    print("\nCustomer Info:")
    print(state.get("customer_info"))

    print("\nTicket Details:")
    print(state.get("ticket_details"))

    # -----------------------------
    # Step 3 - Response Agent
    # -----------------------------
    print("\n🔹 Running Response Agent...")

    state = generate_response(state)

    print(" Response Generated")

    print("\n" + "=" * 60)
    print("📧 Final Customer Reply")
    print("=" * 60)

    print(state["draft_response"])

    print("=" * 60)
    print("🎉 Pipeline Completed Successfully")
    print("=" * 60)


if __name__ == "__main__":
    main()