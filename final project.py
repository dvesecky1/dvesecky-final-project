# -*- coding: utf-8 -*-
"""
Created on Fri Nov 24 14:58:00 2023

@author: dv987
"""

import os
import pandas as pd
import pandas_datareader.data as web
from pandas_datareader import wb
import datetime


BASE_PATH=r'c:\Users\dv987\Documents\GitHub\dvesecky-final-project'

#Loading the PEI data
def load_pei(path):
    df=pd.read_csv(os.path.join(BASE_PATH, path))
    df=df[['country', 'PEIIndexp', 'PEIIndexi', 'rating', 'PEItype']].dropna(how='all')
    df=df.rename(columns={'country':'Country'})
    return df
pei=load_pei('dataverse_files\PEI country-level data (PEI_9.0).csv')

#Loading the PEI data
def load_acled(path):
    df=pd.read_excel(os.path.join(BASE_PATH, path))
    df=df[['Country', 'Index Ranking', 'Index Category']].dropna(how='all')
    return df
acled=load_acled('July-2023-Index-Rankings.xlsx')

#Loading the World Bank Data
def load_wb():
    start = datetime.date(year=2022, month=1,  day=1)
    end = datetime.date(year=2023, month=12, day=31)
    indicator_WB = ['NY.GDP.PCAP.KD', 'SP.POP.TOTL']
    df = wb.download(indicator=indicator_WB, country='all', start=start, end=end)
    return df
df_wb=load_wb()
