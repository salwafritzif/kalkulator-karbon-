import streamlit as st

# Konfigurasi Halaman Web
st.set_page_config(
    page_title="Kalkulator Jejak Karbon", page_icon="🌱", layout="centered"
)

# Judul dan Deskripsi
st.title("🌱 Kalkulator Jejak Karbon Pribadi")
st.write(
    "Hitung estimasi emisi karbon ($\text{CO}_2$) harian atau bulanan Anda dan temukan cara untuk menguranginya!"
)

st.markdown("---")

# Bagian Input Pengguna
st.subheader("📝 Masukkan Aktivitas Anda (Per Bulan)")

# 1. Transportasi
st.markdown("### 1. Transportasi")
km_motor = st.number_input(
    "Jarak tempuh dengan Motor (km per bulan):", min_value=0.0, value=100.0
)
km_mobil = st.number_input(
    "Jarak tempuh dengan Mobil (km per bulan):", min_value=0.0, value=0.0
)
jam_umum = st.number_input(
    "Waktu naik Transportasi Umum (jam per bulan):", min_value=0.0, value=10.0
)

# 2. Konsumsi Energi Rumah Tangga
st.markdown("### 2. Energi Rumah Tangga")
kwh_listrik = st.number_input(
    "Konsumsi Listrik (kWh per bulan):", min_value=0.0, value=150.0
)

# 3. Konsumsi Makanan & Sampah (Estimasi Sederhana)
st.markdown("### 3. Pola Konsumsi & Sampah")
pilihan_makanan = st.selectbox(
    "Pola konsumsi makanan utama Anda:",
    [
        "Banyak Daging (Sapi/Kambing)",
        "Seimbang (Daging Ayam/Ikan & Sayur)",
        "Vegetarian / Berbasis Nabati",
    ],
)

st.markdown("---")

# Tombol Hitung
if st.button("Hitung Jejak Karbon Saya 🚀", type="primary"):
  # --- FAKTOR EMISI (Standar Estimasi) ---
  # Motor: ~0.10 kg CO2 per km
  # Mobil: ~0.19 kg CO2 per km
  # Transportasi Umum: ~0.05 kg CO2 per jam
  # Listrik PLN Indonesia: ~0.85 kg CO2 per kWh (rata-rata grid)
  # Makanan: Daging tinggi (~300 kg/bln), Seimbang (~150 kg/bln), Nabati (~80 kg/bln)

  emisi_motor = km_motor * 0.10
  emisi_mobil = km_mobil * 0.19
  emisi_umum = jam_umum * 0.05
  emisi_listrik = kwh_listrik * 0.85

  if pilihan_makanan == "Banyak Daging (Sapi/Kambing)":
    emisi_makanan = 300.0
  elif pilihan_makanan == "Seimbang (Daging Ayam/Ikan & Sayur)":
    emisi_makanan = 150.0
  else:
    emisi_makanan = 80.0

  # Total Emisi dalam kg CO2
  total_emisi_kg = (
      emisi_motor
      + emisi_mobil
      + emisi_umum
      + emisi_listrik
      + emisi_makanan )
  total_emisi_ ton = total_emisi_kg / 1000 
  # --- MENAMPILKAN HASIL ---
  st.subheader("📊 Hasil Perhitungan Anda")

  col1, col2 = st.columns(2)
  with col1:
    st.metric(
        label="Total Emisi per Bulan", value=f"{total_emisi_kg:.2f} kg CO₂"
    )
  with col2:
    st.metric(
        label="Total Emisi per Tahun",
        value=f"{(total_emisi_ton * 12):.2f} ton CO₂",
    )

  # Visualisasi Breakdown menggunakan Bar Chart sederhana
  st.write("### Rincian Sumber Emisi (kg CO₂)")
  data_chart = {
      "Kategori": [
          "Motor",
          "Mobil",
          "Trans. Umum",
          "Listrik",
          "Makanan & Lainnya",
      ],
      "Emisi (kg)": [
          emisi_motor,
          emisi_mobil,
          emisi_umum,
          emisi_listrik,
          emisi_makanan,
      ],
  }
  st.bar_chart(data_chart, x="Kategori", y="Emisi (kg)")

  # --- REKOMENDASI / TIPS ---
  st.subheader("💡 Tips Mengurangi Jejak Karbon")
  if total_emisi_kg > 300:
    st.warning(
        "Jejak karbon Anda tergolong **Tinggi**. Coba kurangi penggunaan kendaraan"
        " pribadi, beralih ke transportasi umum, atau hemat penggunaan listrik"
        " rumah."
    )
  elif total_emisi_kg > 150:
    st.info(
        "Jejak karbon Anda tergolong **Sedang**. Pertahankan gaya hidup ramah"
        " lingkungan dan tingkatkan efisiensi energi."
    )
  else:
    st.success(
        "Luar biasa! Jejak karbon Anda tergolong **Rendah**. Tetap jaga pola"
        " hidup berkelanjutan ini!"
    )
