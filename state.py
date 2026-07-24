from typing import Any, Dict, List, Optional, TypedDict


class TicketState(TypedDict):
    """
    Shared state passed between all LangGraph nodes.
    """

    # Input
    raw_email: str

    # Extracted identifiers
    ticket_id: Optional[str]
    customer_id: Optional[str]

    # Data populated by database tools
    customer_info: Optional[Dict[str, Any]]
    ticket_details: Optional[List[Dict[str, Any]]]
    kb_articles: Optional[List[Dict[str, Any]]]

    # Classification Agent Output
    category: Optional[str]
    sentiment: Optional[str]
    urgency: Optional[str]

    # Routing Information
    requires_tool: Optional[bool]
    tool_name: Optional[str]

    # Response Agent Output
    draft_response: Optional[str]

    # Final Ticket Status
    resolution_status: Optional[str]