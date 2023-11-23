from urllib.error import URLError
import altair as alt
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
from streamlit.hello.utils import show_code
import plotly.express as px
kota = pd.read_csv("PRSA_Data_Wanshouxigong_20130301-20170228.csv")

def data():
    st.title("Kesimpulan")
    st.write(
        """
        # Pertanyaan 
        1. Bagaimana Kualitas Udara pada setiap kota dalam kurun waktu tertentu ?
        2. Nilai Polutan paling tinggi berdasarkan rata-rata seluruh waktu terdapat pada kota?
        3. Kapan kualitas udara memiliki kualitas tidak baik dalam kurun waktu tertentu pada setiap kota berdasarkan Indeks Standar Pencemar Udara?
        ## Jawab
        1. Berdasarkan dari hasil penelitian dengan mengkategorikan periode waktu yaitu harian, 30 hari, bulanan, tahunan mendapatkan hasil bahwa pada Berdasarkan hasil penelitian maka didapatkan kesimpulan yaitu kota Aotizhongxin mulai memiliki kualitas udara terburuk pada tahun 2014 hingga 2016 menurun tetapi kembali memuncak pada tahun 2017, kota Changping memiliki kualitas udara terburuk pada tahun 2014 dengan kualitas udara tertinggi dimulai dari bulan 3 menurun hingga bulan 10 kemudian kembali memuncak pada bulan 12 dan kualitas udara harian terburuk terjadi pada pertengahan bulan. kota Dingling memiliki kualitas udara terburuk mulai pada tahun 2014 dengan kualitas udara terburuk terjadi pada bulan 3 hingga bulan 9 kemudian kembali memuncak dibulan 12 dan kualitas udara harian terburuk terjadi pada pertengahan bulan. Kota Dongsi memiliki kualitas udara terburuk pada tahun 2017 dengan kualitas udara terburuk pada bulan 3 hingga bulan 8 kembali memuncak pada bulan 12 dan kualitas udara harian terburuk terjadi pada pertengahan bulan. Kota Guanyuan memiliki kualitas udara terburuk mulai pada tahun 2014 kemudian memuncak pada tahun 2017 dengan kualitas terburuk pada bulan 3 hingga bulan 8 kembali memuncak pada bulan 12 dan kualitas udara harian terburuk terjadi pada pertengahan bulan. Kota Gucheng memiliki kualitas udara terburuk pada tahun 2014 dengan kualitas udara terburuk pada bulan 3 hingga bulan 8 kembali memuncak pada tahun 12 dan kualitas udara harian terburuk terjadi pada pertengahan bulan Kota Nongzhanguan memiliki kualitas udara terburuk pada tahun 2014 dengan puncak kualitas udara terjadi pada bulan 3 dan kualitas udara harian terburuk terjadi pada pertengahan bulan. Kota Shunyi memiliki kualitas udara terburuk pada tahun 2014 dengan puncak kualitas udara terburuk terjadi pada bulan 4 dan kualitas udara harian terburuk terjadi pada pertengahan bulan Kota Tiantan memiliki kualitas udara terburuk pada tahun 2017 dengan puncak kualitas udara terburuk terjadi pada akhir tahun dan kualitas udara harian terburuk terjadi pada pertengahan bulan. Kota Wanliu memiliki kualitas udara terburuk pada tahun 2014 dengan puncak kualitas yang terjadi pada bulan 3 dan kualitas udara harian terburuk terjadi pada pertengahan bulan Kota Wanshouxigong memiliki kualitas udara terburuk pada tahun 2014 dengan puncak kualitas udara terburuk pada bulan 3 dan kualitas udara harian terburuk terjadi pada pertengahan bulan.
        2. Berdasarkan dari hasil penelitian maka didapatkan hasil yaitu data polutan PM2.5 pada kota Dongsi, polutan PM10 pada kota Guchen, polutan SO2 pada kota Nongzhanguan, polutan NO2 pada kota Wanliu, polutan O3 pada kota Dingling, polutan CO pada kota Wanshouxigong
        3. Prediksi Udara yang memiliki kualitas terburuk dalam kurun waktu pada kota Aotizhongxin pada pukul 6 AM ,Changping pada pukul 9 AM ,Dingling pada pukul 17 PM ,Dongsi pada pukul 15 PM ,Guanyuan pada pukul 15 PM ,Gucheng pada pukul 6 PM ,Nongzhanguan pada pukul 9 PM ,Shunyi pada pukul 17 PM ,Tiantan pada pukul 15 PM ,Wanliu pada pukul 15 PM ,Wanshouxigong pada pukul 15 PM
        """
    )
data()