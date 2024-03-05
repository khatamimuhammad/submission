import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Membaca dataset
df = pd.read_csv('./Dashboard/all_data.csv')

# Judul Dashboard
st.title('Air Quality Dashboard')

# Sidebar untuk pemilihan tahun dan bulan
year = st.sidebar.selectbox('Pilih Tahun', df['year'].unique())
month = st.sidebar.selectbox('Pilih Bulan', df['month'].unique())

# Filter data berdasarkan pemilihan tahun dan bulan
filtered_df = df[(df['year'] == year) & (df['month'] == month)]

# Menampilkan informasi umum dataset
st.subheader('Informasi Umum Dataset:')
st.write(df.info())

# Visualisasi distribusi PM2.5
st.subheader('Distribusi PM2.5:')
plt.figure(figsize=(10, 6))
sns.histplot(df['PM2.5'], kde=True, bins=30, color='blue')
st.pyplot()

# Visualisasi rata-rata kualitas udara dari tahun ke tahun
st.subheader('Tren Rata-rata Kualitas Udara dari Tahun ke Tahun:')
yearly_mean = df.groupby('year').mean()
plt.figure(figsize=(10, 6))
sns.lineplot(data=yearly_mean[['PM2.5', 'PM10', 'SO2', 'NO2', 'CO', 'O3']])
st.pyplot()

# Visualisasi pola musiman kualitas udara
st.subheader('Pola Musiman Kualitas Udara:')
monthly_mean = df.groupby('month').mean()
plt.figure(figsize=(10, 6))
sns.lineplot(data=monthly_mean[['PM2.5', 'PM10', 'SO2', 'NO2', 'CO', 'O3']])
st.pyplot()

# Visualisasi pola perubahan kualitas udara selama hari tertentu
st.subheader('Pola Perubahan PM2.5 Selama Hari:')
plt.figure(figsize=(10, 6))
sns.lineplot(data=filtered_df, x='hour', y='PM2.5')
st.pyplot()
