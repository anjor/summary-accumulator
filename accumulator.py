import os
from openai import OpenAI
from dotenv import load_dotenv


def accumulate_summary(
    summary: str, new_message: str, openai_client: OpenAI, model: str
):
    # Check for new relevant content
    prompt_check = f'Summarize the following message and determine if it contains new, relevant content that impacts the summary. If no new content is found return "no new relevant content": {new_message}\nCurrent Summary: {summary}'

    response = openai_client.chat.completions.create(
        model=model, messages=[{"role": "system", "content": prompt_check}]
    )

    new_relevant_content = response.choices[0].message.content.strip()

    if "no new relevant content" in new_relevant_content.lower():
        print(new_relevant_content)
        return summary
    else:
        # Generate updated summary
        prompt_update = f"Update the following summary based on the new message: {new_message}\nCurrent Summary: {summary}"
        response = openai_client.chat.completions.create(
            model=model, messages=[{"role": "system", "content": prompt_update}]
        )

        return response.choices[0].message.content


def main():
    load_dotenv()

    openai_client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

    summary = "The user wants a todo list application written in python."
    new_message = (
        "Scratch that. I would actually prefer to code scrabble, and let's use go."
    )

    print(accumulate_summary(summary, new_message, openai_client, "gpt-4o"))


if __name__ == "__main__":
    main()
