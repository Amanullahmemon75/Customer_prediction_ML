import streamlit as st
import joblib
import numpy as np

# Load the saved models
models = {
    "Neural Network (MLP) - Accuracy: 87.88%": 'tuned_mlp_model.joblib',
    "Gradient Boosting - Accuracy: 90.38%": 'tuned_gradient_boosting_model.joblib',
    "Decision Tree - Accuracy: 88.50%": 'tuned_decision_tree_model.joblib'
}

# Define a function for prediction
def predict(input_data, model_file):
    # Load the selected model
    model = joblib.load(model_file)
    # Ensure the input data is in the correct format for the model
    input_data = np.array(input_data).reshape(1, -1)
    prediction = model.predict(input_data)
    # Return "True" for 0 (converted) and "False" for 1 (not converted)
    return "True" if prediction[0] == 0 else "False"

# Streamlit app structure
st.title("Customer Conversion Prediction App")

# Select the model
model_choice = st.selectbox("Choose a model", list(models.keys()))
model_file = models[model_choice]

# Collect user input with suitable alignment
st.subheader("Customer Information")
age = st.slider("Age", min_value=0, max_value=100, value=30)
income = st.number_input("Income", min_value=0.0, value=50000.0)
previous_purchases = st.number_input("Previous Purchases", min_value=0.0, value=10.0)
loyalty_points = st.number_input("Loyalty Points", min_value=0.0, value=100.0)

st.subheader("Campaign Engagement")
total_page_views = st.number_input("Total Page Views", min_value=0.0, value=5.0)
time_on_site = st.slider("Time on Site (minutes)", min_value=0.0, max_value=100.0, value=15.0)
click_through_rate = st.slider("Click Through Rate (%)", min_value=0.0, max_value=100.0, value=10.0)
ad_spend = st.number_input("Ad Spend", min_value=0.0, value=1000.0)
conversion_rate = st.slider("Conversion Rate (%)", min_value=0.0, max_value=100.0, value=5.0)
social_shares = st.number_input("Social Shares", min_value=0.0, value=2.0)
email_activity = st.slider("Email Activity (Opens)", min_value=0.0, max_value=50.0, value=10.0)

# Arrange the input data according to the model's expected features
input_data = [
    total_page_views, time_on_site, click_through_rate, ad_spend, conversion_rate,
    loyalty_points, email_activity, income, previous_purchases, social_shares, age
]

# When the user clicks the predict button
if st.button("Predict"):
    prediction = predict(input_data, model_file)
    st.write(f"Customer Conversion Prediction: {prediction}")


