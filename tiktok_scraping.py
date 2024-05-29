# -*- coding: utf-8 -*-
"""
Created on Wed May 29 09:03:12 2024

@author: Micah Angelo Bacani
"""

import requests
from bs4 import BeautifulSoup as bs
from requests_html import HTMLSession

url = "https://www.tiktok.com/@bongbong.marcos"


session = HTMLSession()
page = session.get(url)
page.html.render()

soup = bs(page.html.html, 'html.parser')

name = soup.select("#main-content-others_homepage > div > div.css-1g04lal-DivShareLayoutHeader-StyledDivShareLayoutHeaderV2.enm41492 > h3 > div:nth-child(1) > strong")
#print (page.html.html)
print ((name[0]).get_text())