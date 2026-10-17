
import streamlit as st
import pandas as pd
import joblib

# Memuat model dan daftar fitur
model = joblib.load("model_bike.pkl")
fitur = joblib.load("fitur_bike.pkl")

# Judul aplikasi
st.title("Bike Rental Prediction")
st.write(
    "Aplikasi untuk memperkirakan jumlah penyewaan sepeda."
)

# Form input pengguna
with st.form("form_prediksi"):
    season = st.selectbox("Musim", [1, 2, 3, 4])
    yr = st.selectbox("Tahun", [0, 1])
    mnth = st.selectbox("Bulan", list(range(1, 13)))
    hr = st.slider("Jam", 0, 23, 8)

    holiday = st.selectbox("Hari libur?", [0, 1])
    weekday = st.selectbox(
        "Hari dalam minggu", list(range(7))
    )
    workingday = st.selectbox("Hari kerja?", [0, 1])
    weathersit = st.selectbox(
        "Kondisi cuaca", [1, 2, 3, 4]
    )

    temp = st.slider(
        "Suhu (skala dataset)", 0.0, 1.0, 0.5
    )
    atemp = st.slider(
        "Suhu terasa (skala dataset)", 0.0, 1.0, 0.5
    )
    hum = st.slider(
        "Kelembapan (skala dataset)", 0.0, 1.0, 0.5
    )
    windspeed = st.slider(
        "Kecepatan angin (skala dataset)",
        0.0, 1.0, 0.2
    )

    submit = st.form_submit_button("Prediksi")

# Memproses prediksi setelah tombol ditekan
if submit:
    data = pd.DataFrame([{
        "season": season,
        "yr": yr,
        "mnth": mnth,
        "hr": hr,
        "holiday": holiday,
        "weekday": weekday,
        "workingday": workingday,
        "weathersit": weathersit,
        "temp": temp,
        "atemp": atemp,
        "hum": hum,
        "windspeed": windspeed
    }])[fitur]

    prediksi = model.predict(data)[0]

    st.success(
        f"Perkiraan penyewaan: "
        f"{max(0, round(prediksi))} sepeda"
    )

    st.caption(
        "Hasil merupakan perkiraan model, bukan jumlah aktual."
    )
