import streamlit as st
import joblib
import numpy as np

# Load the saved models
models = {
    "Neural Network (MLP) - Accuracy: 87.88%": 'tuned_mlp_model.joblib',
    "Gradient Boosting - Accuracy: 90.38%": 'tuned_gradient_boosting_model.joblib',
    "Decision Tree - Accuracy: 88.50%": 'tuned_decision_tree_model.joblib'
}

# Custom CSS for styling
st.markdown("""
    <style>
        .main {
            background-color: #f5f5f5;
            padding: 20px;
            border-radius: 10px;
        }
        .title {
            color: #4CAF50;
            font-size: 40px;
            font-weight: bold;
        }
        .subheader {
            font-size: 20px;
            font-weight: bold;
        }
    </style>
""", unsafe_allow_html=True)

# Title and app structure
st.markdown("<div class='title'>Customer Conversion Prediction App</div>", unsafe_allow_html=True)

# Select the model
model_choice = st.selectbox("Choose a model", list(models.keys()))
model_file = models[model_choice]

# Define a function for prediction
def predict(input_data, model_file):
    model = joblib.load(model_file)
    input_data = np.array(input_data).reshape(1, -1)
    prediction = model.predict(input_data)
    return "True" if prediction[0] == 0 else "False"

# Collect user inputs
st.markdown("<div class='subheader'>Customer Information</div>", unsafe_allow_html=True)
col1, col2, col3 = st.columns(3)

with col1:
    age = st.slider("Age", min_value=0, max_value=100, value=30)
    gender = st.selectbox("Gender", options=["Male", "Female", "Other"])
    income = st.number_input("Income", min_value=0.0, value=50000.0)
    
with col2:
    ad_spend = st.number_input("Ad Spend", min_value=0.0, value=1000.0)
    click_through_rate = st.slider("Click Through Rate (%)", min_value=0.0, max_value=100.0, value=10.0)
    conversion_rate = st.slider("Conversion Rate (%)", min_value=0.0, max_value=100.0, value=5.0)
    
with col3:
    time_on_site = st.slider("Time on Site (minutes)", min_value=0.0, max_value=100.0, value=15.0)
    social_shares = st.number_input("Social Shares", min_value=0.0, value=2.0)
    email_activity = st.slider("Email Activity (Opens)", min_value=0.0, max_value=50.0, value=10.0)

col4, col5 = st.columns(2)

with col4:
    previous_purchases = st.number_input("Previous Purchases", min_value=0.0, value=10.0)
    loyalty_points = st.number_input("Loyalty Points", min_value=0.0, value=100.0)

with col5:
    total_page_views = st.number_input("Total Page Views", min_value=0.0, value=5.0)

# Process gender input as a numeric value
gender_numeric = {"Male": 0, "Female": 1, "Other": 2}.get(gender, 0)

# Arrange input data
input_data = [
    age, gender_numeric, income, ad_spend, click_through_rate, 
    conversion_rate, time_on_site, social_shares, email_activity, 
    previous_purchases, loyalty_points, total_page_views
]

# Prediction
if st.button("Predict"):
    prediction = predict(input_data, model_file)
    st.markdown(f"<h3 style='color: #4CAF50;'>Customer Conversion Prediction: {prediction}</h3>", unsafe_allow_html=True)
