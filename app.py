import streamlit as st

st.title("🌱 Kalkulator Jejak Karbon")
st.write("Hitung estimasi emisi karbon bulanan Anda berdasarkan aktivitas sehari-hari.")

st.subheader("🚗 Transportasi")
km_motor = st.number_input("Kilometer perjalanan dengan motor per bulan:", min_value=0.0, value=0.0)
km_mobil = st.number_input("Kilometer perjalanan dengan mobil per bulan:", min_value=0.0, value=0.0)
transport_umum = st.number_input("Penggunaan transportasi umum (dalam Rupiah/bulan):", min_value=0.0, value=0.0)

st.subheader("⚡ Konsumsi Energi Rumah Tangga")
kwh_listrik = st.number_input("Penggunaan listrik (kWh per bulan):", min_value=0.0, value=0.0)

st.subheader("🍽️ Makanan & Pola Konsumsi")
pilihan_makanan = st.selectbox(
    "Pilih pola konsumsi makanan Anda:",
    ["Tinggi Daging", "Seimbang (Daging Ayam/Ikan & Sayur)", "Vegetarian/Vegan"]
)

emisi_motor = km_motor * 0.12
emisi_mobil = km_mobil * 0.20
emisi_umum = transport_umum * 0.0001
emisi_listrik = kwh_listrik * 0.85

if pilihan_makanan == "Tinggi Daging":
    emisi_makanan = 300.0
elif pilihan_makanan == "Seimbang (Daging Ayam/Ikan & Sayur)":
    emisi_makanan = 150.0
else:
    emisi_makanan = 80.0

total_emisi_kg = emisi_motor + emisi_mobil + emisi_umum + emisi_listrik + emisi_makanan
total_emisi_ton = total_emisi_kg / 1000

st.subheader("📊 Hasil Perhitungan Anda")

col1, col2 = st.columns(2)
with col1:
    st.metric(label="Total Emisi per Bulan", value=f"{total_emisi_kg:.2f} kg CO₂")
with col2:
    st.metric(label="Total Emisi dalam Ton", value=f"{total_emisi_ton:.3f} ton CO₂")

st.info("💡 Tips: Kurangi penggunaan kendaraan pribadi dan beralih ke energi efisien untuk menekan jejak karbon Anda!")
