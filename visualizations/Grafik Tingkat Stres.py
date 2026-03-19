import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# 1. Menyiapkan data berdasarkan temuan dalam grafik
data = {
    'Pekerjaan': [
        'Student', 'Manager', 'Software Engineer', 'Doctor', 
        'Researcher', 'Freelancer', 'Teacher', 'Designer'
    ],
    'Rata-rata Tingkat Stres': [7.18, 7.06, 7.02, 6.97, 6.92, 6.90, 6.90, 6.87]
}

df = pd.DataFrame(data)

# 2. Mengatur gaya visualisasi
sns.set_theme(style="whitegrid")
plt.figure(figsize=(12, 6))

# 3. Membuat Horizontal Bar Plot
# Menggunakan palet 'viridis' untuk gradasi warna yang serupa dengan gambar
plot = sns.barplot(
    x='Rata-rata Tingkat Stres', 
    y='Pekerjaan', 
    data=df, 
    palette='viridis'
)

# 4. Kustomisasi Grafik
plt.title('Rata-rata Tingkat Stres Berdasarkan Pekerjaan', fontsize=14, pad=15)
plt.xlabel('Average Stress Level', fontsize=12)
plt.ylabel('', fontsize=12) # Menghapus label Y agar lebih bersih

# Mengatur rentang sumbu X agar perbedaan terlihat jelas (sesuai gambar: 6.0 - 7.5)
plt.xlim(6.0, 7.5)

# Menampilkan grid hanya pada sumbu X
plt.grid(axis='x', linestyle='--', alpha=0.7)

# 5. Menampilkan hasil
plt.tight_layout()
plt.show()
