import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# 1. Simulasi Data (Gunakan data asli kamu jika ada)
np.random.seed(42)
n_samples = 1000

# Menghasilkan durasi layar antara 1 hingga 10 jam
screen_time = np.random.uniform(1, 10, n_samples)

# Membuat korelasi positif (0.83) untuk skor kelelahan
# Rumus: y = ax + b + noise
fatigue_score = 0.85 * screen_time + np.random.normal(2.2, 1.5, n_samples)

# Memastikan skor tetap berada dalam rentang 1 hingga 10
fatigue_score = np.clip(fatigue_score, 1, 10)

# Masukkan ke dalam DataFrame
df = pd.DataFrame({
    'Daily Screen Time (Hours)': screen_time,
    'Mental Fatigue Score': fatigue_score
})

# 2. Mengatur Gaya Visualisasi
sns.set_theme(style="whitegrid")
plt.figure(figsize=(10, 6))

# 3. Membuat Scatter Plot dengan Garis Regresi
# 'scatter_kws' untuk mengatur tampilan titik (transparansi dan warna)
# 'line_kws' untuk mengatur tampilan garis regresi (warna dan ketebalan)
sns.regplot(
    data=df, 
    x='Daily Screen Time (Hours)', 
    y='Mental Fatigue Score',
    scatter_kws={'alpha': 0.4, 'color': '#45ADA8'}, # Warna teal transparan
    line_kws={'color': 'red', 'linewidth': 3}       # Garis merah tebal
)

# 4. Kustomisasi Judul dan Label
plt.title('Korelasi Screen Time vs Kelelahan Mental (Sample 1000 data)', fontsize=14)
plt.xlabel('Daily Screen Time (Hours)', fontsize=12)
plt.ylabel('Mental Fatigue Score', fontsize=12)

# 5. Menampilkan Hasil
plt.tight_layout()
plt.show()
