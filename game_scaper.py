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
games = tree.xpath('//a[@class="App-Teaser__link"]/text()')
print(games)