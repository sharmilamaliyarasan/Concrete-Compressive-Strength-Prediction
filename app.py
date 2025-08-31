import streamlit as st
import numpy as np
import joblib

model = joblib.load("model.pkl")

st.title("Concrete Compressive Strength Prediction")

cement = st.number_input("Cement")
slag = st.number_input("Blast Furnace Slag")
flyash = st.number_input("Fly Ash ")
water = st.number_input("Water")
superplasticizer = st.number_input("Superplasticizer")
coarseagg = st.number_input("Coarse Aggregate")
fineagg = st.number_input("Fine Aggregate ")
age = st.number_input("Age")

final_input = np.array([[cement, slag, flyash, water, superplasticizer,
                         coarseagg, fineagg, age]])

if st.button("Predict"):
    prediction = model.predict(final_input)[0]
    st.success(f"Predicted Concrete Strength: {prediction:.2f}")
