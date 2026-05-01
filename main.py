import csv
from src.feedback_engine import generate_feedback
from src.evaluator import evaluate_feedback

INPUT_FILE = "data/raw/test_data.csv"
OUTPUT_FILE = "results.csv"

# Read test data from CSV file
test_cases = []

with open(INPUT_FILE, mode="r", newline="", encoding="utf-8") as file:
    reader = csv.DictReader(file)

    for row in reader:
        test_cases.append({
            "question": row["question"],
            "expected_answer": row["expected_answer"],
            "student_answer": row["student_answer"]
        })

# Create results CSV file
with open(OUTPUT_FILE, mode="w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)

    # Write header row
    writer.writerow([
        "Question",
        "Expected Answer",
        "Student Answer",
        "AI Feedback",
        "Accuracy",
        "Relevance",
        "Clarity",
        "Helpfulness",
        "Summary"
    ])

    # Loop through each question/answer case
    for case in test_cases:
        question = case["question"]
        expected_answer = case["expected_answer"]
        student_answer = case["student_answer"]

        feedback = generate_feedback(
            question,
            expected_answer,
            student_answer
        )

        evaluation = evaluate_feedback(
            question,
            expected_answer,
            student_answer,
            feedback
        )

        # Write result row
        writer.writerow([
            question,
            expected_answer,
            student_answer,
            feedback,
            evaluation["student_answer_correctness"],
            evaluation["feedback_accuracy"],
            evaluation["feedback_relevance"],
            evaluation["feedback_clarity"],
            evaluation["feedback_helpfulness"]
        ])

        print("\n==============================")
        print("Question:", question)
        print("Expected Answer:", expected_answer)
        print("Student Answer:", student_answer)

        print("\nAI Feedback:")
        print(feedback)

        print("\nEvaluation:")
        print("Student Correctness:", evaluation["student_answer_correctness"])
        print("Feedback Accuracy:", evaluation["feedback_accuracy"])
        print("Feedback Relevance:", evaluation["feedback_relevance"])
        print("Feedback Clarity:", evaluation["feedback_clarity"])
        print("Feedback Helpfulness:", evaluation["feedback_helpfulness"])
        print("Summary:", evaluation["summary"])

        print("\nSaved result for:", student_answer)