# -*- coding: utf-8 -*-
"""
Created on Thu Nov 30 14:56:31 2023

@author: dv987
"""

import os
import pandas as pd
import matplotlib.pyplot as plt
from shiny import App, render, ui, reactive

BASE_PATH=r'c:\Users\dv987\Documents\GitHub\dvesecky-final-project'

#Terminal commands for launching shiny
#cd documents\GitHub\dvesecky-final-project
#shiny run --reload my_app/app.py

def load_merged(path):
    df=pd.read_csv(os.path.join(BASE_PATH, path))
    return df
df_merged=load_merged('merged.csv')

#Functions for plotting with shiny
def pei_index_by_wb_statistic(df, stat):
    fig, ax=plt.subplots()
    if stat=='Total Population':
        plt.yscale('log')
    plt.scatter(df['PEIIndexi'], df[stat])
    ax.set_title("PEI Index by " + stat)
    ax.set_xlabel("PEI Index")
    ax.set_ylabel(stat)

def acled_index_by_wb_statistic(df, stat):
    fig, ax=plt.subplots()
    if stat=='Total Population':
        plt.yscale('log')
    plt.scatter(df['ACLED Index'], df[stat])
    ax.set_title("ACLED Index by " + stat)
    ax.set_xlabel("ACLED Index")
    ax.set_ylabel(stat)

#Generating a shiny page with some plots
app_ui = ui.page_fluid(
    #Text with relevant information
     ui.row(ui.column(12, ui.h1('Final Project'),
                     ui.hr(),
                     align='center')),
    ui.row(ui.column(4, ui.em(ui.h3("Danny Vesecky")),
                     offset=1,
                     align='center'),
           ui.column(4, ui.h3('PPHA 30538 Autumn 2023'),
                     offset=2,
                     align='center')),
    #Dropdown choices for World Bank statistics
    ui.row(ui.column(4, ui.input_select(id='wb_statistic_pei',
                                        label='Please pick a statistic',
                                        choices=['GDP per Capita', 'Total Population']),
                                                 offset=4,
                                                 align='center')),
    ui.output_plot('pei_plot'),
    ui.row(ui.column(4, ui.input_select(id='wb_statistic_acled',
                                        label='Please pick a statistic',
                                        choices=['GDP per Capita', 'Total Population']),
                                                 offset=4,
                                                 align='center')),
    ui.output_plot('acled_plot'),
    )

def server(input, output, session):
    @output
    @render.plot
    def pei_plot():
        return pei_index_by_wb_statistic(df_merged, input.wb_statistic_pei())
    @render.plot
    def acled_plot():
        return acled_index_by_wb_statistic(df_merged, input.wb_statistic_acled())
app = App(app_ui, server)