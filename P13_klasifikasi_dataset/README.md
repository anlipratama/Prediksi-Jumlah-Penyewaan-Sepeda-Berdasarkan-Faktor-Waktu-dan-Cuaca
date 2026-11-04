# Klasifikasi Binary, Multi-class, dan Multi-label

Tugas Machine Learning (Klasifikasi). Repositori ini berisi satu notebook, `klasifikasi_dataset_v2.ipynb`, yang:

1. menjelaskan perbedaan tiga jenis klasifikasi: **binary**, **multi-class**, dan **multi-label**;
2. memuat **9 dataset** (3 untuk tiap jenis) beserta narasi deskripsi dan keterangan asal dataset;
3. **mengidentifikasi jenis klasifikasi** tiap dataset secara otomatis memakai **pandas**.

## Isi Repositori

| Berkas | Keterangan |
|---|---|
| `klasifikasi_dataset.ipynb` | Notebook utama (narasi, kode, dan tabel ringkasan) |
| `README.md` | Dokumen ini |

## Dataset yang Digunakan

| Jenis | Dataset | Asal dataset | Cara dimuat |
|---|---|---|---|
| Binary | Pima Indians Diabetes | NIDDK (UCI/Kaggle) | CSV dari GitHub `jbrownlee/Datasets` |
| Binary | Banknote Authentication | UCI (id=267) | CSV dari GitHub `jbrownlee/Datasets` |
| Binary | Sonar (Mines vs. Rocks) | UCI (id=151) | CSV dari GitHub `jbrownlee/Datasets` |
| Multi-class | Digits | UCI (id=80) | `sklearn.datasets.load_digits` |
| Multi-class | Wheat Seeds | UCI (id=236) | CSV dari GitHub `jbrownlee/Datasets` |
| Multi-class | Glass Identification | UCI (id=42) | CSV dari GitHub `jbrownlee/Datasets` |
| Multi-label | Flags | UCI (id=40) | CSV di Hugging Face `imodels/multitask-tabular-datasets` |
| Multi-label | Foodtruck | Rivolli dkk. (2017) | CSV di Hugging Face `imodels/multitask-tabular-datasets` |
| Multi-label | Water Quality | Blockeel dkk. (1999) | CSV di Hugging Face `imodels/multitask-tabular-datasets` |

Dataset multi-label berasal dari *Multi-Label Classification Dataset Repository* (Universidad de Córdoba): https://www.uco.es/kdis/mllresources

Tautan UCI memakai pola `https://archive.ics.uci.edu/dataset/<id>`, misalnya https://archive.ics.uci.edu/dataset/267.

## Cara Menjalankan

1. Pastikan Python 3 terpasang, lalu pasang pustaka yang dibutuhkan:

   ```bash
   pip install pandas numpy scikit-learn jupyter
   ```

2. Buka notebook dengan Jupyter (atau unggah ke Google Colab), lalu pilih **Run all**.
3. Komputer harus terhubung ke internet, karena semua dataset diunduh saat notebook dijalankan (kecuali Digits, yang sudah ada di scikit-learn).

Jika satu dataset gagal dimuat, notebook menampilkan pesan error untuk dataset itu saja dan tetap melanjutkan ke dataset berikutnya.

## Penjelasan Kode

### 1. Tiga jenis klasifikasi

- **Binary:** target hanya punya dua kelas, dan tiap data masuk ke salah satunya.
- **Multi-class:** target punya lebih dari dua kelas, tetapi tiap data tetap hanya punya satu kelas.
- **Multi-label:** tiap data boleh punya beberapa label sekaligus, sehingga targetnya berupa beberapa kolom 0/1.

Pembahasan ketiga jenis ini, termasuk pelatihan *binary classifier*, *multiclass classification*, dan *multilabel classification*, ada pada bab "Classification" di Géron (2025).

### 2. Fungsi `deteksi_jenis(y)`

Fungsi ini menentukan jenis klasifikasi dari DataFrame target `y` hanya dengan pandas:

- Jika target satu kolom dan `nunique() == 2`, hasilnya **binary**.
- Jika target satu kolom dan `nunique() > 2`, hasilnya **multi-class**.
- Jika target beberapa kolom 0/1 dan ada baris dengan `sum(axis=1) > 1`, hasilnya **multi-label**.

Metode `nunique()`, `sum()`, dan `value_counts()` adalah bagian dari DataFrame dan Series pandas. Dasar penggunaan pandas (Series, DataFrame, dan statistik ringkas) dibahas di McKinney (2022), Bab 5.

### 3. Fungsi pemuat data

- `muat_github(...)` membaca CSV tanpa header dari GitHub dengan `pd.read_csv(..., header=None, names=...)`, lalu memisahkan kolom fitur dan kolom target. Pembacaan berkas CSV dibahas di McKinney (2022), Bab 6.
- `muat_digits()` memakai `load_digits` dari scikit-learn.
- `muat_hf(nama)` membaca CSV multi-label. Semua kolom berakhiran `__target` dianggap sebagai label, lalu diubah menjadi bilangan bulat 0/1.

### 4. Fungsi `analisis(...)`

Untuk tiap dataset, fungsi ini mencetak:

- ukuran fitur (baris x kolom) dan jumlah nilai kosong (`isnull().sum()`, lihat McKinney (2022), Bab 7 tentang data hilang);
- jenis klasifikasi hasil deteksi;
- distribusi kelas (`value_counts()`) dan rasio kelas terbesar terhadap terkecil untuk melihat ketidakseimbangan kelas;
- untuk multi-label: rata-rata dan maksimum label aktif per data, serta jumlah data tiap label.

Hasilnya dikumpulkan ke daftar `RINGKASAN` dan ditampilkan sebagai tabel di bagian akhir notebook. Kolom **Terdeteksi** harus sama dengan kolom **Seharusnya**.

## Referensi

- Géron, A. (2025). *Hands-On Machine Learning with Scikit-Learn and PyTorch*. O'Reilly Media. ISBN 979-8-3416-0797-2. Bab 3, "Classification".
- McKinney, W. (2022). *Python for Data Analysis: Data Wrangling with pandas, NumPy, and Jupyter* (edisi ke-3). O'Reilly Media. ISBN 978-1-0981-0403-0.
- Dua, D. dan Graff, C. (2019). *UCI Machine Learning Repository*. University of California, Irvine. https://archive.ics.uci.edu
- Universidad de Córdoba. *Multi-Label Classification Dataset Repository*. https://www.uco.es/kdis/mllresources
