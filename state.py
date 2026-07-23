from typing import Any,Dict,List,Optional, TypedDict

class TicketState(TypedDict):
    raw_email:str
    ticket_id:Optional[str]
    customer_id:Optional[str]

    customer_info:Optional[Dict[str,Any]]
    ticket_details:Optional[Dict[str,Any]]
    kb_articles:Optional[List[Dict[str,Any]]]

    category:Optional[str]
    urgency:Optional[str]
    draft_response:Optional[str]
    resolutional_status:Optional[str]
    
    sentiment: Optional[str]
    requires_tool: Optional[bool]
    tool_name: Optional[str]