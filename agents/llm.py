"""
Shared LLM client configuration.
Supports multiple providers.
"""

import os
from typing import Type, TypeVar

from dotenv import load_dotenv
from openai import OpenAI
from pydantic import BaseModel

from utils.logger import logger

load_dotenv()

PROVIDER = os.getenv("LLM_PROVIDER", "openai").lower()
MODEL_NAME = os.getenv("MODEL_NAME")

if PROVIDER == "openai":
    client = OpenAI(
        api_key=os.getenv("OPENAI_API_KEY")
    )

elif PROVIDER == "openrouter":
    client = OpenAI(
        api_key=os.getenv("OPENROUTER_API_KEY"),
        base_url="https://openrouter.ai/api/v1",
    )

else:
    raise ValueError(f"Unsupported provider: {PROVIDER}")


T = TypeVar("T", bound=BaseModel)


def invoke_structured_llm(
    *,
    system_prompt: str,
    user_prompt: str,
    output_model: Type[T],
    temperature: float = 0,
) -> T:
    """
    Sends a prompt to the LLM and validates the JSON response
    against a Pydantic model.
    """

    try:
        response = client.chat.completions.create(
            model=MODEL_NAME,
            temperature=temperature,
            response_format={"type": "json_object"},
            messages=[
                {
                    "role": "system",
                    "content": system_prompt,
                },
                {
                    "role": "user",
                    "content": user_prompt,
                },
            ],
        )

        content = response.choices[0].message.content

        return output_model.model_validate_json(content)

    except Exception as e:
        logger.error(f"LLM request failed: {e}")

        raise RuntimeError(
            f"LLM request failed: {e}"
        ) from e