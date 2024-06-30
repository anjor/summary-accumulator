import ollama
import math


def evaluate_accuracy(test_cases):
    total_correct = 0
    for test_case in test_cases:
        expected_output_embedding = compute_embedding(test_case["expected_output"])
        actual_output_embedding = compute_embedding(test_case["actual_output"])

        similarity = cosine_similarity(
            expected_output_embedding, actual_output_embedding
        )
        # print(
        #     f"Similarity: {similarity}, Expected output: {test_case['expected_output']}, Actual output: {test_case['actual_output']}"
        # )
        if similarity > 0.9:  # adjust this threshold value as needed
            total_correct += 1
    accuracy = total_correct / len(test_cases)
    return accuracy


def compute_embedding(text):
    response = ollama.embeddings(model="mxbai-embed-large", prompt=text)
    return response["embedding"]


def cosine_similarity(a, b):
    dot = sum(x * y for x, y in zip(a, b))
    norm_a = math.sqrt(sum(x**2 for x in a))
    norm_b = math.sqrt(sum(y**2 for y in b))

    return dot / (norm_a * norm_b)
