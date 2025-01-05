import streamlit as st
import pandas as pd
import joblib
from sklearn.preprocessing import StandardScaler
from sklearn.feature_selection import SelectKBest, f_classif

# Load the trained model and preprocessing objects
scaler = joblib.load(r'C:\Users\ASUS\Dropbox\PC\Desktop\Resesrch file\UI\scaler.pkl')
selector = joblib.load(r'C:\Users\ASUS\Dropbox\PC\Desktop\Resesrch file\UI\selector.pkl')
le = joblib.load(r'C:\Users\ASUS\Dropbox\PC\Desktop\Resesrch file\UI\label_encoder.pkl')
selected_features = joblib.load(r'C:\Users\ASUS\Dropbox\PC\Desktop\Resesrch file\UI\selected_features.pkl')


# Streamlit UI for model prediction
st.title("Liver Cirrhosis Stage Prediction")
st.write("Enter the details to predict the stage of liver cirrhosis")

# Get feature names after selection
selected_features = joblib.load(r'C:\Users\ASUS\Dropbox\PC\Desktop\Resesrch file\UI\selected_features.pkl')

# User input fields
test_data = {}
for feature in selected_features:
    test_data[feature] = st.number_input(f"Enter {feature}", min_value=0.0, format="%.2f")

# Predict button
if st.button('Predict'):
    # Prepare input data as DataFrame
    input_df = pd.DataFrame([test_data])
    input_scaled = scaler.transform(input_df)
    input_selected = selector.transform(input_scaled)

    # Make prediction
    prediction = rf_model.predict(input_selected)

    # Decode and display result
    stage = le.inverse_transform(prediction)
    st.success(f"Predicted Stage: {stage[0]}")
