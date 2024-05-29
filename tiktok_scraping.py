# -*- coding: utf-8 -*-
"""
Created on Wed May 29 09:03:12 2024

@author: Micah Angelo Bacani
"""

from bs4 import BeautifulSoup as bs
from requests_html import HTMLSession

url = "https://www.tiktok.com/@bongbong.marcos"

header_content = []
video_links = []

#creating html session to parse and load scripts
session = HTMLSession()
page = session.get(url)
page.html.render(sleep = 25)

#initializing beautiful soup object
soup = bs(page.html.html, 'html.parser')

#extracting header info
head = soup.find("div", attrs = {"class" : "css-1g04lal-DivShareLayoutHeader-StyledDivShareLayoutHeaderV2 enm41492"})
bio = head.find("h2", attrs = {"data-e2e" : 'user-bio'})
link = head.find("a", attrs = {'data-e2e' : 'user-link'})

#compiling header info in list
header_content.append(head.h1.get_text())
header_content.append(head.h2.get_text())
header_content.append(head.h3.get_text())
header_content.append(bio.get_text())
header_content.append(link.get_text())
header_content.append(link['href'])

#extracting video links
body = soup.find('#main-content-others_homepage > div > div.css-833rgq-DivShareLayoutMain.ee7zj8d4 > div.css-1qb12g8-DivThreeColumnContainer.eegew6e2 > div > div:nth-child(1)')
print (body)
print (page.html.absolute_links)
test = soup.find("div", attrs = {'class' : 'css-833rgq-DivShareLayoutMain ee7zj8d4'})
#print (test)

print ("Header info:")
for i in header_content:
    print (i)
"""
print("Video links:")
for i in video_links:
    print (i)



pretty_data = soup.prettify()
with open ('whole_page.txt', 'w') as f:
    f.write(pretty_data)
"""