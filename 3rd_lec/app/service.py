import os
from typing import Protocol

from dotenv import load_dotenv
from openai import AsyncOpenAI

load_dotenv()


class Summarizer(Protocol):
    async def __call__(self, ticket: str) -> str:
        ...


client = AsyncOpenAI(
    api_key=os.getenv("OPENROUTER_API_KEY"),
    base_url="https://openrouter.ai/api/v1",
)

MODEL = os.getenv(
    "OPENAI_MODEL",
    "nvidia/nemotron-3-ultra-550b-a55b:free",
)


async def summarize_ticket(ticket: str) -> str:
    response = await client.chat.completions.create(
        model=MODEL,
        messages=[
            {
                "role": "system",
                "content": "Summarize the customer support ticket clearly and briefly.",
            },
            {
                "role": "user",
                "content": ticket,
            },
        ],
    )

    return response.choices[0].message.content