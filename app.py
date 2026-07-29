import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression

# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="USA House Price Prediction",
    page_icon="🏠",
    layout="centered"
)

# -----------------------------
# App Title
# -----------------------------
st.title("🏠 USA House Price Prediction")

st.write(
    "Enter the house details below to predict the estimated house price."
)

# -----------------------------
# Load Dataset
# -----------------------------
df = pd.read_csv("USA_Housing.csv")

# -----------------------------
# Feature Engineering
# -----------------------------
df["rooms_per_bedroom"] = (
    df["Avg. Area Number of Rooms"]
    / df["Avg. Area Number of Bedrooms"]
)

# -----------------------------
# Select Features
# -----------------------------
X = df[
    [
        "Avg. Area Income",
        "Avg. Area House Age",
        "Avg. Area Number of Rooms",
        "Avg. Area Number of Bedrooms",
        "Area Population",
        "rooms_per_bedroom"
    ]
]

# Target variable
y = df["Price"]

# -----------------------------
# Train Linear Regression Model
# -----------------------------
model = LinearRegression()
model.fit(X, y)

# -----------------------------
# User Input Section
# -----------------------------
st.header("Enter House Details")

avg_area_income = st.number_input(
    "Average Area Income",
    min_value=0.0,
    value=70000.0
)

avg_area_house_age = st.number_input(
    "Average Area House Age",
    min_value=0.0,
    value=5.0
)

avg_area_number_of_rooms = st.number_input(
    "Average Area Number of Rooms",
    min_value=1.0,
    value=6.0
)

avg_area_number_of_bedrooms = st.number_input(
    "Average Area Number of Bedrooms",
    min_value=1.0,
    value=4.0
)

area_population = st.number_input(
    "Area Population",
    min_value=0.0,
    value=30000.0
)

# -----------------------------
# Calculate Rooms per Bedroom
# -----------------------------
rooms_per_bedroom = (
    avg_area_number_of_rooms
    / avg_area_number_of_bedrooms
)

# -----------------------------
# Prediction Button
# -----------------------------
if st.button("Predict House Price"):

    # Create input DataFrame
    input_data = pd.DataFrame({
        "Avg. Area Income": [avg_area_income],
        "Avg. Area House Age": [avg_area_house_age],
        "Avg. Area Number of Rooms": [avg_area_number_of_rooms],
        "Avg. Area Number of Bedrooms": [avg_area_number_of_bedrooms],
        "Area Population": [area_population],
        "rooms_per_bedroom": [rooms_per_bedroom]
    })

    # Make prediction
    prediction = model.predict(input_data)[0]

    # Display predicted price
    st.success(
        f"Estimated House Price: ${prediction:,.2f}"
    )

    # -----------------------------
    # Population Category
    # -----------------------------
    low_threshold = df["Area Population"].quantile(0.33)
    high_threshold = df["Area Population"].quantile(0.66)

    if area_population <= low_threshold:
        category = "Low"
    elif area_population <= high_threshold:
        category = "Medium"
    else:
        category = "High"

    # Display category
    st.info(
        f"Population Category: {category}"
    )
