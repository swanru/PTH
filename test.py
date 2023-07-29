import pandas as pd
from openpyxl import load_workbook
wb = load_workbook(filename='2021.xlsx')
sr = wb['Sheet1']
data = pd.DataFrame(sr.values)
d = data
d[1:5][[0,1,2,3,4,5]]
d.columns = ['Daerah','Positif','Sembuh','Dirawat','Meninggal','BULAN']
april = d[d.BULAN == 'APRIL'].reset_index(drop=True)
april = april[['Daerah','Positif','Meninggal']]
april['Jarak'] = april['Positif'] - april['Meninggal']
april