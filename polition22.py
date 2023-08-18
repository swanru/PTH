import pandas as pd
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
# Data per year and month
data['Tahun'] = pd.to_datetime(data['date_recorded']).dt.strftime('%Y')
data = data[data.Tahun == '2020'].reset_index(drop=True)
data['Bulan'] = pd.to_datetime(data['date_recorded']).dt.strftime('%m')
data_bulan = data[data.Bulan == '01'].reset_index(drop=True)
data_bulan
# High data per colums
data_bulan = data_bulan[(data_bulan.wind_direction_at_max_speed>100) & (data_bulan.wind_direction_at_max_speed<200)]
ctypes = {
    'Tahun':int,
    'Bulan':int,
}
data_bulan = data_bulan.astype(ctypes)
data_bulan.dtypes
data_bulan
#shelwan riaudy U
#shelwan riaudy u universitas ahmad dahlan
