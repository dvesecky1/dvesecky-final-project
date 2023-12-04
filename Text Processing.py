# -*- coding: utf-8 -*-
"""
Created on Thu Nov 30 14:56:31 2023

@author: dv987
"""

import os
import fitz
from wordcloud import WordCloud
import matplotlib.pyplot as plt

BASE_PATH=r'c:\Users\dv987\Documents\GitHub\dvesecky-final-project\Articles'

#Create a list containing the text of each article
def create_list():
    dates = ['January 2023', 'February 2023', 'March 2023', 'April 2023', 'May 2023', 'June 2023',
             'July 2023', 'August 2023', 'September 2023', 'October 2023', 'November 2023', 'December 2023']
    counter=0
    articles=['','','','','','','','','','','','']
    for date in dates:
        doc = fitz.open(os.path.join(BASE_PATH, date+'.pdf'))
        text = ""
        for page in doc:
           text+=page.get_text()
           articles[counter]=text
        counter +=1
    return articles
articles=create_list()

#Create and plot a wordcloud for each article
def clouds(texts):    
    wc=WordCloud()
    for x in texts:
        wordcloud=wc.generate(x)
        fig, ax=plt.subplots()
        ax.imshow(wordcloud, interpolation='bilinear')
        ax.axis=('off')
        plt.show()
clouds(articles)

#Create and plot a wordcloud for all articles together
def one_cloud(texts):
    total=""
    for x in articles:
        total += x
    wc=WordCloud()
    stop_words = list(wc.stopwords)
    custom_stop_words = ['url', 'https', 'PM', '2F', '3A', 'S', 'U']
    stop_words = set(stop_words + custom_stop_words)
    wordcloud=WordCloud(stopwords=stop_words).generate(total)
    fig, ax=plt.subplots()
    ax.imshow(wordcloud, interpolation='bilinear')
    ax.axis=('off')
    plt.show()
one_cloud(articles)