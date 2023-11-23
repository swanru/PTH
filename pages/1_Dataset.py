from urllib.error import URLError
import altair as alt
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
from streamlit.hello.utils import show_code
import plotly.express as px
Aotizhongxin = pd.read_csv("PRSA_Data_Aotizhongxin_20130301-20170228.csv")
Changping = pd.read_csv("PRSA_Data_Changping_20130301-20170228.csv")
Dingling = pd.read_csv("PRSA_Data_Dingling_20130301-20170228.csv")
Dongsi = pd.read_csv("PRSA_Data_Dongsi_20130301-20170228.csv")
Guanyuan = pd.read_csv("PRSA_Data_Guanyuan_20130301-20170228.csv")
Gucheng = pd.read_csv("PRSA_Data_Gucheng_20130301-20170228.csv")
Nongzhanguan = pd.read_csv("PRSA_Data_Nongzhanguan_20130301-20170228.csv")
Shunyi = pd.read_csv("PRSA_Data_Shunyi_20130301-20170228.csv")
Tiantan = pd.read_csv("PRSA_Data_Tiantan_20130301-20170228.csv")
Wanliu = pd.read_csv("PRSA_Data_Wanliu_20130301-20170228.csv")
Wanshouxigong = pd.read_csv("PRSA_Data_Wanshouxigong_20130301-20170228.csv")


