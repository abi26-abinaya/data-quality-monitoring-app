import streamlit as st
from quality_engine import run_quality_checks
from report_generator import generate_report
import matplotlib.pyplot as plt
import seaborn as sns
import os

st.title("📊 Data Quality Monitoring System")

uploaded_file = st.file_uploader("Upload CSV File", type=["csv"])

if uploaded_file:

    # Save uploaded file temporarily
    with open("data.csv", "wb") as f:
        f.write(uploaded_file.getbuffer())

    # Run quality checks
    df, missing, duplicates, invalid_age, score = run_quality_checks("data.csv")

    # 🔎 Missing Values
    st.subheader("🔎 Missing Values")
    st.write(missing)

    # 📈 Visualization
    st.subheader("📈 Missing Values Visualization")
    fig, ax = plt.subplots()
    missing.plot(kind='bar', ax=ax)
    st.pyplot(fig)

    # 🔁 Duplicates
    st.subheader("🔁 Duplicate Count")
    st.write(duplicates)

    # ⚠️ Invalid Age
    st.subheader("⚠️ Invalid Age Records")
    st.write(invalid_age)

    # ⭐ Quality Score
    st.subheader("⭐ Data Quality Score")
    st.success(f"{score:.2f}%")

    # Generate PDF
    if not os.path.exists("reports"):
        os.makedirs("reports")

    generate_report(missing, duplicates, score)

    # Download cleaned CSV
    st.download_button(
        "⬇ Download Cleaned Data",
        df.to_csv(index=False),
        file_name="cleaned.csv",
        mime="text/csv"
    )

    st.success("✅ Report Generated Successfully!")