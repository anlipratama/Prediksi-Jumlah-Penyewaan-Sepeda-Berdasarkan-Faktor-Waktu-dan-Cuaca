# Tugas Machine Learning
# Bike Rental Prediction 🚲

**Prediksi Jumlah Penyewaan Sepeda Menggunakan Machine Learning**

## 📌 Deskripsi Proyek

Proyek ini bertujuan untuk memprediksi jumlah penyewaan sepeda berdasarkan faktor waktu dan kondisi cuaca menggunakan Machine Learning.

Dataset yang digunakan adalah **Bike Sharing Dataset** dari UCI Machine Learning Repository. Data berisi informasi penyewaan sepeda per jam beserta faktor-faktor yang berkaitan dengan aktivitas penyewaan.

Proyek ini dibuat sebagai sarana pembelajaran untuk memahami tahapan pengolahan data, analisis eksploratif, pemodelan regresi, evaluasi model, dan pengembangan aplikasi web sederhana.

## 🎯 Tujuan

- Memahami proses pengolahan data menggunakan Python.
- Melakukan Exploratory Data Analysis (EDA) dan eksplorasi lanjutan.
- Membangun model untuk memprediksi jumlah penyewaan sepeda.
- Membandingkan performa dua algoritma regresi.
- Mengevaluasi model menggunakan MAE, RMSE, dan R².
- Mengembangkan model menjadi aplikasi web menggunakan Streamlit.

## 📊 Dataset