def data():
    data = [Aotizhongxin,Changping,Dingling,Dongsi,Guanyuan,Gucheng,Nongzhanguan,Shunyi,Tiantan,Wanliu,Wanshouxigong]
    dataset = pd.concat(data)
    st.write("Dataset",dataset.head())
    tab1, tab2, tab3= st.tabs(["Korelasi Data","Kualitas Udara","Prediksi"])
    # tab1
    with tab1:
        Pollution_dataset = dataset[['PM2.5','PM10','SO2','NO2','CO','O3']]
        st.write("Dataset Polutant",Pollution_dataset)
        st.write("Korelasi antar data:")
        korelasi_data = Pollution_dataset.corr()
        
        fig,ax=plt.subplots()
        sns.heatmap(korelasi_data,ax=ax)
        st.write(fig)
        st.write(korelasi_data)
    # tab2
    with tab2:
        dataset_station = dataset.groupby(by='station').agg({
            'PM2.5':'mean',
            'PM10':'mean',
            'SO2':'mean',
            'NO2':'mean',
            'O3':'mean',
            'CO':'mean',
        })
        st.line_chart(dataset_station)
        data = pd.DataFrame(dataset_station)
        High_PM25 = pd.DataFrame(data["PM2.5"].sort_values(ascending=False).reset_index())
        High_PM10 = pd.DataFrame(data["PM10"].sort_values(ascending=False).reset_index()) 
        High_SO2  = pd.DataFrame(data["SO2"].sort_values(ascending=False).reset_index())
        High_NO2  = pd.DataFrame(data["NO2"].sort_values(ascending=False).reset_index())
        High_O3   = pd.DataFrame(data["O3"].sort_values(ascending=False).reset_index())
        High_CO = pd.DataFrame(dataset_station["CO"].sort_values(ascending=False).reset_index())
        st.write(data)
        Hasil = pd.DataFrame({"Data Tertinggi": ["PM 2.5", "PM 10",
                                        "SO2","NO2",
                                        "O3","CO"], 
                      "Kota"          :[High_PM25.station[0], High_PM10.station[0],
                                        High_SO2.station[0], High_NO2.station[0],
                                        High_O3.station[0], High_CO.station[0]],
                      "Nilai"         :[High_PM25["PM2.5"][0], High_PM10.PM10[0],
                                        High_SO2.SO2[0], High_NO2.NO2[0],
                                        High_O3.O3[0], High_CO.CO[0]]})
        Hasil.to_numpy()
        st.write("Data Polutant tertinggi",Hasil)
    with tab3:
        # 2013 - 2017
        Pollution_Aotizhongxin = Aotizhongxin[['month','day','year','hour','PM2.5','PM10','SO2','NO2','CO','O3']]
        Pollution_Changping = Changping[['month','day','year','hour','PM2.5','PM10','SO2','NO2','CO','O3']]
        Pollution_Dingling = Dingling[['month','day','year','hour','PM2.5','PM10','SO2','NO2','CO','O3']]
        Pollution_Dongsi = Dongsi[['month','day','year','hour','PM2.5','PM10','SO2','NO2','CO','O3']] 
        Pollution_Guanyuan = Guanyuan[['month','day','year','hour','PM2.5','PM10','SO2','NO2','CO','O3']] 
        Pollution_Gucheng = Gucheng[['month','day','year','hour','PM2.5','PM10','SO2','NO2','CO','O3']] 
        Pollution_Nongzhanguan = Nongzhanguan[['month','day','year','hour','PM2.5','PM10','SO2','NO2','CO','O3']] 
        Pollution_Shunyi = Shunyi[['month','day','year','hour','PM2.5','PM10','SO2','NO2','CO','O3']] 
        Pollution_Tiantan = Tiantan[['month','day','year','hour','PM2.5','PM10','SO2','NO2','CO','O3']] 
        Pollution_Wanliu = Wanliu[['month','day','year','hour','PM2.5','PM10','SO2','NO2','CO','O3']] 
        Pollution_Wanshouxigong = Wanshouxigong[['month','day','year','hour','PM2.5','PM10','SO2','NO2','CO','O3']]
        Pollution_Aotizhongxin ['date'] = pd.to_datetime(Pollution_Aotizhongxin [['year','month','day']])
        Pollution_Changping ['date'] = pd.to_datetime(Pollution_Changping [['year','month','day']])
        Pollution_Dingling ['date'] = pd.to_datetime(Pollution_Dingling [['year','month','day']])
        Pollution_Dongsi ['date'] = pd.to_datetime(Pollution_Dongsi [['year','month','day']])
        Pollution_Guanyuan ['date'] = pd.to_datetime(Pollution_Guanyuan [['year','month','day']])
        Pollution_Gucheng ['date'] = pd.to_datetime(Pollution_Gucheng [['year','month','day']])
        Pollution_Nongzhanguan ['date'] = pd.to_datetime(Pollution_Nongzhanguan [['year','month','day']])
        Pollution_Shunyi ['date'] = pd.to_datetime(Pollution_Shunyi [['year','month','day']])
        Pollution_Tiantan ['date'] = pd.to_datetime(Pollution_Tiantan [['year','month','day']])
        Pollution_Wanliu['date'] = pd.to_datetime(Pollution_Wanliu[['year','month','day']])
        Pollution_Wanshouxigong ['date'] = pd.to_datetime(Pollution_Wanshouxigong [['year','month','day']]) 
        Pollutant = ['PM2.5','PM10','SO2','NO2','O3']
        data_kota1 = Pollution_Aotizhongxin.copy()
        data_kota2 = Pollution_Changping.copy()
        data_kota3 =Pollution_Dingling.copy()
        data_kota4 = Pollution_Dongsi.copy()
        data_kota5 =Pollution_Guanyuan.copy()
        data_kota6 =Pollution_Gucheng.copy()
        data_kota7 =Pollution_Nongzhanguan.copy()
        data_kota8 =Pollution_Shunyi.copy()
        data_kota9 =Pollution_Tiantan.copy()
        data_kota10=Pollution_Wanliu.copy()
        data_kota11=Pollution_Wanshouxigong.copy()
        data_prediksi1  = pd.pivot_table(data=data_kota1,index=["hour"],values=Pollutant,aggfunc='mean').round()
        data_prediksi2  = pd.pivot_table(data=data_kota2,index=["hour"],values=Pollutant,aggfunc='mean').round()
        data_prediksi3  = pd.pivot_table(data=data_kota3,index=["hour"],values=Pollutant,aggfunc='mean').round()
        data_prediksi4  = pd.pivot_table(data=data_kota4,index=["hour"],values=Pollutant,aggfunc='mean').round()
        data_prediksi5  = pd.pivot_table(data=data_kota5,index=["hour"],values=Pollutant,aggfunc='mean').round()
        data_prediksi6  = pd.pivot_table(data=data_kota6,index=["hour"],values=Pollutant,aggfunc='mean').round()
        data_prediksi7  = pd.pivot_table(data=data_kota7,index=["hour"],values=Pollutant,aggfunc='mean').round()
        data_prediksi8  = pd.pivot_table(data=data_kota8,index=["hour"],values=Pollutant,aggfunc='mean').round()
        data_prediksi9  = pd.pivot_table(data=data_kota9,index=["hour"],values=Pollutant,aggfunc='mean').round()
        data_prediksi10 = pd.pivot_table(data=data_kota10,index=["hour"],values=Pollutant,aggfunc='mean').round()
        data_prediksi11 = pd.pivot_table(data=data_kota11,index=["hour"],values=Pollutant,aggfunc='mean').round()
        data_prediksi1['kategori'] = pd.Series()
        for index, row in enumerate(data_prediksi1.itertuples()):
            temp_treeshold = 0
            for cell in row:
                if type(cell) == int or type(cell) == float:
                    if cell > temp_treeshold:
                        if cell in range(1,50):
                            data_prediksi1.kategori.loc[index] = '1.Baik'
                        elif cell in range(51,100):
                            data_prediksi1.kategori.loc[index] = '2.Sedang'
                        elif cell in range(101,200):
                            data_prediksi1.kategori.loc[index] = '3.Tidak Sehat'
                        elif cell in range(201,300):
                            data_prediksi1.kategori.loc[index] = '4.Sangat Tidak Sehat'
                        else:
                            data_prediksi1.kategori.loc[index] = '5.Berbahaya'
                        temp_treeshold = cell
        data_prediksi2['kategori'] = pd.Series()
        for index, row in enumerate(data_prediksi2.itertuples()):
            temp_treeshold = 0
            for cell in row:
                if type(cell) == int or type(cell) == float:
                    if cell > temp_treeshold:
                        if cell in range(1,50):
                            data_prediksi2.kategori.loc[index] = '1.Baik'
                        elif cell in range(51,100):
                            data_prediksi2.kategori.loc[index] = '2.Sedang'
                        elif cell in range(101,200):
                            data_prediksi2.kategori.loc[index] = '3.Tidak Sehat'
                        elif cell in range(201,300):
                            data_prediksi2.kategori.loc[index] = '4.Sangat Tidak Sehat'
                        else:
                            data_prediksi2.kategori.loc[index] = '5.Berbahaya'
                        temp_treeshold = cell
        data_prediksi3['kategori'] = pd.Series()
        for index, row in enumerate(data_prediksi3.itertuples()):
            temp_treeshold = 0
            for cell in row:
                if type(cell) == int or type(cell) == float:
                    if cell > temp_treeshold:
                        if cell in range(1,50):
                            data_prediksi3.kategori.loc[index] = '1.Baik'
                        elif cell in range(51,100):
                            data_prediksi3.kategori.loc[index] = '2.Sedang'
                        elif cell in range(101,200):
                            data_prediksi3.kategori.loc[index] = '3.Tidak Sehat'
                        elif cell in range(201,300):
                            data_prediksi3.kategori.loc[index] = '4.Sangat Tidak Sehat'
                        else:
                            data_prediksi3.kategori.loc[index] = '5.Berbahaya'
                        temp_treeshold = cell
        data_prediksi4['kategori'] = pd.Series()
        for index, row in enumerate(data_prediksi4.itertuples()):
            temp_treeshold = 0
            for cell in row:
                if type(cell) == int or type(cell) == float:
                    if cell > temp_treeshold:
                        if cell in range(1,50):
                            data_prediksi4.kategori.loc[index] = '1.Baik'
                        elif cell in range(51,100):
                            data_prediksi4.kategori.loc[index] = '2.Sedang'
                        elif cell in range(101,200):
                            data_prediksi4.kategori.loc[index] = '3.Tidak Sehat'
                        elif cell in range(201,300):
                            data_prediksi4.kategori.loc[index] = '4.Sangat Tidak Sehat'
                        else:
                            data_prediksi4.kategori.loc[index] = '5.Berbahaya'
                        temp_treeshold = cell
        data_prediksi5['kategori'] = pd.Series()
        for index, row in enumerate(data_prediksi5.itertuples()):
            temp_treeshold = 0
            for cell in row:
                if type(cell) == int or type(cell) == float:
                    if cell > temp_treeshold:
                        if cell in range(1,50):
                            data_prediksi5.kategori.loc[index] = '1.Baik'
                        elif cell in range(51,100):
                            data_prediksi5.kategori.loc[index] = '2.Sedang'
                        elif cell in range(101,200):
                            data_prediksi5.kategori.loc[index] = '3.Tidak Sehat'
                        elif cell in range(201,300):
                            data_prediksi5.kategori.loc[index] = '4.Sangat Tidak Sehat'
                        else:
                            data_prediksi5.kategori.loc[index] = '5.Berbahaya'
                        temp_treeshold = cell
        data_prediksi6['kategori'] = pd.Series()
        for index, row in enumerate(data_prediksi6.itertuples()):
            temp_treeshold = 0
            for cell in row:
                if type(cell) == int or type(cell) == float:
                    if cell > temp_treeshold:
                        if cell in range(1,50):
                            data_prediksi6.kategori.loc[index] = '1.Baik'
                        elif cell in range(51,100):
                            data_prediksi6.kategori.loc[index] = '2.Sedang'
                        elif cell in range(101,200):
                            data_prediksi6.kategori.loc[index] = '3.Tidak Sehat'
                        elif cell in range(201,300):
                            data_prediksi6.kategori.loc[index] = '4.Sangat Tidak Sehat'
                        else:
                            data_prediksi6.kategori.loc[index] = '5.Berbahaya'
                        temp_treeshold = cell
        data_prediksi7['kategori'] = pd.Series()
        for index, row in enumerate(data_prediksi7.itertuples()):
            temp_treeshold = 0
            for cell in row:
                if type(cell) == int or type(cell) == float:
                    if cell > temp_treeshold:
                        if cell in range(1,50):
                            data_prediksi7.kategori.loc[index] = '1.Baik'
                        elif cell in range(51,100):
                            data_prediksi7.kategori.loc[index] = '2.Sedang'
                        elif cell in range(101,200):
                            data_prediksi7.kategori.loc[index] = '3.Tidak Sehat'
                        elif cell in range(201,300):
                            data_prediksi7.kategori.loc[index] = '4.Sangat Tidak Sehat'
                        else:
                            data_prediksi7.kategori.loc[index] = '5.Berbahaya'
                        temp_treeshold = cell
        data_prediksi8['kategori'] = pd.Series()
        for index, row in enumerate(data_prediksi8.itertuples()):
            temp_treeshold = 0
            for cell in row:
                if type(cell) == int or type(cell) == float:
                    if cell > temp_treeshold:
                        if cell in range(1,50):
                            data_prediksi8.kategori.loc[index] = '1.Baik'
                        elif cell in range(51,100):
                            data_prediksi8.kategori.loc[index] = '2.Sedang'
                        elif cell in range(101,200):
                            data_prediksi8.kategori.loc[index] = '3.Tidak Sehat'
                        elif cell in range(201,300):
                            data_prediksi8.kategori.loc[index] = '4.Sangat Tidak Sehat'
                        else:
                            data_prediksi8.kategori.loc[index] = '5.Berbahaya'
                        temp_treeshold = cell
        data_prediksi9['kategori'] = pd.Series()
        for index, row in enumerate(data_prediksi9.itertuples()):
            temp_treeshold = 0
            for cell in row:
                if type(cell) == int or type(cell) == float:
                    if cell > temp_treeshold:
                        if cell in range(1,50):
                            data_prediksi9.kategori.loc[index] = '1.Baik'
                        elif cell in range(51,100):
                            data_prediksi9.kategori.loc[index] = '2.Sedang'
                        elif cell in range(101,200):
                            data_prediksi9.kategori.loc[index] = '3.Tidak Sehat'
                        elif cell in range(201,300):
                            data_prediksi9.kategori.loc[index] = '4.Sangat Tidak Sehat'
                        else:
                            data_prediksi9.kategori.loc[index] = '5.Berbahaya'
                        temp_treeshold = cell
        data_prediksi10['kategori'] = pd.Series()
        for index, row in enumerate(data_prediksi10.itertuples()):
            temp_treeshold = 0
            for cell in row:
                if type(cell) == int or type(cell) == float:
                    if cell > temp_treeshold:
                        if cell in range(1,50):
                            data_prediksi10.kategori.loc[index] = '1.Baik'
                        elif cell in range(51,100):
                            data_prediksi10.kategori.loc[index] = '2.Sedang'
                        elif cell in range(101,200):
                            data_prediksi10.kategori.loc[index] = '3.Tidak Sehat'
                        elif cell in range(201,300):
                            data_prediksi10.kategori.loc[index] = '4.Sangat Tidak Sehat'
                        else:
                            data_prediksi10.kategori.loc[index] = '5.Berbahaya'
                        temp_treeshold = cell
        data_prediksi11['kategori'] = pd.Series()
        for index, row in enumerate(data_prediksi11.itertuples()):
            temp_treeshold = 0
            for cell in row:
                if type(cell) == int or type(cell) == float:
                    if cell > temp_treeshold:
                        if cell in range(1,50):
                            data_prediksi11.kategori.loc[index] = '1.Baik'
                        elif cell in range(51,100):
                            data_prediksi11.kategori.loc[index] = '2.Sedang'
                        elif cell in range(101,200):
                            data_prediksi11.kategori.loc[index] = '3.Tidak Sehat'
                        elif cell in range(201,300):
                            data_prediksi11.kategori.loc[index] = '4.Sangat Tidak Sehat'
                        else:
                            data_prediksi11.kategori.loc[index] = '5.Berbahaya'
                        temp_treeshold = cell
        data_prediksi_kota1 = data_prediksi1.sort_values('kategori',ascending=False)
        data_prediksi_kota2 = data_prediksi2.sort_values('kategori',ascending=False)
        data_prediksi_kota3 = data_prediksi3.sort_values('kategori',ascending=False)
        data_prediksi_kota4 = data_prediksi4.sort_values('kategori',ascending=False)
        data_prediksi_kota5 = data_prediksi5.sort_values('kategori',ascending=False)
        data_prediksi_kota6 = data_prediksi1.sort_values('kategori',ascending=False)
        data_prediksi_kota7 = data_prediksi2.sort_values('kategori',ascending=False)
        data_prediksi_kota8 = data_prediksi3.sort_values('kategori',ascending=False)
        data_prediksi_kota9 = data_prediksi4.sort_values('kategori',ascending=False)
        data_prediksi_kota10 = data_prediksi5.sort_values('kategori',ascending=False)
        data_prediksi_kota11 = data_prediksi5.sort_values('kategori',ascending=False)
        st.write("Prediksi Udara yang memiliki kualitas terburuk dalam kurun waktu pada kota\nAotizhongxin pada pukul",data_prediksi_kota1.index[0],"AM")
        st.write("Changping pada pukul",data_prediksi_kota2.index[0],"AM")
        st.write("Dingling pada pukul",data_prediksi_kota3.index[0],"PM")
        st.write("Dongsi pada pukul",data_prediksi_kota4.index[0],"PM")
        st.write("Guanyuan pada pukul",data_prediksi_kota5.index[0],"PM")
        st.write("Gucheng pada pukul",data_prediksi_kota6.index[0],"PM")
        st.write("Nongzhanguan pada pukul",data_prediksi_kota7.index[0],"PM") 
        st.write("Shunyi pada pukul",data_prediksi_kota8.index[0],"PM") 
        st.write("Tiantan pada pukul",data_prediksi_kota9.index[0],"PM") 
        st.write("Wanliu pada pukul",data_prediksi_kota10.index[0],"PM") 
        st.write("Wanshouxigong pada pukul",data_prediksi_kota11.index[0],"PM") 

    

st.title('Dataset Seluruh Kota')
data()