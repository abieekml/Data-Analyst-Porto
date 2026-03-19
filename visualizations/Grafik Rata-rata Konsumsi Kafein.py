import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# 1. Persiapan Data (Berdasarkan estimasi angka di gambar)
data = {
    'Pekerjaan': [
        'Freelancer', 'Researcher', 'Doctor', 'Student', 
        'Manager', 'Designer', 'Software Engineer', 'Teacher'
    ],
    'Rata-rata Kafein': [2.05, 2.02, 2.02, 2.01, 2.01, 1.97, 1.96, 1.95]
}

df = pd.DataFrame(data)

# 2. Mengatur Tema Visual
sns.set_theme(style="whitegrid")
plt.figure(figsize=(12, 6))

# 3. Membuat Horizontal Bar Plot
# Palette 'magma' menghasilkan gradasi dari warna gelap (ungu tua) ke terang (oranye)
sns.barplot(
    x='Rata-rata Kafein', 
    y='Pekerjaan', 
    data=df, 
    palette='magma' 
)

# 4. Kustomisasi Judul dan Label Sumbu
plt.title('Rata-rata Konsumsi Kafein Berdasarkan Pekerjaan', fontsize=14, pad=15)
plt.xlabel('Average Caffeine Cups per Day', fontsize=12)
plt.ylabel('') # Menghapus label Y agar lebih rapi seperti di gambar

# Mengatur batas sumbu X agar batang tidak terlalu mepet ke kanan
plt.xlim(0, 2.15)

# 5. Menampilkan Hasil
plt.tight_layout()
plt.show()
