# 📊 Analisis Kualitas Tidur, Penggunaan Gadget, dan Tingkat Stres

[![Analysis-Status](https://img.shields.io/badge/Status-Completed-success.svg)](#)
[![Field](https://img.shields.io/badge/Field-Data%20Analysis-blue.svg)](#)
[![Tools](https://img.shields.io/badge/Tools-Python%20%7C%20Pandas%20%7C%20Seaborn-blue.svg)](#)

## 📝 Deskripsi Proyek
Proyek ini mengeksplorasi hubungan antara pola penggunaan perangkat seluler, kualitas tidur, dan tingkat stres individu. Proyek ini telah ditingkatkan dari analisis berbasis spreadsheet ke **automasi menggunakan Python** untuk mendemonstrasikan kemampuan teknis dalam pengolahan data besar (*big data*) dan visualisasi yang lebih mendalam.

Analisis dilakukan menggunakan dataset dari **Kaggle** yang mencakup **15.000 data observasi** dengan distribusi gender yang representatif: 7.234 laki-laki, 7.181 perempuan, dan 585 kategori lainnya.

---

## 🛠️ Keahlian & Alat yang Digunakan
Proyek ini mengacu pada standar kompetensi *data analyst* modern:

* **Python (Pandas & NumPy)**: Digunakan untuk manipulasi dataset besar secara efisien dan pembersihan data (*data cleaning*) otomatis.
* **Statistika**: Penerapan analisis korelasi Pearson untuk mengidentifikasi hubungan antar variabel kesehatan dan kebiasaan digital.
* **Seaborn & Matplotlib**: Pembuatan visualisasi data profesional seperti *heatmap* korelasi, *regplot*, dan *hexbin plot* untuk melihat kepadatan data.
* **Critical Thinking**: Menganalisis faktor penyebab kelelahan mental untuk menemukan solusi praktis terkait keseimbangan hidup (*work-life balance*).

---

## 🚀 Langkah-Langkah Analisis
1. **Identifikasi Pertanyaan**: Menentukan variabel penelitian seperti hubungan *screen time* vs kelelahan mental agar interpretasi data lebih tajam.
2. **Automated Data Cleaning**: Menggunakan skrip Python untuk memastikan integritas data dan menangani dataset 15.000 baris secara efisien.
3. **Exploratory Data Analysis (EDA)**: Meneliti korelasi antar variabel, termasuk dampak penggunaan ponsel sebelum tidur terhadap kualitas istirahat.
4. **Final Visualization**: Menyusun temuan utama dalam bentuk laporan visual sistematis menggunakan *library* Python.

---

## 💡 Temuan Utama (Insights)
* **Korelasi Screen Time**: Terdapat korelasi positif yang sangat kuat (**0,83**) antara durasi layar harian dengan skor kelelahan mental.
* **Kelompok Paling Rentan**: Mahasiswa (*Student*) memiliki rata-rata tingkat stres tertinggi (**7,18**) dibandingkan profesi lainnya.
* **Higiene Tidur**: Penggunaan ponsel sesaat sebelum tidur memiliki korelasi negatif (**-0,33**) yang secara signifikan menurunkan kualitas tidur.
* **Mitos Notifikasi**: Secara mengejutkan, jumlah notifikasi harian hampir tidak memiliki pengaruh terhadap tingkat stres (korelasi **-0,002**).
* **Konsumsi Kafein**: Kelompok *Freelancer* tercatat sebagai konsumen kafein tertinggi dengan rata-rata **2,05** cangkir per hari.

---

## 📁 Struktur Repositori
| Folder/File | Deskripsi |
| :--- | :--- |
| `data/` | Dataset "Sleep, Mobile, & Stress" dari Kaggle.com |
| `analysis.py` | Skrip Python untuk perhitungan statistik dan korelasi data |
| `visualization/grafik.py` | Skrip Python untuk menghasilkan grafik (PNG) secara otomatis |
| `requirements.txt` | Daftar *library* Python yang diperlukan (Pandas, Seaborn, dll) |
| `README.md` | Dokumentasi lengkap proyek |

---

## 👤 Informasi Penulis
* **Nama**: Abi Kamal
* **NIM**: 124090310100004
* **Instansi**: 4A Sistem Informasi, UIN Syarif Hidayatullah Jakarta
* **GitHub**: [abieekml](https://github.com/abieekml)

---
*Proyek ini dikelola secara mandiri untuk tujuan pengembangan portofolio data analis.*
