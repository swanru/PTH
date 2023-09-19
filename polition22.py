import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from pandas import DataFrame, Series
from datetime import datetime
data = pd.read_csv('climate_data.csv')
data.head()
colum = {'Tn':'temp_min',
    'Tx':'temp_max',
    'Tavg':'temp_avg',
    'RH_avg':'humidity_avg',
    'RR':'rainfall',
    'ss':'duration_sunshine_hr',
    'ff_x':'wind_speed_max',
    'ddd_x':'wind_direction_at_max_speed',
    'ff_avg':'wind_speed_avg',
    'ddd_car':'wind_direction_most_frequent',
    'station_id':'station_id',
    'date':'date_recorded'}
data = data.rename(columns=colum)
# Transforming Datetime to US
data = data.assign(
    date_recorded = data['date_recorded'].apply(
        lambda x:datetime.strptime(x,'%d-%m-%Y')
    )
)
data = data.fillna(0)
# Data year 2020, Month, Province
data['Tahun'] = pd.to_datetime(data['date_recorded']).dt.strftime('%Y')
data = data[data.Tahun == '2020'].reset_index(drop=True)
data['Bulan'] = pd.to_datetime(data['date_recorded']).dt.strftime('%m')
province = pd.read_csv('province_detail.csv')
station = pd.read_csv('station_detail.csv')
data = data.merge(station,'inner',left_on='station_id',right_on='station_id')
data = data.merge(province,'inner',left_on='province_id',right_on='province_id')
# Aceh (Nanggroe Aceh Darussalam)
data = data[data.province_id == 1].reset_index(drop=True)
temp_min_agg = pd.NamedAgg('temp_min','min')
temp_max_agg = pd.NamedAgg('temp_max','max')
temp_avg_agg = pd.NamedAgg('temp_avg','mean')
temp_avg_count_agg = pd.NamedAgg('temp_avg','count')
new_data = data.groupby('date_recorded').agg(temp_max=temp_max_agg,temp_min=temp_min_agg,
                                            temp_avg = temp_avg_agg,temp_count=temp_avg_count_agg)
visual_data = DataFrame({
    'temp_max':new_data['temp_max'].resample('1M').max(),
    'temp_min':new_data['temp_min'].resample('1M').min(),
    'temp_avg':new_data.resample('1M').agg(func=lambda x:sum(x.temp_count * x.temp_avg)/sum(x.temp_count))
})
fig, ax = plt.subplots(figsize=(20,7.5))
ax.set_title("Temperature by Month at Aceh")
ax.plot(visual_data.index,visual_data['temp_min'],label='Min. Temp')
ax.plot(visual_data.index,visual_data['temp_max'],label='Max. Temp')
ax.plot(visual_data.index,visual_data['temp_avg'],label='Avg. Temp')
ax.legend()
ax.plot
# data_bulan
# # High data per colums
# data_bulan = data_bulan[(data_bulan.wind_direction_at_max_speed>100) & (data_bulan.wind_direction_at_max_speed<200)]
# ctypes = {
#     'Tahun':int,
#     'Bulan':int,
# }
# data_bulan = data_bulan.astype(ctypes)
# data_bulan.dtypes

# Januari = data[data.Bulan == '01'].reset_index(drop=True)
# Februari = data[data.Bulan == '02'].reset_index(drop=True)
# Maret = data[data.Bulan == '03'].reset_index(drop=True)
# April = data[data.Bulan == '04'].reset_index(drop=True)
# Mei = data[data.Bulan == '05'].reset_index(drop=True)
# Juni = data[data.Bulan == '06'].reset_index(drop=True)
# Juli = data[data.Bulan == '07'].reset_index(drop=True)
# Agustus = data[data.Bulan == '08'].reset_index(drop=True)
# September = data[data.Bulan == '09'].reset_index(drop=True)
# Oktober = data[data.Bulan == '10'].reset_index(drop=True)
# November = data[data.Bulan == '11'].reset_index(drop=True)
# Desember = data[data.Bulan == '12'].reset_index(drop=True)