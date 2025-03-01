import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load Data
df = pd.read_csv("patient_data.csv")

# Streamlit App
st.set_page_config(page_title="Health Monitoring Dashboard", layout="wide")
st.title("🏥 Health Monitoring System")

# Sidebar Filters
st.sidebar.header("Filter Data")
age_filter = st.sidebar.slider("Select Age Range", min_value=18, max_value=90, value=(18, 90))
gender_filter = st.sidebar.multiselect("Select Gender", ["Male", "Female"], default=["Male", "Female"])

df_filtered = df[(df["Age"] >= age_filter[0]) & (df["Age"] <= age_filter[1]) & df["Gender"].isin(gender_filter)]

# Layout
tabs = st.tabs(["Overview", "BP Analysis", "Sugar Analysis", "Cholesterol Analysis", "Haemoglobin Analysis"])

# Overview Tab
with tabs[0]:
    st.subheader("📊 Patient Data Overview")
    st.dataframe(df_filtered, height=300)
    st.subheader("📈 Age Distribution")
    fig, ax = plt.subplots()
    sns.histplot(df_filtered["Age"], bins=30, kde=True, ax=ax)
    st.pyplot(fig)

# BP Analysis Tab
with tabs[1]:
    st.subheader("🩸 Blood Pressure Analysis")
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Systolic BP Distribution")
        fig, ax = plt.subplots()
        sns.histplot(df_filtered["BP_Systolic"], bins=30, kde=True, ax=ax)
        st.pyplot(fig)
    with col2:
        st.subheader("Diastolic BP Distribution")
        fig, ax = plt.subplots()
        sns.histplot(df_filtered["BP_Diastolic"], bins=30, kde=True, ax=ax)
        st.pyplot(fig)
    
    st.subheader("BP Levels by Age")
    fig, ax = plt.subplots()
    sns.scatterplot(x=df_filtered["Age"], y=df_filtered["BP_Systolic"], label="Systolic", alpha=0.6)
    sns.scatterplot(x=df_filtered["Age"], y=df_filtered["BP_Diastolic"], label="Diastolic", alpha=0.6)
    ax.set_xlabel("Age")
    ax.set_ylabel("Blood Pressure")
    st.pyplot(fig)

# Sugar Analysis Tab
with tabs[2]:
    st.subheader("🍬 Sugar Level Analysis")
    fig, ax = plt.subplots()
    sns.histplot(df_filtered["Sugar_Level"], bins=30, kde=True, ax=ax)
    st.pyplot(fig)
    
    st.subheader("Sugar Levels by Age")
    fig, ax = plt.subplots()
    sns.scatterplot(x=df_filtered["Age"], y=df_filtered["Sugar_Level"], alpha=0.6)
    ax.set_xlabel("Age")
    ax.set_ylabel("Sugar Level")
    st.pyplot(fig)

# Cholesterol Analysis Tab
with tabs[3]:
    st.subheader("🥩 Cholesterol Level Analysis")
    fig, ax = plt.subplots()
    sns.histplot(df_filtered["Cholesterol"], bins=30, kde=True, ax=ax)
    st.pyplot(fig)
    
    st.subheader("Cholesterol Levels by Age")
    fig, ax = plt.subplots()
    sns.scatterplot(x=df_filtered["Age"], y=df_filtered["Cholesterol"], alpha=0.6)
    ax.set_xlabel("Age")
    ax.set_ylabel("Cholesterol Level")
    st.pyplot(fig)

# Haemoglobin Analysis Tab
with tabs[4]:
    st.subheader("🩸 Haemoglobin Level Analysis")
    fig, ax = plt.subplots()
    sns.histplot(df_filtered["Haemoglobin"], bins=30, kde=True, ax=ax)
    st.pyplot(fig)
    
    st.subheader("Haemoglobin Levels by Age")
    fig, ax = plt.subplots()
    sns.scatterplot(x=df_filtered["Age"], y=df_filtered["Haemoglobin"], alpha=0.6)
    ax.set_xlabel("Age")
    ax.set_ylabel("Haemoglobin Level")
    st.pyplot(fig)

st.sidebar.markdown("---")
st.sidebar.markdown("👨‍⚕️ Developed for Health Monitoring System")