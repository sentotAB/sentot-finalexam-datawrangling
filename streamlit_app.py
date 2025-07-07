# 📦 Import libraries
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# ⚙️ Konfigurasi tampilan halaman
st.set_page_config(page_title="Netflix Dashboard", layout="wide")

# 🎬 Judul utama
st.title("UAS Data Wrangling-Sentot-24120510004-Dashboard Data Netflix")

# 📂 Load data
df = pd.read_csv("netflix_clean.csv")

# 🎯 Ringkasan Statistik
col1, col2, col3 = st.columns(3)
col1.metric("🎥 Jumlah Movie", df[df['type'] == "Movie"].shape[0])
col2.metric("📺 Jumlah TV Show", df[df['type'] == "TV Show"].shape[0])
col3.metric("📅 Tahun Terbanyak", df['release_year'].mode()[0])

# 🗂️ Tabs untuk navigasi konten
tab1, tab2, tab3 = st.tabs(["📊 Ringkasan", "🔍 Filter & Data", "🌍 Visualisasi"])

with tab1:
    st.subheader("🧾 Ringkasan Statistik")
    st.dataframe(df.describe())
    st.write(f"Jumlah total data: {len(df)}")

with tab2:
    st.subheader("🔍 Filter Data")
    selected_type = st.selectbox("Pilih Tipe Konten", df['type'].unique())
    selected_year = st.slider("Pilih Tahun Rilis", int(df['release_year'].min()), int(df['release_year'].max()))
    filtered_df = df[(df['type'] == selected_type) & (df['release_year'] == selected_year)]
    st.write(f"Menampilkan {selected_type} yang rilis di tahun {selected_year}:")
    st.dataframe(filtered_df)

with tab3:
    st.subheader("🌍 Top 10 Negara Produksi")
    country_counts = df['country'].value_counts().head(10)
    fig, ax = plt.subplots(figsize=(6, 3))
ax.bar(country_counts.index, country_counts.values, color='salmon')
ax.set_ylabel("Jumlah")
ax.set_xlabel("Negara")
ax.set_title("Top 10 Negara Produksi Konten")

# 🔧 Tambahkan rotasi label agar tidak bertumpuk
plt.xticks(rotation=45)

st.pyplot(fig)
