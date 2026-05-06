import csv
from src.combined_engine import generate_combined_report

INPUT_FILE = "data/raw/combined_test_data.csv"
OUTPUT_FILE = "combined_results.csv"

with open(INPUT_FILE, mode="r", newline="", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    test_cases = list(reader)

with open(OUTPUT_FILE, mode="w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)

    writer.writerow([
        "Student Profile",
        "Academic Result",
        "Academic Feedback",
        "Final Combined Report"
    ])

    for case in test_cases:
        final_report = generate_combined_report(
            case["student_profile"],
            case["academic_result"],
            case["academic_feedback"]
        )

        writer.writerow([
            case["student_profile"],
            case["academic_result"],
            case["academic_feedback"],
            final_report
        ])

        print("\n==============================")
        print("Student Profile:", case["student_profile"])
        print("Academic Result:", case["academic_result"])
        print("Academic Feedback:", case["academic_feedback"])
        print("\nFinal Combined Report:")
        print(final_report)
        print("\nSaved result.")