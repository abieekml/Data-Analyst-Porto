import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Simulasi Data 
# Menggunakan 15.000 data seperti di proyek kamu
np.random.seed(42)
n_samples = 15000

# X: Penggunaan HP (0 - 120 menit)
x = np.random.uniform(0, 120, n_samples)

# Y: Kualitas Tidur (skala 1-10) dengan tren negatif terhadap X
# Rumus: baseline - (faktor_penurunan * x) + noise_acak
y = 8.5 - (0.035 * x) + np.random.normal(0, 1.2, n_samples)
y = np.clip(y, 1, 10) # Memastikan nilai tetap di rentang 1-10

# 2. Pengaturan Tema Visual (Whitegrid)
sns.set_theme(style="whitegrid")
fig, ax = plt.subplots(figsize=(10, 6))

# 3. Membuat Hexbin Plot
# 'gridsize=25' menghasilkan ukuran segi enam yang pas seperti di gambar
# 'cmap=YlGnBu' (Yellow-Green-Blue) adalah palet yang digunakan di gambar
# 'mincnt=1' memastikan area tanpa data tetap berwarna putih (tidak kuning pucat)
# 'edgecolors=None' atau 'face' agar antar segi enam terlihat menyatu rapi
hb = ax.hexbin(
    x, y, 
    gridsize=25, 
    cmap='YlGnBu', 
    mincnt=1, 
    edgecolors='face'
)

# 4. Menambahkan Colorbar (Legenda Hitungan/Count)
cb = fig.colorbar(hb, ax=ax)
cb.set_label('Count', fontsize=12)

# 5. Kustomisasi Judul dan Label Sumbu 
ax.set_title('Kepadatan Data: Penggunaan HP Sebelum Tidur vs Kualitas Tidur', 
             fontsize=14, pad=15, loc='left', color='#333333')
ax.set_xlabel('Phone Usage Before Sleep (Minutes)', fontsize=12)
ax.set_ylabel('Sleep Quality Score', fontsize=12)

# Mengatur batas tampilan sumbu  (0-125 dan 0.5-10.5)
ax.set_xlim(-5, 125)
ax.set_ylim(0.5, 10.5)

# 6. Menampilkan Grafik
plt.tight_layout()
plt.show()
