# -*- coding: utf-8 -*-
"""
Created on Thu Nov 30 14:15:11 2023

@author: dv987
"""
import os
import pandas as pd
import matplotlib.pyplot as plt

BASE_PATH=r'c:\Users\dv987\Documents\GitHub\dvesecky-final-project'

def load_merged(path):
    df=pd.read_csv(os.path.join(BASE_PATH, path))
    return df
df_merged=load_merged('merged.csv')

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