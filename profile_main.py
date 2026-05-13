import csv
from src.profile_engine import generate_profile_comment
from src.profile_evaluator import evaluate_profile_comment

INPUT_FILE = "data/raw/profile_test_data.csv"
OUTPUT_FILE = "profile_results.csv"

test_cases = []

with open(INPUT_FILE, mode="r", newline="", encoding="utf-8") as file:
    reader = csv.DictReader(file)

    for row in reader:
        test_cases.append({
            "student_profile": row["student_profile"],
            "expected_focus": row["expected_focus"]
        })

with open(OUTPUT_FILE, mode="w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)

    writer.writerow([
        "Student Name",
        "Student Profile",
        "Expected Focus",
        "Generated Comment",
        "Profile Alignment",
        "Tone Professionalism",
        "Specificity",
        "Constructiveness",
        "Sensitivity",
        "Summary"
    ])

    for case in test_cases:
        student_name = case["student_name"]
        student_profile = case["student_profile"]
        expected_focus = case["expected_focus"]

        # 'Test comment for hypothetical testing'
        # generated_comment = "The Student is good and doing well"

        generated_comment = generate_profile_comment(
            student_name,
            student_profile,
            expected_focus
        )

        evaluation = evaluate_profile_comment(
            student_profile,
            expected_focus,
            generated_comment
        )

        writer.writerow([
            student_name,
            student_profile,
            expected_focus,
            generated_comment,
            evaluation["profile_alignment"],
            evaluation["tone_professionalism"],
            evaluation["specificity"],
            evaluation["constructiveness"],
            evaluation["sensitivity"],
            evaluation["summary"]
        ])

        print("\n==============================")
        print("Student Profile:", student_profile)
        print("\nGenerated Comment:")
        print(generated_comment)
        print("\nEvaluation:")
        print(evaluation)
        print("\nSaved result.")