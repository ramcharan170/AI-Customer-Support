from state import TicketState

from agents.llm import invoke_structured_llm
from agents.models import TicketClassification
from agents.prompts import CLASSIFIER_SYSTEM_PROMPT


def classify_ticket(state: TicketState) -> TicketState:

    classification = invoke_structured_llm(
        system_prompt=CLASSIFIER_SYSTEM_PROMPT,
        user_prompt=state["raw_email"],
        output_model=TicketClassification,
    )

    return {
        **state,
        "category": classification.category,
        "sentiment": classification.sentiment,
        "urgency": classification.urgency,
        "requires_tool": classification.requires_tool,
        "tool_name": classification.tool_name,
    }