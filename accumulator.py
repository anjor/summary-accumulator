import os
from dotenv import load_dotenv
from models import chat


def accumulate_summary(summary: str, new_message: str, model: str):
    # Check for new relevant content
    prompt_check = f'Summarize the following message and determine if it contains new, relevant content that impacts the summary. If no new content is found return "no new relevant content": {new_message}\nCurrent Summary: {summary}'

    new_relevant_content = chat(
        model=model, messages=[{"role": "user", "content": prompt_check}]
    )

    if "no new relevant content" in new_relevant_content.lower():
        print(new_relevant_content)
        return summary
    else:
        # Generate updated summary
        prompt_update = f"Update the following summary based on the new message: {new_message}\nCurrent Summary: {summary}"

        return chat(model=model, messages=[{"role": "user", "content": prompt_update}])


def main():
    load_dotenv()

    summary = "The user wants a todo list application written in python."
    new_message = (
        "Scratch that. I would actually prefer to code scrabble, and let's use go."
    )

    for i in range(3):
        print("OpenAI: " + accumulate_summary(summary, new_message, "gpt-4o"))
        print(
            "Anthropic: "
            + accumulate_summary(summary, new_message, "claude-3-5-sonnet-20240620")
        )

        print("==========")


if __name__ == "__main__":
    main()
