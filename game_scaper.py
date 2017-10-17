#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 16 14:36:36 2017

@author: matthew_green
"""

from lxml import html
import requests

page = requests.get('https://thinkgaming.com/app-sales-data/top-free-games/?page=1/.html')
tree = html.fromstring(page.content)

# xpath to the game names
games = tree.xpath('//a[@class="App-Teaser__link"]/text()')

# xpath to the game publishers
publishers = tree.xpath('//td[@class="info table-data table-data-publisher"]/a/text()')

# xpath to the game's revenue
revenue = tree.xpath('//td[@class="table-data table-data-revenue"]/text()')
# clean the revenue data of non-digit characters and change to int type
for i in range(len(revenue)):
    revenue[i] = revenue[i].translate({ord(c): None for c in '$,'})
    revenue[i] = int(revenue[i])

# xpath for the amount of installs per game    
installs = tree.xpath('//td[@class="table-data table-data-installs_new"]/text()')
# clean the installs data of non-digit characters and change to int type
for i in range(len(installs)):
    installs[i] = installs[i].replace(',', '')
    installs[i] = int(installs[i])

# %%

