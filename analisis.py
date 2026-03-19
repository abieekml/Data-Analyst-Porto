import pandas as pd
import numpy as np

# Load dataset
file_name = 'sleep_mobile_stress_dataset_15000.csv'

try:
    df = pd.read_csv(file_name)
    print(f"--- ANALISIS DATA: {file_name} ---")
    print(f"Total Observasi: {len(df)} data [cite: 7]")
except FileNotFoundError:
    print(f"Error: File {file_name} tidak ditemukan.")
    exit()

# 1. Distribusi Gender [cite: 12]
gender_dist = df['gender'].value_counts()
print("\n[1] DISTRIBUSI GENDER")
print(gender_dist)

# 2. Analisis Korelasi Utama [cite: 13, 94, 98, 99]
# Hubungan Screen Time vs Kelelahan Mental
corr_screen_fatigue = df['daily_screen_time_hours'].corr(df['mental_fatigue_score'])
# Hubungan Penggunaan HP sebelum tidur vs Kualitas Tidur
corr_phone_sleep = df['phone_usage_before_sleep_minutes'].corr(df['sleep_quality_score'])
# Hubungan Notifikasi vs Stres
corr_notif_stress = df['notifications_received_per_day'].corr(df['stress_level'])

print("\n[2] ANALISIS KORELASI")
print(f"- Korelasi Screen Time & Kelelahan Mental: {corr_screen_fatigue:.2f} (Target: 0.83)")
print(f"- Korelasi Penggunaan HP & Kualitas Tidur: {corr_phone_sleep:.2f} (Target: -0.33)")
print(f"- Korelasi Notifikasi & Tingkat Stres: {corr_notif_stress:.4f} (Target: -0.002)")

# 3. Analisis Tingkat Stres Berdasarkan Pekerjaan [cite: 13, 97]
stress_by_job = df.groupby('occupation')['stress_level'].mean().sort_values(ascending=False)
print("\n[3] RATA-RATA TINGKAT STRES PER PEKERJAAN")
print(stress_by_job)

# 4. Analisis Aktivitas Fisik (>60 menit) vs Durasi Tidur [cite: 13, 100]
active_sleep = df[df['physical_activity_minutes'] > 60]['sleep_duration_hours'].mean()
inactive_sleep = df[df['physical_activity_minutes'] <= 60]['sleep_duration_hours'].mean()
print("\n[4] PENGARUH AKTIVITAS FISIK TERHADAP DURASI TIDUR")
print(f"- Rata-rata Tidur (Aktif >60m): {active_sleep:.2f} jam")
print(f"- Rata-rata Tidur (Tidak Aktif): {inactive_sleep:.2f} jam")

# 5. Konsumsi Kafein Berdasarkan Pekerjaan [cite: 13, 101]
caffeine_by_job = df.groupby('occupation')['caffeine_intake_cups'].mean().sort_values(ascending=False)
print("\n[5] RATA-RATA KONSUMSI KAFEIN PER PEKERJAAN")
print(caffeine_by_job)

# 6. Rata-rata Usia Kelelahan Mental Ekstrem (Skor > 8) [cite: 13]
extreme_fatigue_avg_age = df[df['mental_fatigue_score'] > 8]['age'].mean()
print("\n[6] PROFIL KELELAHAN MENTAL EKSTREM")
print(f"- Rata-rata Usia (Skor > 8): {extreme_fatigue_avg_age:.1f} tahun")
