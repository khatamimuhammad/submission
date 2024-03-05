import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Judul Dashboard
st.title('Kualitas Udara')

# Membaca dataset
@st.cache
def load_data():
    data = pd.read_csv("./Dashboard/all_data.csv")
    return data

data = load_data()

# Tampilkan dataset
st.subheader('Data Kualitas Udara')
st.write(data)

# Tampilkan statistik deskriptif
st.subheader('Statistik Deskriptif')
st.write(data.describe())

# Visualisasi distribusi PM2.5
st.subheader('Distribusi PM2.5')
plt.figure(figsize=(8, 6))
sns.histplot(data['PM2.5'], kde=True, bins=30, color='blue')
plt.xlabel('PM2.5')
plt.ylabel('Frekuensi')
st.pyplot()

# Visualisasi matriks korelasi
st.subheader('Matriks Korelasi')
correlation_matrix = data.corr()
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f")
st.pyplot()
