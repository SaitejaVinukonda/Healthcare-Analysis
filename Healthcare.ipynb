import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from datetime import datetime, timedelta

# Generate synthetic healthcare dataset
np.random.seed(123)
num_records = 1000

data = pd.DataFrame({
    'Age': np.random.randint(18, 90, num_records),
    'Gender': np.random.choice(['Male', 'Female'], num_records, p=[0.5, 0.5]),
    'Medical_Condition': np.random.choice(
        ['Diabetes', 'Hypertension', 'Asthma', 'Heart Disease', 'Arthritis', 'Cancer', 'Depression'],
        num_records
    ),
    'Billing_Amount': np.round(np.random.uniform(100, 5000, num_records), 2),
    'Date_of_Admission': [datetime(2022, 1, 1) + timedelta(days=np.random.randint(0, 730)) for _ in range(num_records)],
})
data['Discharge_Date'] = data['Date_of_Admission'] + pd.to_timedelta(np.random.randint(1, 11, num_records), unit='D')

# Streamlit UI
st.title("Healthcare Data Analysis Dashboard")

# Sidebar filters
gender_filter = st.selectbox("Select Gender:", ['All'] + list(data['Gender'].unique()))
age_range = st.slider("Select Age Range:", int(data['Age'].min()), int(data['Age'].max()), (int(data['Age'].min()), int(data['Age'].max())))
date_range = st.date_input("Select Date Range:", [data['Date_of_Admission'].min(), data['Discharge_Date'].max()])
condition_filter = st.selectbox("Select Medical Condition:", ['All'] + list(data['Medical_Condition'].unique()))

# Filter data
filtered_data = data.copy()
if gender_filter != 'All':
    filtered_data = filtered_data[filtered_data['Gender'] == gender_filter]
filtered_data = filtered_data[(filtered_data['Age'] >= age_range[0]) & (filtered_data['Age'] <= age_range[1])]
filtered_data = filtered_data[(filtered_data['Date_of_Admission'] >= pd.to_datetime(date_range[0])) &
                              (filtered_data['Discharge_Date'] <= pd.to_datetime(date_range[1]))]
if condition_filter != 'All':
    filtered_data = filtered_data[filtered_data['Medical_Condition'] == condition_filter]

# Plots
st.subheader("Age Distribution")
st.plotly_chart(px.histogram(filtered_data, x='Age', nbins=20, title='Age Distribution'))

st.subheader("Gender Distribution")
gender_counts = filtered_data['Gender'].value_counts().reset_index()
# Rename the 'index' column to 'Gender' and the 'Gender' column to 'Count'
gender_counts.columns = ['Gender', 'Count']  
st.plotly_chart(px.bar(gender_counts, x='Gender', y='Count', title='Gender Distribution'))

st.subheader("Top Medical Conditions")
condition_counts = filtered_data['Medical_Condition'].value_counts().reset_index()
# Rename the 'index' column to 'Medical_Condition' and the 'Medical_Condition' column to 'Count'
condition_counts.columns = ['Medical_Condition', 'Count']
st.plotly_chart(px.bar(condition_counts, x='Medical_Condition', y='Count', title='Top Medical Conditions'))

st.subheader("Billing Amount by Condition")
st.plotly_chart(px.box(filtered_data, x='Medical_Condition', y='Billing_Amount', title='Billing Amount by Condition'))

st.subheader("Age vs Billing Amount")
st.plotly_chart(px.scatter(filtered_data, x='Age', y='Billing_Amount', title='Age vs Billing Amount'))

# Download filtered data
st.subheader("Download Filtered Data")
st.download_button("Download CSV", data=filtered_data.to_csv(index=False), file_name="filtered_data.csv", mime="text/csv")
