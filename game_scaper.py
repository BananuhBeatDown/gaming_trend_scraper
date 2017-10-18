#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 16 14:36:36 2017

@author: matthew_green
"""

import requests
from lxml import html
import pandas as pd
import os
import datetime

# helper function that cleans common characters from numbers
# and changes them to int class
def clean_and_int(data):
    for i in range(len(data)):
        if data[i] == '-':
            data[i] = 0
        else:
            data[i] = data[i].translate({ord(c): None for c in '$,'})
            data[i] = int(data[i])
    return data

games = []
publishers = []
revenues = []
installs = []
free_ranks = []
gross_ranks = []
prices = []

for i in range(1, 5):
    page = requests.get('https://thinkgaming.com/app-sales-data/?page={}'.format(i))
    tree = html.fromstring(page.content)
    
    # xpath to the game names
    games.extend(tree.xpath('//a[@class="App-Teaser__link"]/text()'))
    
    # xpath to the game publishers
    publishers.extend(tree.xpath('//td[@class="info table-data table-data-publisher"]/a/text()'))
    
    # xpath to the game's revenue
    revenues.extend(tree.xpath('//td[@class="table-data table-data-revenue"]/text()'))
    
    # xpath for the amount of installs per game    
    installs.extend(tree.xpath('//td[@class="table-data table-data-installs_new"]/text()'))
    
    # xoath for the free_rank(amount of installs) of the game  
    free_ranks.extend(tree.xpath('//td[@class="info table-data table-data-free_rank"]/text() | \
                           //td[@class="info table-data table-data-free_rank table-data-free_rank_empty"]/text() | \
                           //td[@class="info table-data table-data-paid_rank"]/text()'))
    
    # xpath for the gross_rank of the game
    gross_ranks.extend(tree.xpath('//td[@class="info top-grossing-rank"]/text()'))
    
    # xpath for the price of the game
    prices.extend(tree.xpath('//td[@class="info table-data table-data-price"]/text()'))    

# clean the data   
revenues = clean_and_int(revenues)
installs = clean_and_int(installs)
free_ranks = clean_and_int(free_ranks)
gross_ranks = clean_and_int(gross_ranks)

# zip the lists into a total dataset
dataset = list(zip(games, publishers, revenues, installs, gross_ranks, free_ranks, prices))

#
frame = pd.DataFrame(dataset, columns=['game', 'publisher', 'revenue', 'installs', 'gross_rank', 'free_rank', 'price'])

frame.index = range(1, 201)

frame.loc[:, 'date'] = datetime.date.today()

# create a new folder if needed
if not os.path.exists('pickles'):
    os.makedirs('pickles')

# save each day as a different pickle file
now = datetime.datetime.now()
pickle_file = '/Users/matthew_green/Desktop/version_control/gaming_trend_scraper/pickles/{}_{}_{}.pickle'.format(now.month, now.day, now.year)

frame.to_pickle(pickle_file)

# %%

