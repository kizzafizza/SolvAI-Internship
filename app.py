import streamlit as st
import pandas as pd

from src.feedback_engine import generate_feedback
from src.evaluator import evaluate_feedback
from src.profile_engine import generate_profile_comment
from src.profile_evaluator import evaluate_profile_comment
from src.combined_engine import generate_combined_report


st.set_page_config(
    page_title="SolvAI AI Feedback System",
    layout="wide"
)

st.title("SolvAI AI Feedback System")

st.write(
    "Run academic feedback, student profile comments, and final combined student reports."
)

tab1, tab2, tab3 = st.tabs([
    "Academic Feedback",
    "Student Profile",
    "Combined Report"
])


# -------------------------------
# TAB 1: Academic Feedback
# -------------------------------

with tab1:
    st.header("Academic Feedback Pipeline")

    academic_file = st.file_uploader(
        "Upload academic test CSV",
        type=["csv"],
        key="academic_file"
    )

    st.info(
        "Required columns: question, expected_answer, student_answer"
    )

    if academic_file is not None:
        academic_df = pd.read_csv(academic_file)
        st.dataframe(academic_df)

        if st.button("Run Academic Pipeline"):
            results = []

            for _, row in academic_df.iterrows():
                student_id = row["student_id"]
                student_name = row["student_name"]
                question = row["question"]
                expected_answer = row["expected_answer"]
                student_answer = row["student_answer"]

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

                results.append({
                    "Student ID": student_id,
                    "Student Name": student_name,
                    "Question": question,
                    "Expected Answer": expected_answer,
                    "Student Answer": student_answer,
                    "AI Feedback": feedback,
                    "Student Correctness": evaluation["student_answer_correctness"],
                    "Feedback Accuracy": evaluation["feedback_accuracy"],
                    "Feedback Relevance": evaluation["feedback_relevance"],
                    "Feedback Clarity": evaluation["feedback_clarity"],
                    "Feedback Helpfulness": evaluation["feedback_helpfulness"],
                    "Summary": evaluation["summary"]
                })

            results_df = pd.DataFrame(results)
            st.success("Academic pipeline completed.")
            st.dataframe(results_df)

            csv = results_df.to_csv(index=False).encode("utf-8")
            st.download_button(
                "Download Academic Results",
                csv,
                "academic_results.csv",
                "text/csv"
            )


# -------------------------------
# TAB 2: Student Profile
# -------------------------------

with tab2:
    st.header("Student Profile Pipeline")

    profile_file = st.file_uploader(
        "Upload student profile CSV",
        type=["csv"],
        key="profile_file"
    )

    st.info(
        "Required columns: student_profile, expected_focus"
    )

    if profile_file is not None:
        profile_df = pd.read_csv(profile_file)
        st.dataframe(profile_df)

        if st.button("Run Profile Pipeline"):
            results = []

            for _, row in profile_df.iterrows():
                student_id = row["student_id"]
                student_name = row["student_name"]
                student_profile = row["student_profile"]
                expected_focus = row["expected_focus"]

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

                results.append({
                    "Student ID": student_id,
                    "Student Name": student_name,
                    "Student Profile": student_profile,
                    "Expected Focus": expected_focus,
                    "Generated Comment": generated_comment,
                    "Profile Alignment": evaluation["profile_alignment"],
                    "Tone Professionalism": evaluation["tone_professionalism"],
                    "Specificity": evaluation["specificity"],
                    "Constructiveness": evaluation["constructiveness"],
                    "Sensitivity": evaluation["sensitivity"],
                    "Summary": evaluation["summary"]
                })

            results_df = pd.DataFrame(results)
            st.success("Profile pipeline completed.")
            st.dataframe(results_df)

            csv = results_df.to_csv(index=False).encode("utf-8")
            st.download_button(
                "Download Profile Results",
                csv,
                "profile_results.csv",
                "text/csv"
            )


# -------------------------------
# TAB 3: Combined Report
# -------------------------------

with tab3:
    st.header("Combined Student Report Pipeline")

    combined_file = st.file_uploader(
        "Upload combined report CSV",
        type=["csv"],
        key="combined_file"
    )

    st.info(
        "Required columns: student_profile, academic_result, academic_feedback"
    )

    if combined_file is not None:
        combined_df = pd.read_csv(combined_file)
        st.dataframe(combined_df)

        if st.button("Run Combined Report Pipeline"):
            results = []

            for _, row in combined_df.iterrows():
                student_id = row["student_id"]
                student_name = row["student_name"]
                student_profile = row["student_profile"]
                academic_result = row["academic_result"]
                academic_feedback = row["academic_feedback"]

                final_report = generate_combined_report(
                    student_name,
                    student_profile,
                    academic_result,
                    academic_feedback
                )

                results.append({
                    "Student ID": student_id,
                    "Student Name": student_name,
                    "Student Profile": student_profile,
                    "Academic Result": academic_result,
                    "Academic Feedback": academic_feedback,
                    "Final Combined Report": final_report
                })

            results_df = pd.DataFrame(results)
            st.success("Combined report pipeline completed.")
            st.dataframe(results_df)

            csv = results_df.to_csv(index=False).encode("utf-8")
            st.download_button(
                "Download Combined Results",
                csv,
                "combined_results.csv",
                "text/csv"
            )