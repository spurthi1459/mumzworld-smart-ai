import sys
import os

# Fix import path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from backend.pipeline import get_response
from evals.test_cases import test_cases


def evaluate():
    total = len(test_cases)
    total_score = 0

    print("\nRunning Evaluations...\n")

    for i, test in enumerate(test_cases, 1):
        query = test["query"]
        expected = test["expected_keywords"]

        result = get_response(query=query)
        products = result["products"]

        # Collect tags
        product_tags = " ".join([
            " ".join(p.get("tags", []))
            for p in products
        ]).lower()

        # 🔥 score calculation (instead of strict pass/fail)
        matched = sum(1 for keyword in expected if keyword in product_tags)

        if len(expected) == 0:
            score = 1.0
        else:
            score = matched / len(expected)

        total_score += score

        # 🔥 classification (clean output)
        if score == 1.0:
            status = "PASS"
        elif score >= 0.5:
            status = "PARTIAL"
        else:
            status = "LOW"

        print(f"Test {i}: {query}")
        print(f"Expected: {expected}")
        print(f"Found tags: {product_tags}")
        print(f"Match Score: {score:.2f}")
        print(f"Result: {status}\n")

    avg_score = total_score / total

    print("-----------")
    print(f"Average Score: {avg_score:.2f}")
    print("-----------")


if __name__ == "__main__":
    evaluate()