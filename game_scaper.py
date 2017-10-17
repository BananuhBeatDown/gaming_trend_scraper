#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 16 14:36:36 2017

@author: matthew_green
"""

from lxml import html
import requests

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
revenue = []
installs = []
free_rank = []
gross_rank = []
price = []

for i in range(1, 5):
    page = requests.get('https://thinkgaming.com/app-sales-data/?page={}'.format(i))
    tree = html.fromstring(page.content)
    
    # xpath to the game names
    games.extend(tree.xpath('//a[@class="App-Teaser__link"]/text()'))
    
    # xpath to the game publishers
    publishers.extend(tree.xpath('//td[@class="info table-data table-data-publisher"]/a/text()'))
    
    # xpath to the game's revenue
    revenue.extend(tree.xpath('//td[@class="table-data table-data-revenue"]/text()'))
    
    # xpath for the amount of installs per game    
    installs.extend(tree.xpath('//td[@class="table-data table-data-installs_new"]/text()'))
    
    # xoath for the free_rank(amount of installs) of the game  
    free_rank.extend(tree.xpath('//td[@class="info table-data table-data-free_rank"]/text() | \
                           //td[@class="info table-data table-data-free_rank table-data-free_rank_empty"]/text() | \
                           //td[@class="info table-data table-data-paid_rank"]/text()'))
    
    # xpath for the gross_rank of the game
    gross_rank.extend(tree.xpath('//td[@class="info top-grossing-rank"]/text()'))
    
    # xpath for the price of the game
    price.extend(tree.xpath('//td[@class="info table-data table-data-price"]/text()'))    

# clean the data   
revenue = clean_and_int(revenue)
installs = clean_and_int(installs)
free_rank = clean_and_int(free_rank)
gross_rank = clean_and_int(gross_rank)

# combine all the lists together
data_package = list(zip(games, publishers, revenue, installs, gross_rank, free_rank, price))

print(len(data_package))

# %%

