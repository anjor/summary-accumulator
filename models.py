import os
from typing import List
from dotenv import load_dotenv
from openai import OpenAI
from anthropic import Anthropic

OPENAI_MODELS = {"gpt-4o"}
ANTHROPIC_MODELS = {"claude-3-5-sonnet-20240620"}


def chat(messages, model):

    if model in OPENAI_MODELS:
        return _openai_chat(messages, model)
    elif model in ANTHROPIC_MODELS:
        return _anthropic_chat(messages, model)
    else:
        raise ValueError(f"Model {model} not supported")


def _openai_chat(messages: List[dict[str, str]], model: str):
    load_dotenv()

    openai_client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

    response = openai_client.chat.completions.create(model=model, messages=messages)

    return response.choices[0].message.content.strip()


def _anthropic_chat(
    messages: List[dict[str, str]], model: str, max_tokens: int | None = None
):
    load_dotenv()

    anthropic_client = Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

    if not max_tokens:
        max_tokens = 1024

    for message in messages:
        if message["role"] not in ["user", "assistant"]:
            raise ValueError("Role must be user or assistant")

    response = anthropic_client.messages.create(
        model=model, messages=messages, max_tokens=max_tokens
    )

    return response.content[0].text