**Nama:** Bike Sharing Dataset  
**Sumber:** [UCI Machine Learning Repository](https://archive.ics.uci.edu/dataset/275/bike+sharing+dataset)  
**File yang digunakan:** `hour.csv`  
**Jumlah data:** 17.379 baris pada versi file yang umum digunakan.

Dataset berisi informasi penyewaan sepeda berdasarkan waktu, musim, dan kondisi cuaca.

### Fitur yang digunakan

| Kolom | Keterangan |
|---|---|
| `season` | Musim |
| `yr` | Tahun pengamatan |
| `mnth` | Bulan |
| `hr` | Jam penyewaan |
| `holiday` | Status hari libur |
| `weekday` | Hari dalam minggu |
| `workingday` | Status hari kerja |
| `weathersit` | Kondisi cuaca |
| `temp` | Suhu yang dinormalisasi |
| `atemp` | Suhu terasa yang dinormalisasi |
| `hum` | Kelembapan yang dinormalisasi |
| `windspeed` | Kecepatan angin yang dinormalisasi |
| `cnt` | Jumlah total penyewaan sepeda |

**Target prediksi:** `cnt`

Kolom `casual` dan `registered` tidak digunakan sebagai fitur karena keduanya merupakan komponen pembentuk jumlah total penyewaan.

## 🛠️ Teknologi yang Digunakan

- Python
- Pandas
- NumPy
- Matplotlib
- Scikit-learn
- Joblib
- Streamlit
- Google Colab / Visual Studio Code

## 🔄 Tahapan Pengerjaan

### 1. Data Loading
Mengunduh dan membaca dataset menggunakan Pandas.

### 2. Data Cleaning
Memeriksa tipe data, nilai kosong, dan data duplikat.

### 3. Exploratory Data Analysis (EDA)
Menganalisis statistik dasar, distribusi penyewaan, dan pola penyewaan berdasarkan jam.

### 4. Exploratory Data Analysis Lanjutan (ExDA)
Mengeksplorasi hubungan antara kondisi cuaca, fitur numerik, dan jumlah penyewaan.

### 5. Data Preprocessing
Memilih fitur yang digunakan sebagai input dan menetapkan `cnt` sebagai target.

### 6. Data Splitting
Membagi data menjadi 80% data latih dan 20% data uji berdasarkan urutan waktu.

### 7. Modeling
Membangun dan membandingkan dua algoritma regresi:

- **Linear Regression:** mempelajari hubungan linear antara fitur dan target.
- **Random Forest Regressor:** menggabungkan banyak pohon keputusan untuk menghasilkan prediksi.

### 8. Evaluation
Menggunakan tiga metrik evaluasi:

- **MAE (Mean Absolute Error):** mengukur rata-rata kesalahan absolut prediksi.
- **RMSE (Root Mean Squared Error):** mengukur kesalahan dengan penalti lebih besar untuk kesalahan besar.
- **R² Score:** mengukur kemampuan model menjelaskan variasi target pada data uji.

Model terbaik dipilih berdasarkan hasil evaluasi, dengan MAE sebagai kriteria utama pada implementasi awal.

### 9. Development
Mengembangkan model yang telah dilatih menjadi aplikasi web sederhana menggunakan Streamlit.

Pengguna dapat memasukkan informasi waktu dan cuaca untuk mendapatkan perkiraan jumlah penyewaan sepeda.

## 📁 Struktur Proyek

```text
bike-rental-prediction/
├── app.py
├── model_bike.pkl
├── fitur_bike.pkl
├── README.md
└── requirements.txt
```

Keterangan:

- `app.py`: kode aplikasi Streamlit.
- `model_bike.pkl`: model Machine Learning yang telah dilatih.
- `fitur_bike.pkl`: daftar fitur yang digunakan model.
- `README.md`: dokumentasi proyek.
- `requirements.txt`: daftar pustaka yang diperlukan.

## ⚙️ Instalasi dan Menjalankan Aplikasi

### 1. Clone repository

```bash
git clone https://github.com/anlipratama/bike-rental-prediction.git
cd bike-rental-prediction
```


### 2. Instal dependensi

```bash
pip install -r requirements.txt
```

Jika file `requirements.txt` belum tersedia, gunakan:

```bash
pip install streamlit pandas numpy matplotlib scikit-learn joblib
```

### 3. Jalankan aplikasi

Pastikan `app.py`, `model_bike.pkl`, dan `fitur_bike.pkl` berada di folder yang sama.

```bash
streamlit run app.py
```

Aplikasi akan terbuka melalui browser dan siap digunakan untuk mencoba prediksi.

## 📈 Hasil dan Evaluasi

Evaluasi model dilakukan menggunakan MAE, RMSE, dan R² untuk membandingkan hasil prediksi dengan data aktual.

Hasil numerik evaluasi akan dicantumkan setelah proses pemodelan dijalankan.

| Algoritma | MAE | RMSE | R² |
|---|---:|---:|---:|
| Linear Regression | Isi sesuai hasil | Isi sesuai hasil | Isi sesuai hasil |
| Random Forest Regressor | Isi sesuai hasil | Isi sesuai hasil | Isi sesuai hasil |

Model terbaik ditentukan berdasarkan hasil pengujian dan perbandingan metrik evaluasi.

## 🚀 Pengembangan Selanjutnya

Beberapa pengembangan yang dapat dilakukan:

- Menambahkan visualisasi hasil prediksi ke dalam aplikasi.
- Memperbaiki tampilan input agar lebih mudah dipahami.
- Melakukan optimasi hyperparameter.
- Memperbaiki encoding fitur kategori.
- Membandingkan hasil model dengan metode regresi lainnya.
- Melakukan deployment aplikasi agar dapat diakses secara online.

## ⚠️ Catatan

Hasil prediksi merupakan perkiraan berdasarkan pola pada data historis, bukan jumlah penyewaan aktual yang dijamin akan terjadi.

Proyek ini dibuat untuk tujuan pembelajaran dan pengembangan portofolio Machine Learning.

## 📚 Referensi

Fanaee-T, H. (2013). *Bike Sharing [Dataset].* UCI Machine Learning Repository.

https://doi.org/10.24432/C5W894

Lisensi dataset: Creative Commons Attribution 4.0 International (CC BY 4.0).

## 👨‍💻 Author

Dibuat sebagai proyek pembelajaran Machine Learning menggunakan Python.
