# -*- coding: utf-8 -*-
"""
Created on Wed Dec  6 15:18:08 2023

@author: dv987
"""

import os
import pandas as pd
from sklearn.linear_model import LinearRegression
import numpy as np
import matplotlib.pyplot as plt

BASE_PATH=r'c:\Users\dv987\Documents\GitHub\dvesecky-final-project'

def load_merged(path):
    df=pd.read_csv(os.path.join(BASE_PATH, path))
    df=df.dropna()
    return df
df_merged=load_merged('Data\merged.csv')

#Create a simple OLS regression function
def regression(x, y, df):
    x_v=np.array(x).reshape((-1,1))
    y_v=np.array(y)
    model = LinearRegression()
    model.fit(x_v, y_v)
    df['predicted']=model.predict(x_v)
    plt.scatter(x_v, y_v, color="black")
    plt.plot(x_v, df['predicted'], color="blue", linewidth=3)
    r_sqr=model.score(x_v, y_v)
    return model, r_sqr
#Regress electoral integrity index against conflict index
pei_acled_regression=regression(df_merged['PEIIndexp'], df_merged['ACLED Index'], df_merged)[0]
print('Model intercept: ' + str(pei_acled_regression.intercept_) + ', model slope: '
      + str(pei_acled_regression.coef_) + ', model r-squared: ' + 
      str(regression(df_merged['PEIIndexp'], df_merged['ACLED Index'], df_merged)[1]))
