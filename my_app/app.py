# -*- coding: utf-8 -*-
"""
Created on Thu Nov 30 14:56:31 2023

@author: dv987
"""

import os
import pandas as pd
import matplotlib.pyplot as plt
from shiny import App, render, ui, reactive
import seaborn as sns

BASE_PATH=r'c:\Users\dv987\Documents\GitHub\dvesecky-final-project'

#Terminal commands for launching shiny
#cd documents\GitHub\dvesecky-final-project
#shiny run --reload my_app/app.py

def load_merged(path):
    df=pd.read_csv(os.path.join(BASE_PATH, path))
    return df
df_merged=load_merged('Data\merged.csv')

#Functions for plotting with shiny
def acled_index_by_wb_statistic(df, stat, size):
    fig, ax=plt.subplots()
    if stat=='Total Population':
        plt.yscale('log')
    plt.scatter(df['ACLED Index'], df[stat], s=size)
    ax.set_title("ACLED Index by " + stat)
    ax.set_xlabel("ACLED Index")
    ax.set_ylabel(stat)

#Generating a shiny page with some plots
app_ui = ui.page_fluid(
    #Text with relevant information
    ui.panel_title('Final Project'),
    ui.row(ui.column(4, ui.em(ui.h3("Danny Vesecky")),
                     offset=1,
                     align='center'),
           ui.column(4, ui.h3('PPHA 30538 Autumn 2023'),
                     offset=2,
                     align='center')),
    ui.layout_sidebar(
        ui.sidebar(
            #Sliders for point and text size
            ui.input_slider("cex", "Point Size", min=0, max=100, value=50, step=5),
            ui.input_slider("cexaxis", "Axis Text Size", min=0, max=2, value=1, step=0.25), 
        ),
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
    ),
)

def server(input, output, session):
    @output
    @render.plot
    def pei_plot():
        p = sns.scatterplot(data = df_merged,
                            x = "PEIIndexi",
                            y = input.wb_statistic_pei(),
                            s = float(input.cex()))
        sns.set(font_scale=input.cexaxis())
        return(p)
    @render.plot
    def acled_plot():
        p = sns.scatterplot(data = df_merged,
                            x = "ACLED Index",
                            y = input.wb_statistic_acled(),
                            s = float(input.cex()))
        sns.set(font_scale=input.cexaxis())
        return(p)
app = App(app_ui, server)