import streamlit as st
import pandas as pd
import joblib

# Memuat model
model = joblib.load("house_price_app_model.pkl")

# Judul aplikasi
st.title("🏠 House Price Prediction")

st.write(
    "Aplikasi sederhana untuk memprediksi harga rumah "
    "menggunakan Machine Learning."
)

# Input pengguna
overall_qual = st.slider(
    "Kualitas Rumah",
    min_value=1,
    max_value=10,
    value=5
)

gr_liv_area = st.number_input(
    "Luas Rumah (GrLivArea)",
    min_value=100,
    value=1500
)

year_built = st.number_input(
    "Tahun Dibangun",
    min_value=1800,
    max_value=2026,
    value=2000
)

garage_cars = st.number_input(
    "Kapasitas Garasi",
    min_value=0,
    max_value=5,
    value=2
)

total_bsmt_sf = st.number_input(
    "Luas Basement",
    min_value=0,
    value=800
)

# Tombol prediksi
if st.button("Prediksi Harga"):

    # Membuat data input
    input_data = pd.DataFrame({
        "OverallQual": [overall_qual],
        "GrLivArea": [gr_liv_area],
        "YearBuilt": [year_built],
        "GarageCars": [garage_cars],
        "TotalBsmtSF": [total_bsmt_sf]
    })

    # Melakukan prediksi
    prediction = model.predict(input_data)

    # Menampilkan hasil
    st.success(
        f"Prediksi Harga Rumah: ${prediction[0]:,.2f}"
    )