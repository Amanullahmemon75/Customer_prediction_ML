import streamlit as st
import joblib
import numpy as np

# Load the saved models
models = {
    "✨ Neural Network (MLP) - Accuracy: 87.88%": 'tuned_mlp_model.joblib',
    "🚀 Gradient Boosting - Accuracy: 90.38%": 'tuned_gradient_boosting_model.joblib',
    "🌲 Decision Tree - Accuracy: 88.50%": 'tuned_decision_tree_model.joblib'
}

# Custom CSS for rich styling
st.markdown("""
    <style>
        /* Background styling */
        .main {
            background-color: black;
            color: white;  /* White text on black background */
            padding: 20px;
            font-family: 'Arial', sans-serif;
        }
        /* Title styling */
        .title {
            color: #fff;
            font-size: 3em;
            font-weight: bold;
            text-align: center;
            text-shadow: 2px 2px #ff7f50;
        }
        /* Subtitle styling */
        .subheader {
            font-size: 1.5em;
            font-weight: bold;
            color: #ff6347;
            text-align: center;
        }
        /* Input styling */
        .stSlider label, .stTextInput label, .stNumberInput label {
            color: #333;
            font-size: 1.1em;
            font-weight: 600;
        }
        /* Prediction button styling */
        .stButton button {
            background-color: #4CAF50;
            color: white;
            font-size: 1.2em;
            padding: 0.5em 1em;
            border-radius: 8px;
            transition: 0.3s;
        }
        .stButton button:hover {
            background-color: #45a049;
            box-shadow: 2px 2px 10px rgba(0, 0, 0, 0.2);
        }
    </style>
""", unsafe_allow_html=True)

# Title and app structure
st.markdown("<div class='title'>🔮 Customer Conversion Prediction App 🔮</div>", unsafe_allow_html=True)

# Select the model
st.subheader("💡 Choose Your Model")
model_choice = st.selectbox("Select the prediction model", list(models.keys()))
model_file = models[model_choice]

# Define a function for prediction
def predict(input_data, model_file):
    model = joblib.load(model_file)
    input_data = np.array(input_data).reshape(1, -1)
    prediction = model.predict(input_data)
    return "🌟Likely to Convert" if prediction[0] == 0 else "⚠️Not Likely to Convert"

# Collect user inputs with columns and grouping
st.markdown("<div class='subheader'>🧑‍💼 Customer Details</div>", unsafe_allow_html=True)

# Use separate layout for sliders and number inputs
st.markdown("### Select Customer Information")

# Collect sliders (age, click-through rate, etc.)
col1, col2, col3 = st.columns(3)

with col1:
    age = st.slider("Age", min_value=0, max_value=100, value=30)
    click_through_rate = st.slider("Click Through Rate (%)", min_value=0.0, max_value=100.0, value=10.0)
    conversion_rate = st.slider("Conversion Rate (%)", min_value=0.0, max_value=100.0, value=5.0)

with col2:
    time_on_site = st.slider("Time on Site (minutes)", min_value=0.0, max_value=100.0, value=15.0)
    email_activity = st.slider("Email Activity (Opens)", min_value=0, max_value=50, value=10)

with col3:
    ad_spend = st.number_input("Ad Spend ($)", min_value=0.0, value=1000.0, step=50.0)
    social_shares = st.number_input("Social Shares", min_value=0, value=2, step=1)

# Collect number inputs (income, previous purchases, etc.)
st.markdown("### Engagement Metrics")
col4, col5 = st.columns(2)

with col4:
    gender = st.selectbox("Gender", options=["Male", "Female", "Other"])
    income = st.number_input("Income ($)", min_value=0.0, value=50000.0, step=1000.0)
    previous_purchases = st.number_input("Previous Purchases", min_value=0, value=10, step=1)

with col5:
    loyalty_points = st.number_input("Loyalty Points", min_value=0, value=100, step=5)
    total_page_views = st.number_input("Total Page Views", min_value=0, value=5, step=1)

# Convert gender to numeric for model compatibility
gender_numeric = {"Male": 0, "Female": 1, "Other": 2}.get(gender, 0)

# Arrange input data
input_data = [
    age, gender_numeric, income, ad_spend, click_through_rate, 
    conversion_rate, time_on_site, social_shares, email_activity, 
    previous_purchases, loyalty_points, total_page_views
]

# Prediction
if st.button("🔍 Predict Conversion"):
    prediction = predict(input_data, model_file)
    st.markdown(f"<h3 style='color: #4CAF50; text-align: center;'>Result: {prediction}</h3>", unsafe_allow_html=True)
