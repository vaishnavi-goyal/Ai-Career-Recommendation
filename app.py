import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="AI Career Recommendation",
    page_icon="🎯"
)

st.title("AI Career Recommendation System")

name = st.text_input("Enter Name")

skills = st.text_input(
    "Enter Skills (comma separated)"
)

interest = st.selectbox(
    "Select Interest",
    [
        "AI",
        "Data Science",
        "Web Development",
        "Software Development"
    ]
)

cgpa = st.slider(
    "Select CGPA",
    0.0,
    10.0,
    8.0
)

career = ""
learn = ""

if st.button("Recommend Career"):

    skills = skills.lower()

    if (
        "python" in skills
        and
        "sql" in skills
    ):

        career = "Data Analyst"

        learn = """
Power BI
Statistics
Advanced SQL
"""

    elif (
        "machine learning"
        in skills
    ):

        career = "Machine Learning Engineer"

        learn = """
Deep Learning
TensorFlow
Deployment
"""

    elif (
        "html" in skills
    ):

        career = "Web Developer"

        learn = """
React
API
Backend
"""

    elif (
        "java"
        in skills
    ):

        career = "Software Developer"

        learn = """
Spring Boot
DSA
System Design
"""

    else:

        career = "Python Developer"

        learn = """
Flask
SQL
Projects
"""

    st.success(
        f"Recommended Role: {career}"
    )

    st.subheader(
        "Skills To Learn"
    )

    st.write(
        learn
    )

    if cgpa >= 8:

        st.info(
            "Placement Probability: High"
        )

    else:

        st.warning(
            "Build More Projects"
        )
