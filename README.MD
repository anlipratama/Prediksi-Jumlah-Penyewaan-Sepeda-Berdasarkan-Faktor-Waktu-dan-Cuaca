# 🚲 Bike Rental Prediction

Project Machine Learning untuk memprediksi jumlah penyewaan sepeda berdasarkan waktu, kondisi cuaca, dan karakteristik lingkungan menggunakan algoritma regresi. Project ini dibuat menggunakan Python dan Streamlit sehingga model prediksi dapat digunakan melalui aplikasi web sederhana.

## 📌 Tentang Project

Penyewaan sepeda dapat dipengaruhi oleh beberapa faktor, seperti jam, musim, hari kerja, dan kondisi cuaca. Melalui project ini, dilakukan analisis data dan penerapan algoritma Machine Learning untuk memperkirakan jumlah penyewaan sepeda berdasarkan data historis.

Dua algoritma yang dibandingkan dalam project ini adalah **Linear Regression** dan **Random Forest Regressor**.

## 🎯 Tujuan

- Memahami proses pengolahan data untuk Machine Learning.
- Melakukan Exploratory Data Analysis (EDA) untuk melihat pola penyewaan sepeda.
- Membangun model regresi untuk memprediksi jumlah penyewaan sepeda.
- Membandingkan performa dua algoritma regresi.
- Membuat aplikasi prediksi sederhana menggunakan Streamlit.

## 📊 Dataset

Dataset yang digunakan adalah **Bike Sharing Dataset** dari UCI Machine Learning Repository.

- Sumber: [UCI Bike Sharing Dataset](https://archive.ics.uci.edu/dataset/275/bike+sharing+dataset)
- File yang digunakan: `hour.csv`
- Jumlah data: 17.379 baris pada versi dataset yang umum digunakan.
- Target prediksi: `cnt`, yaitu total jumlah penyewaan sepeda per jam.

Dataset ini mencakup informasi waktu, musim, hari kerja, kondisi cuaca, dan jumlah penyewaan sepeda.

## 🛠️ Teknologi yang Digunakan

- Python
- Pandas
- NumPy
- Matplotlib
- Scikit-learn
- Joblib
- Streamlit
- Jupyter Notebook / Google Colab
- Visual Studio Code

## ⚙️ Tahapan Pengerjaan

1. **Data Loading** — memuat dataset ke dalam DataFrame menggunakan Pandas.
2. **Data Cleaning** — memeriksa tipe data, nilai kosong, dan data duplikat.
3. **EDA (Exploratory Data Analysis)** — memahami distribusi jumlah penyewaan dan pola berdasarkan waktu.
4. **ExDA (Explorasi Data Lanjutan)** — melihat hubungan antara jumlah penyewaan dengan faktor cuaca dan variabel lainnya.
5. **Feature Selection** — menentukan fitur yang digunakan untuk memprediksi `cnt`.
6. **Data Splitting** — membagi data menjadi data latih dan data uji.
7. **Model Training** — melatih Linear Regression dan Random Forest Regressor.
8. **Model Evaluation** — membandingkan model menggunakan MAE, RMSE, dan R².
9. **Model Saving** — menyimpan model terpilih menggunakan Joblib.
10. **Deployment Sederhana** — membuat antarmuka prediksi menggunakan Streamlit.

## 📈 Hasil Evaluasi Model

Berikut hasil evaluasi kedua algoritma pada data pengujian:

| Algoritma | MAE | RMSE | R² |
|---|---:|---:|---:|
| Linear Regression | 138.3424 | 183.1024 | 0.3090 |
| Random Forest Regressor | 45.0257 | 70.2705 | 0.8982 |

### 🔍 Analisis Hasil

**Random Forest Regressor memberikan hasil terbaik** berdasarkan ketiga metrik evaluasi yang digunakan.

- **MAE sebesar 45,03:** rata-rata selisih absolut antara prediksi dan nilai aktual sekitar 45 penyewaan sepeda.
- **RMSE sebesar 70,27:** mengukur besar kesalahan prediksi dengan memberikan penalti lebih besar pada kesalahan yang tinggi.
- **R² sebesar 0,8982:** model menjelaskan sekitar 89,82% variasi target pada data pengujian.

Sebagai perbandingan, Linear Regression memperoleh R² sebesar 0,3090. Pada pengujian ini, Random Forest Regressor mampu menangkap pola data dengan lebih baik dibandingkan Linear Regression.

Hasil tersebut berlaku pada pembagian data dan konfigurasi model yang digunakan dalam project ini. Performa pada data lain dapat berbeda.

## 🖥️ Menjalankan Aplikasi

### 1. Clone Repository

```bash
git clone https://github.com/anlipratama/bike-rental-prediction.git
cd bike-rental-prediction
```

### 2. Instal Library

Pastikan Python sudah terinstal, lalu jalankan:

```bash
pip install -r requirements.txt
```

### 3. Jalankan Streamlit

```bash
streamlit run app.py
```

Setelah berjalan, buka alamat lokal yang ditampilkan di terminal, biasanya `http://localhost:8501`.

## 📁 Struktur Folder

```text
bike-rental-prediction/
├── app.py
├── model_bike.pkl
├── fitur_bike.pkl
├── requirements.txt
└── README.md
```

Keterangan:

- `app.py`: kode aplikasi Streamlit.
- `model_bike.pkl`: model Machine Learning yang telah disimpan.
- `fitur_bike.pkl`: daftar fitur yang digunakan model.
- `requirements.txt`: daftar library Python yang diperlukan.
- `README.md`: dokumentasi project.

## 📝 Kesimpulan

Berdasarkan hasil pengujian, Random Forest Regressor memiliki performa lebih baik daripada Linear Regression dalam memprediksi jumlah penyewaan sepeda pada dataset yang digunakan. Model Random Forest memperoleh MAE sebesar 45,0257, RMSE sebesar 70,2705, dan R² sebesar 0,8982.

Project ini menunjukkan tahapan penerapan Machine Learning, mulai dari pemuatan dan eksplorasi data hingga pelatihan, evaluasi, penyimpanan model, dan pembuatan aplikasi prediksi berbasis Streamlit.

## 📚 Referensi Dataset

Fanaee-T, H. (2013). *Bike Sharing Dataset*. UCI Machine Learning Repository.

https://doi.org/10.24432/C5W894

Dataset digunakan sesuai lisensi CC BY 4.0 dengan mencantumkan atribusi sumber.

## 👨‍💻 Author

Dikembangkan sebagai project pembelajaran Machine Learning menggunakan Python.
