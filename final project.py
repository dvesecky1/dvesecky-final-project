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
import matplotlib.pyplot as plt


BASE_PATH=r'c:\Users\dv987\Documents\GitHub\dvesecky-final-project'

#Loading the PEI data
def load_pei(path):
    df=pd.read_csv(os.path.join(BASE_PATH, path))
    df=df[['country', 'PEIIndexp', 'PEIIndexi', 'PEItype']].dropna(how='all')
    df=df.rename(columns={'country':'Country'})
    return df
pei=load_pei('dataverse_files\PEI country-level data (PEI_9.0).csv')

#Loading the PEI data
def load_acled(path):
    df=pd.read_excel(os.path.join(BASE_PATH, path))
    df=df[['Country', 'Index Ranking']].dropna(how='all')
    df=df.rename(columns={'Index Ranking':'ACLED Index'})
    return df
acled=load_acled('July-2023-Index-Rankings.xlsx')

#Loading the World Bank Data
def load_wb():
    start=datetime.date(year=2022, month=1,  day=1)
    end=datetime.date(year=2023, month=12, day=31)
    indicator_WB = ['NY.GDP.PCAP.KD', 'SP.POP.TOTL']
    df=wb.download(indicator=indicator_WB, country='all', start=start, end=end)
    df=df.iloc[49:]
    df.reset_index(inplace=True)
    df=df.drop(['year'], axis=1)
    df=df.rename(columns={'NY.GDP.PCAP.KD':'GDP per Capita', 'SP.POP.TOTL':'Total Population', 'country':'Country'})
    return df
df_wb=load_wb()

#Merging the data together
def merge_all(pei, acled, df_wb):
    df_pei_acled=pei.merge(acled, how='left', on='Country')
    df=df_pei_acled.merge(df_wb, how='left', on='Country')
    return df
df_merged=merge_all(pei, acled, df_wb)

#Creating some plots with the merged data
def violence_by_election_type_plot(df):
    fig, ax=plt.subplots()
    order = ['Very Low', 'Low', 'Moderate', 'High', 'Very High']
    df.PEItype = df.PEItype.astype("category")
    df.PEItype = df.PEItype.cat.set_categories(order)
    df=df.sort_values(['PEItype'])
    plt.scatter(df['PEItype'], df['ACLED Index'])
    ax.set_title("Conflict Index Position by Electoral Integrity Category")
    ax.set_xlabel("Degree of Election Integrity")
    ax.set_ylabel("Conflict Index")
violence_by_election_type_plot(df_merged)

def gdp_per_captia_by_population_plot(df):
    fig, ax=plt.subplots()
    plt.yscale('log')
    plt.scatter(df['GDP per Capita'], df['Total Population'])
    ax.set_title("Per Capita GDP by Total Population")
    ax.set_xlabel("GDP per Capita")
    ax.set_ylabel("Total Population")
gdp_per_captia_by_population_plot(df_merged)