from eval import evaluate_accuracy
from models import chat

import jsonlines


def accumulate_summary(summary: str, new_message: str, model: str):
    # Check for new relevant content
    prompt_check = f'Summarize the following message and determine if it contains new, relevant content that impacts the summary. If no new content is found return "no new relevant content": {new_message}\nCurrent Summary: {summary}'

    new_relevant_content = chat(
        model=model, messages=[{"role": "user", "content": prompt_check}]
    )

    if "no new relevant content" in new_relevant_content.lower():
        return summary
    else:
        # Generate updated summary
        prompt_update = f"Update the following summary based on the new message: {new_message}\nCurrent Summary: {summary}"

        return chat(model=model, messages=[{"role": "user", "content": prompt_update}])


def main():
    num_experiments = 10
    score = 0
    for i in range(num_experiments):
        with jsonlines.open("sample_data.jsonl", "r") as jsonl_file:
            test_cases = [
                {
                    "expected_output": test["expected_output"],
                    "actual_output": accumulate_summary(
                        summary=test["initial_summary"],
                        new_message=test["new_message"],
                        model="gpt-4o",
                    ),
                }
                for test in jsonl_file
            ]
            score += evaluate_accuracy(test_cases=test_cases)

    print(f"{score/num_experiments}")


if __name__ == "__main__":
    main()
