import streamlit as st
import requests

API_URL = "https://electricity-cost-api-m893.onrender.com/prediction" 

st.title("Electricity Cost Prediction Model")
st.markdown("Enter your details below:")

# Input fields
site_area = st.number_input("site area", min_value=1, max_value=5000, value=30)
structure_type = st.selectbox(
    "structure type",
    ['Mixed-use', 'Residential', 'Commercial', 'Industrial']
)
water_consumption = st.number_input("water consumption", min_value=1, max_value=10000, value=10)
recycling_rate = st.number_input("recycling rate", min_value=1,max_value=90, value=10)
utilisation_rate = st.number_input("utilisation rate",min_value=1, max_value=100, value=30 )
air_quality_index= st.number_input("air quality index",min_value=1, max_value=2000, value=30 )
issue_resolution_time = st.number_input("issue resolution time", min_value=1, max_value=72, value=30)
resident_count = st.number_input("resident count", min_value=1, max_value=489, value=30)



if st.button("Predict Electricity Cost"):
    input_data = {
        "site_area": site_area,
        "structure_type": structure_type,
        "water_consumption":water_consumption,
        "recycling_rate": recycling_rate,
        "utilisation_rate": utilisation_rate,
        "air_quality_index": air_quality_index,
        "issue_resolution_time": issue_resolution_time,
        "resident_count": resident_count,
        
    }

    try:
        response = requests.post(API_URL, json=input_data)
        result = response.json()

        if response.status_code == 200 :
            st.write(f"Predicted Electricity Cost: {result}")
            
            
        else:
            st.error(f"API Error: {response.status_code}")
            st.write(result)

    except requests.exceptions.ConnectionError:
        st.error("❌ Could not connect to the FastAPI server. Make sure it's running.")
