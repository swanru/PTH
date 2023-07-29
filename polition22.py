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
data = data.assign(
    date_recorded = data['date_recorded'].apply(
        lambda x:datetime.strptime(x,'%d-%m-%Y')
    )
)
# Transforming Datetime to US
data['Tahun'] = pd.to_datetime(data['date_recorded']).dt.strftime('%Y')
data = data[data.Tahun == '2020'].reset_index(drop=True)
data['Bulan'] = pd.to_datetime(data['date_recorded']).dt.strftime('%m')
data