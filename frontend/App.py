import streamlit as st
import requests
from flask import Flask

def main():
    st.title("AQI Prediction App")
    
    # Input fields for user data
    features = {
        'PM2.5': st.number_input('PM2.5', value=0.0 , format = "%.2f"),
        'PM10': st.number_input('PM10', value=0.0, format = "%.2f"),
        # 'NO': st.number_input('NO', value=0),
        # 'NO2': st.number_input('NO2', value=0),
        # 'NOx': st.number_input('NOx', value=0),
        # 'NH3': st.number_input('NH3', value=0),
        # 'CO': st.number_input('CO', value=0),
        # 'SO2': st.number_input('SO2', value=0),
        # 'O3': st.number_input('O3', value=0),
        'Benzene': st.number_input('Benzene', value=0.0, format = "%.2f"),
        'Toluene': st.number_input('Toluene', value=0.0, format = "%.2f"),
        'Xylene': st.number_input('Xylene', value=0.0, format = "%.2f"),
        # 'AQI_Bucket': st.number_input('AQI_Bucket', value = 0)
        
    }

    # When the user clicks "Predict"
    if st.button('Predict AQI'):
        # Make an API call to Flask backend
        response = requests.post('http://127.0.0.1:5000/predict', json={'features': list(features.values())})
        
        if response.status_code == 200:
            prediction = response.json()['predicted_aqi']
            st.success(f"Predicted AQI: {prediction}")
        else:
            st.error("Error in prediction")

if __name__ == '__main__':
    main()






