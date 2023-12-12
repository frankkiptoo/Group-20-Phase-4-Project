import streamlit as st
import pandas as pd
import pickle
# from statsmodels.tsa.arima.model import ARIMA

# Define the filename where the model is saved
model_filename = 'arima_model.pkl'

# Load the trained ARIMA model
with open(model_filename, 'rb') as model_file:
    loaded_model = pickle.load(model_file)

def predict_price(model, start_date, end_date):
    # Predict future prices using the ARIMA model
    forecast = model.predict(start=start_date, end=end_date)
    return forecast.iloc[0]

st.title('Real Estate Price Prediction')

# User input: Select the date using a date picker
date_input = st.date_input('Select the date for prediction:', min_value=pd.to_datetime('2023-01-01'))

if st.button('Predict Price'):
    try:
        # Format date for prediction
        formatted_date = date_input.strftime('%Y-%m-%d')
        prediction = predict_price(loaded_model, formatted_date, formatted_date)
        st.write(f'Predicted price for {formatted_date}: {prediction}')
    except Exception as e:
        st.error(f"Error: {str(e)}")

# To run the Streamlit app, use the command `streamlit run your_script.py` in your terminal.