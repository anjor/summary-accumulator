import torch
from transformers import BertTokenizer, BertModel

# Load pre-trained BERT model and tokenizer
tokenizer = BertTokenizer.from_pretrained("bert-base-uncased")
model = BertModel.from_pretrained("bert-base-uncased")


def evaluate_accuracy(test_cases):
    total_correct = 0
    for test_case in test_cases:
        expected_output_embedding = compute_embedding(
            test_case["expected_output"], model, tokenizer
        )
        actual_output_embedding = compute_embedding(
            test_case["actual_output"], model, tokenizer
        )

        # Ensure the tensors are on the same device
        expected_output_embedding = expected_output_embedding.to(
            actual_output_embedding.device
        )

        similarity = torch.nn.functional.cosine_similarity(
            expected_output_embedding.unsqueeze(0), actual_output_embedding.unsqueeze(0)
        )
        print(
            f"Similarity: {similarity.item()}, Expected output: {test_case['expected_output']}, Actual output: {test_case['actual_output']}"
        )
        if similarity.item() > 0.8:  # adjust this threshold value as needed
            total_correct += 1
    accuracy = total_correct / len(test_cases)
    return accuracy


def compute_embedding(text, model, tokenizer):
    inputs = tokenizer(
        text, return_tensors="pt", max_length=512, truncation=True, padding="max_length"
    )
    with torch.no_grad():
        outputs = model(**inputs)
    return outputs.pooler_output.squeeze()
