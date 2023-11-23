from urllib.error import URLError
import altair as alt
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
from streamlit.hello.utils import show_code
import plotly.express as px
kota = pd.read_csv("PRSA_Data_Aotizhongxin_20130301-20170228.csv")
def data():
    st.write("Dataset")
    st.write(kota.head())
    tab1, tab2 ,tab3 = st.tabs(["Dataset", "Korelasi Data","Kualitas Udara"])
    with tab1:
        st.write(
            """
            ## Data Cleaning
            Penelitian ini menggunakan Dropping Method dalam pemrosesan Data Cleaning sebagai berikut:
            """
            )
        st.write("Dataset sebelum dilakukan Data Cleaning",kota.isna().sum())
        kota2 = kota.dropna(axis=0).reset_index(drop=True)
        st.write("Dataset setelah melakukan Data Cleaning",kota2.isna().sum())
        st.write("Exploratory Data Analysis",kota.describe())
    with tab2:
        Pollution_dataset = kota[['PM2.5','PM10','SO2','NO2','CO','O3']]
        st.write("Dataset Polutant",Pollution_dataset.head())
        korelasi_data = Pollution_dataset.corr()
        
        fig,ax=plt.subplots()
        sns.heatmap(korelasi_data,ax=ax)
        st.write("Heatmap",fig)
        st.write("Nilai korelasi data",korelasi_data)
    with tab3:
        st.write(
            """
            ## Data Pollutan
            Data polutan yang digunakan pada penelitian ini adalah PM10, PM2.5, O3, NO2, SO2, CO
            """
        )
        Pollution = kota[['month','day','year','hour','PM2.5','PM10','SO2','NO2','CO','O3']]
        Pollution['date'] = pd.to_datetime(Pollution[['year','month','day']])
        st.write(Pollution.head())
        tab_1,tab_2,tab_3,tab_4,tab_5 = st.tabs(["Tahunan", "Bulanan","30 Hari","Setiap Jam","2013-2017"])
        with tab_1:
            dataset_year = kota.groupby(by='year').agg({
            'PM10':'mean',
            'PM2.5':'mean',
            'O3':'mean',
            'NO2':'mean',
            'SO2':'mean',
            })    
            st.line_chart(dataset_year)
            st.write(dataset_year)
        with tab_2:
            dataset_month = kota.groupby(by='month').agg({
            'PM10':'mean',
            'PM2.5':'mean',
            'O3':'mean',
            'NO2':'mean',
            'SO2':'mean',
            })
            st.line_chart(dataset_month)
            st.write(dataset_month)
        with tab_3:
            dataset_day = kota.groupby(by='day').agg({
            'PM10':'mean',
            'PM2.5':'mean',
            'O3':'mean',
            'NO2':'mean',
            'SO2':'mean',
            })
        with tab_4:
            dataset_hour = kota.groupby(by='hour').agg({
            'PM10':'mean',
            'PM2.5':'mean',
            'O3':'mean',
            'NO2':'mean',
            'SO2':'mean',
            })
            st.line_chart(dataset_hour)
            st.write(dataset_hour)        
        with tab_5:    
            dataset_days = Pollution.groupby(by='date').agg({
            'PM10':'mean',
            'PM2.5':'mean',
            'O3':'mean',
            'NO2':'mean',
            'SO2':'mean',
            })
            st.line_chart(dataset_days)
            st.write(dataset_days.head())
st.title('Kualitas Udara Kota Aotizhongxin')
data()