# Import libraries
import streamlit as st
import numpy as np
import pickle

# Load the saved model
model_path = "insurance_model.pkl"
with open(model_path, 'rb') as file:
    model = pickle.load(file)

# Define the app title
st.title("Prediksi Biaya Asuransi")
st.write("Author: Wiliy Wijaya | NIM: 2021230046")

# Input form
st.sidebar.header("Masukkan Informasi Berikut:")

age = st.sidebar.number_input("Usia (Tahun)", min_value=18, max_value=64, value=30)
sex = st.sidebar.selectbox("Jenis Kelamin", options=["Perempuan", "Laki-laki"], index=1)
bmi = st.sidebar.number_input("BMI (Body Mass Index)", min_value=15.0, max_value=50.0, value=25.0)
children = st.sidebar.number_input("Jumlah Anak", min_value=0, max_value=5, value=0)
smoker = st.sidebar.selectbox("Perokok", options=["Tidak", "Ya"], index=0)

# Convert categorical inputs
sex = 1 if sex == "Laki-laki" else 0
smoker = 1 if smoker == "Ya" else 0

# Prediction button
if st.sidebar.button("Prediksi"):
    # Prepare input for prediction
    input_data = np.array([[age, sex, bmi, children, smoker]])
    prediction = model.predict(input_data)

    # Display result
    st.write("### Hasil Prediksi")
    st.write(f"Biaya Asuransi yang Diperkirakan: Rp {prediction[0]:,.2f}")


