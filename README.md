# 📊 Analisis Kualitas Tidur, Penggunaan Gadget, dan Tingkat Stres

[![Analysis-Status](https://img.shields.io/badge/Status-Completed-success.svg)](#)
[![Field](https://img.shields.io/badge/Field-Data%20Analysis-blue.svg)](#)
[![Tools](https://img.shields.io/badge/Tools-Python%20%7C%20Pandas%20%7C%20Seaborn-blue.svg)](#)

## 📝 Deskripsi Proyek
Laporan ini mengeksplorasi hubungan antara pola penggunaan perangkat seluler, kualitas tidur, dan tingkat stres individu[cite: 6]. Proyek ini telah ditingkatkan dari analisis berbasis spreadsheet ke **automasi menggunakan Python** untuk mendemonstrasikan kemampuan teknis dalam pengolahan data besar (*big data*) dan visualisasi yang lebih mendalam.

Analisis dilakukan menggunakan dataset dari **Kaggle** yang mencakup **15.000 data observasi** dengan distribusi gender yang representatif: 7.234 laki-laki, 7.181 perempuan, dan 585 kategori lainnya[cite: 7, 12].

---

## 🛠️ Keahlian & Alat yang Digunakan
Proyek ini mengacu pada standar kompetensi *data analyst* modern:

* **Python (Pandas & NumPy)**: Digunakan untuk manipulasi dataset besar secara efisien dan pembersihan data (*data cleaning*) otomatis.
* [cite_start]**Statistika**: Penerapan analisis korelasi Pearson untuk mengidentifikasi hubungan antar variabel kesehatan dan kebiasaan digital[cite: 13, 14].
* [cite_start]**Seaborn & Matplotlib**: Pembuatan visualisasi data profesional seperti *heatmap* korelasi, *regplot*, dan *hexbin plot* untuk melihat kepadatan data[cite: 15].
* [cite_start]**Critical Thinking**: Menganalisis faktor penyebab kelelahan mental untuk menemukan solusi praktis terkait keseimbangan hidup (*work-life balance*)[cite: 8, 9].

---

## 🚀 Langkah-Langkah Analisis
1. **Identifikasi Pertanyaan**: Menentukan variabel penelitian seperti hubungan *screen time* vs kelelahan mental agar interpretasi data lebih tajam[cite: 106].
2. **Automated Data Cleaning**: Menggunakan skrip Python untuk memastikan integritas data dan menangani dataset 15.000 baris secara efisien[cite: 7].
3. **Exploratory Data Analysis (EDA)**: Meneliti korelasi antar variabel, termasuk dampak penggunaan ponsel sebelum tidur terhadap kualitas istirahat[cite: 13, 98].
4. **Final Visualization**: Menyusun temuan utama dalam bentuk laporan visual sistematis menggunakan *library* Python[cite: 15, 65].

---

## 💡 Temuan Utama (Insights)
**Korelasi Screen Time**: Terdapat korelasi positif yang sangat kuat (**0,83**) antara durasi layar harian dengan skor kelelahan mental[cite: 13, 94].
**Kelompok Paling Rentan**: Mahasiswa (*Student*) memiliki rata-rata tingkat stres tertinggi (**7,18**) dibandingkan profesi lainnya[cite: 13, 97].
**Higiene Tidur**: Penggunaan ponsel sesaat sebelum tidur memiliki korelasi negatif (**-0,33**) yang secara signifikan menurunkan kualitas tidur[cite: 13, 98].
**Mitos Notifikasi**: Secara mengejutkan, jumlah notifikasi harian hampir tidak memiliki pengaruh terhadap tingkat stres (korelasi **-0,002**)[cite: 14, 99].
**Konsumsi Kafein**: Kelompok *Freelancer* tercatat sebagai konsumen kafein tertinggi dengan rata-rata **2,05** cangkir per hari[cite: 14, 101].

---

## 📁 Struktur Repositori
| Folder/File | Deskripsi |
| :--- | :--- |
| `data/` | [cite_start]Dataset "Sleep, Mobile, & Stress" dari Kaggle.com [cite: 108] |
| `analysis.py` | Skrip Python untuk perhitungan statistik dan korelasi data |
| `visualization/grafik.py` | Skrip Python untuk menghasilkan grafik (PNG) secara otomatis |
| `requirements.txt` | Daftar *library* Python yang diperlukan (Pandas, Seaborn, dll) |
| `README.md` | Dokumentasi lengkap proyek |

---

## 👤 Informasi Penulis
**Nama**: Abi Kamal [cite: 1]
**NIM**: 124090310100004 [cite: 3]
**Instansi**: 4A Sistem Informasi, UIN Syarif Hidayatullah Jakarta [cite: 2]
* **Profil**: [GitHub abieekml](https://github.com/abieekml)

---
*Proyek ini dikelola secara mandiri untuk tujuan pengembangan portofolio data analis.*
