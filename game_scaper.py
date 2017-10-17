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

page = requests.get('https://thinkgaming.com/app-sales-data/?page=1/.html')
tree = html.fromstring(page.content)

# xpath to the game names
games = tree.xpath('//a[@class="App-Teaser__link"]/text()')

# xpath to the game publishers
publishers = tree.xpath('//td[@class="info table-data table-data-publisher"]/a/text()')

# xpath to the game's revenue
revenue = tree.xpath('//td[@class="table-data table-data-revenue"]/text()')
revenue = clean_and_int(revenue)

# xpath for the amount of installs per game    
installs = tree.xpath('//td[@class="table-data table-data-installs_new"]/text()')
installs = clean_and_int(installs)

# xoath for the free_rank(amount of installs) of the game  
free_rank = tree.xpath('//td[@class="info table-data table-data-free_rank"]/text() | \
                       //td[@class="info table-data table-data-free_rank table-data-free_rank_empty"]/text()')
free_rank = clean_and_int(free_rank)

# xpath for the gross_rank of the game
gross_rank = tree.xpath('//td[@class="info top-grossing-rank"]/text()')
gross_rank = clean_and_int(gross_rank)

package = list(zip(games, publishers, revenue, installs, gross_rank, free_rank))

print(package)
# %%

