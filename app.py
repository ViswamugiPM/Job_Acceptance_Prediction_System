import streamlit as st
import pandas as pd
import joblib


import streamlit as st
st.write("Streamlit app is running ✅")

# Load model
import os
MODEL_PATH = os.path.join("models", "job_acceptance_model.pkl")
model = joblib.load(MODEL_PATH)

st.set_page_config(page_title="Job Acceptance Prediction", layout="centered")

st.title("💼 Job Acceptance Prediction System")
st.markdown("Predict whether a candidate will accept a job offer")

st.header("📋 Candidate Details")

# Input fields
age = st.number_input("Age", 18, 60, 25)
gender = st.selectbox("Gender", ["Male", "Female"])

ssc = st.slider("SSC Percentage", 0.0, 100.0, 65.0)
hsc = st.slider("HSC Percentage", 0.0, 100.0, 70.0)
degree = st.slider("Degree Percentage", 0.0, 100.0, 75.0)

degree_spec = st.selectbox(
    "Degree Specialization",
    ["Computer Science", "Information Technology", "Electronics", "Mechanical", "Civil"]
)

technical = st.slider("Technical Score", 0.0, 100.0, 70.0)
aptitude = st.slider("Aptitude Score", 0.0, 100.0, 65.0)
communication = st.slider("Communication Score", 0.0, 100.0, 60.0)

skills_match = st.slider("Skills Match Percentage", 0.0, 100.0, 75.0)

certifications = st.number_input("Certifications Count", 0, 10, 1)
internship = st.selectbox("Internship Experience", ["Yes", "No"])
years_exp = st.number_input("Years of Experience", 0, 40, 2)

career_switch = st.selectbox("Career Switch Willingness", ["Yes", "No"])
relevant_exp = st.selectbox("Relevant Experience", ["Yes", "No"])

prev_ctc = st.number_input("Previous CTC (LPA)", 0.0, 50.0, 3.0)
exp_ctc = st.number_input("Expected CTC (LPA)", 0.0, 50.0, 6.0)

company_tier = st.selectbox("Company Tier", ["Tier 1", "Tier 2", "Tier 3"])
job_role_match = st.selectbox("Job Role Match", ["Matched", "Not Matched"])
competition = st.selectbox("Competition Level", ["Low", "Medium", "High"])
bond = st.selectbox("Bond Requirement", ["Required", "Not Required"])

notice = st.number_input("Notice Period (Days)", 0, 180, 30)
layoff = st.selectbox("Layoff History", ["Yes", "No"])
gap = st.number_input("Employment Gap (Months)", 0.0, 60.0, 0.0)

relocation = st.selectbox("Relocation Willingness", ["Willing", "Not Willing"])

# ---------- Feature Engineering Functions ----------

def experience_category(years):
    if years == 0:
        return "Fresher"
    elif years <= 3:
        return "Junior"
    else:
        return "Senior"

def academic_band(score):
    if score < 60:
        return "Low"
    elif score < 75:
        return "Medium"
    else:
        return "High"

def skills_level(skill):
    if skill < 60:
        return "Low"
    elif skill < 80:
        return "Medium"
    else:
        return "High"

# Predict button
if st.button("🔮 Predict Job Acceptance"):
    try:
        input_df = pd.DataFrame([{
            "age_years": age,
            "gender": gender,
            "ssc_percentage": ssc,
            "hsc_percentage": hsc,
            "degree_percentage": degree,
            "degree_specialization": degree_spec,
            "technical_score": technical,
            "aptitude_score": aptitude,
            "communication_score": communication,
            "skills_match_percentage": skills_match,
            "certifications_count": certifications,
            "internship_experience": internship,
            "years_of_experience": years_exp,
            "career_switch_willingness": career_switch,
            "relevant_experience": relevant_exp,
            "previous_ctc_lpa": prev_ctc,
            "expected_ctc_lpa": exp_ctc,
            "company_tier": company_tier,
            "job_role_match": job_role_match,
            "competition_level": competition,
            "bond_requirement": bond,
            "notice_period_days": notice,
            "layoff_history": layoff,
            "employment_gap_months": gap,
            "relocation_willingness": relocation,

            # 🔽 FEATURE ENGINEERING 🔽
            "experience_category": experience_category(years_exp),
            "degree_performance_band": academic_band(degree),
            "skills_match_level": skills_level(skills_match),
            "interview_avg_score": (technical + aptitude + communication) / 3,
            "interview_performance": academic_band(
                (technical + aptitude + communication) / 3
            ),
            "ctc_gap": exp_ctc - prev_ctc,
            "employment_gap_flag": 1 if gap > 6 else 0
        }])

        prediction = model.predict(input_df)[0]

        if prediction == 1:
            st.success("✅ Candidate is likely to ACCEPT the job offer")
        else:
            st.error("❌ Candidate is likely to REJECT the job offer")

    except Exception as e:
        st.error(f"Prediction error: {e}")
