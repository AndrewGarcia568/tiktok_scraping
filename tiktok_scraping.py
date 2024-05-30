# -*- coding: utf-8 -*-
"""
Created on Wed May 29 09:03:12 2024

@author: Micah Angelo Bacani
"""

from bs4 import BeautifulSoup as bs
from requests_html import HTMLSession
import requests
import csv

url = "https://www.tiktok.com/@bongbong.marcos"
ajax_url = ["https://www.tiktok.com/api/post/item_list/?WebIdLastTime=1716944369&aid=1988&app_language=en&app_name=tiktok_web&browser_language=en-PH&browser_name=Mozilla&browser_online=true&browser_platform=Win32&browser_version=5.0%20%28Windows%20NT%2010.0%3B%20Win64%3B%20x64%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F125.0.0.0%20Safari%2F537.36&channel=tiktok_web&cookie_enabled=true&count=35&coverFormat=2&cursor=0&device_id=7374219795930072584&device_platform=web_pc&focus_state=true&from_page=user&history_len=1&is_fullscreen=false&is_page_visible=true&language=en&odinId=7374219707403994120&os=windows&priority_region=&referer=&region=PH&screen_height=1080&screen_width=1920&secUid=MS4wLjABAAAAwePzrs_LFD5wO3VGZlgOa4ARO7a6WAs9jJcqfrg3c37wcYLo8xgR13gPTb_lhPvQ&tz_name=Asia%2FManila&webcast_language=en&msToken=FhSl1ScDnuImeKWalt_4mek_LrFLAW8gojl_4kbOycyWCdpXRiAMqn6wWrkdCeNf-SddZMzE08QV5bvq4Iln5SaifIGsotTM1-iAjg3bppzHjaoAfNQtz6zm55hrooywlNVCVig4L7W2G9SC8Yc=&X-Bogus=DFSzswVOVlbANcK/tAr3Q41WyZJ/&_signature=_02B4Z6wo00001HLnbHgAAIDCk-ePe7MfIARy52jAAHrp77",
            "https://www.tiktok.com/api/post/item_list/?WebIdLastTime=1716944369&aid=1988&app_language=en&app_name=tiktok_web&browser_language=en-PH&browser_name=Mozilla&browser_online=true&browser_platform=Win32&browser_version=5.0%20%28Windows%20NT%2010.0%3B%20Win64%3B%20x64%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F125.0.0.0%20Safari%2F537.36&channel=tiktok_web&cookie_enabled=true&count=35&coverFormat=2&cursor=1711537004000&device_id=7374219795930072584&device_platform=web_pc&focus_state=true&from_page=user&history_len=1&is_fullscreen=false&is_page_visible=true&language=en&odinId=7374219707403994120&os=windows&priority_region=&referer=&region=PH&screen_height=1080&screen_width=1920&secUid=MS4wLjABAAAAwePzrs_LFD5wO3VGZlgOa4ARO7a6WAs9jJcqfrg3c37wcYLo8xgR13gPTb_lhPvQ&tz_name=Asia%2FManila&webcast_language=en&msToken=EYksx-07Fo0R9Y0Ekc0O_klnxREe1O3tO5YoIhOgWVMtvS3c9L2UlsmnmvqDVu1A_seQQzfZRrsdCkQPWRafwxLFiNuo-tU9QXahcest4dfHehPdolVSh46SAOgOGFsGjgIOupSgpsxlAeP4PkY=&X-Bogus=DFSzswVYHVvANeaotArnUo1WyZrg&_signature=_02B4Z6wo00001i4I5cQAAIDAzwgGxx.zTJouCOFAAO3o0d",
            "https://www.tiktok.com/api/post/item_list/?WebIdLastTime=1716944369&aid=1988&app_language=en&app_name=tiktok_web&browser_language=en-PH&browser_name=Mozilla&browser_online=true&browser_platform=Win32&browser_version=5.0%20%28Windows%20NT%2010.0%3B%20Win64%3B%20x64%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F125.0.0.0%20Safari%2F537.36&channel=tiktok_web&cookie_enabled=true&count=35&coverFormat=2&cursor=1703209214000&device_id=7374219795930072584&device_platform=web_pc&focus_state=true&from_page=user&history_len=1&is_fullscreen=false&is_page_visible=true&language=en&odinId=7374219707403994120&os=windows&priority_region=&referer=&region=PH&screen_height=1080&screen_width=1920&secUid=MS4wLjABAAAAwePzrs_LFD5wO3VGZlgOa4ARO7a6WAs9jJcqfrg3c37wcYLo8xgR13gPTb_lhPvQ&tz_name=Asia%2FManila&webcast_language=en&msToken=3x3nu9wX31tjSJd9p5n4l1WoggcdiBOIsC-Nkytsd68h2ujsOnZHJSnvQzmYubkf0pFjf5cCaLe214kHA5hVj-PAxYanhtkSV23aYJC5RxJUFZSWaDLQJg5hUnbyJQkKIQEIjDBO_QhIwOmcmSM=&X-Bogus=DFSzswVYhpiANeaotArnWo1WyZnH&_signature=_02B4Z6wo00001XOC44QAAIDDkoIAhOjYOHFzgucAADq8ef",
            "https://www.tiktok.com/api/post/item_list/?WebIdLastTime=1716944369&aid=1988&app_language=en&app_name=tiktok_web&browser_language=en-PH&browser_name=Mozilla&browser_online=true&browser_platform=Win32&browser_version=5.0%20%28Windows%20NT%2010.0%3B%20Win64%3B%20x64%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F125.0.0.0%20Safari%2F537.36&channel=tiktok_web&cookie_enabled=true&count=35&coverFormat=2&cursor=1655698145000&device_id=7374219795930072584&device_platform=web_pc&focus_state=true&from_page=user&history_len=1&is_fullscreen=false&is_page_visible=true&language=en&odinId=7374219707403994120&os=windows&priority_region=&referer=&region=PH&screen_height=1080&screen_width=1920&secUid=MS4wLjABAAAAwePzrs_LFD5wO3VGZlgOa4ARO7a6WAs9jJcqfrg3c37wcYLo8xgR13gPTb_lhPvQ&tz_name=Asia%2FManila&webcast_language=en&msToken=I44XV4gPH-opPj6Suye_RTDZpUzQU3fZ_lGGfjocmX4Wc06iK-mkTSqXrcYHHQy47JLm-ihJkAaqAx1ARfLIeYzsSBPVa09kwVkjXdMu5stdKt5Wvdd2aBzhbz6BS6_NncKoaaYSa0ILGLDT448=&X-Bogus=DFSzswVYvqhANeaotArn391WyZnv&_signature=_02B4Z6wo000014oIA4gAAIDBawjgi9xOYleKCAcAAITi43",
            "https://www.tiktok.com/api/post/item_list/?WebIdLastTime=1716944369&aid=1988&app_language=en&app_name=tiktok_web&browser_language=en-PH&browser_name=Mozilla&browser_online=true&browser_platform=Win32&browser_version=5.0%20%28Windows%20NT%2010.0%3B%20Win64%3B%20x64%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F125.0.0.0%20Safari%2F537.36&channel=tiktok_web&cookie_enabled=true&count=35&coverFormat=2&cursor=1629940213000&device_id=7374219795930072584&device_platform=web_pc&focus_state=true&from_page=user&history_len=1&is_fullscreen=false&is_page_visible=true&language=en&odinId=7374219707403994120&os=windows&priority_region=&referer=&region=PH&screen_height=1080&screen_width=1920&secUid=MS4wLjABAAAAwePzrs_LFD5wO3VGZlgOa4ARO7a6WAs9jJcqfrg3c37wcYLo8xgR13gPTb_lhPvQ&tz_name=Asia%2FManila&webcast_language=en&msToken=qCeDRYosBu2mMebCZHN6cItl5GcuCJtM8-ZuGjmxAdKQBj8-b0eyCbLWziMQBYqp9Dg0U5q-T2qlJ6Rm_MyEuAyaKVqFOc_FduiB4p9i4a-10pXUzOufY5UK-4OUTWJeK2iBDoZJAFHG-gn-d1c=&X-Bogus=DFSzswVYjWhANeaotArn341WyZnb&_signature=_02B4Z6wo00001CfNCsQAAIDCxs3pxQ3O18AnzQ5AAG-yde"
]
header_content = []
video_links = []
id_for_links = []

#creating html session to parse and load scripts
session = HTMLSession()
page = session.get(url)
page.html.render()

#initializing beautiful soup object
soup = bs(page.html.html, 'html.parser')

#extracting header info
head = soup.find("div", attrs = {"class" : "css-1g04lal-DivShareLayoutHeader-StyledDivShareLayoutHeaderV2 enm41492"})
bio = head.find("h2", attrs = {"data-e2e" : 'user-bio'})
link = head.find("a", attrs = {'data-e2e' : 'user-link'})
counts = head.h3.findAll("div")

#compiling header info in list
header_content.append(head.h1.get_text())
header_content.append(head.h2.get_text())
for i in counts:
    header_content.append(i.get_text())
header_content.append(bio.get_text())
header_content.append(link.get_text())
header_content.append(link['href'])

#closing html session
session.close()

#mimicking ajax requests to load videos
headers = {
    'Referer' : 'https://www.tiktok.com/@bongbong.marcos',
    'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36',
    'X-Kl-Ajax-Request' : 'Ajax_Request',
    'Cookie' : 'ttp=295vb5FcZdjQCRfk1CNh3z8rTKz; tt_chain_token=tvhPiKlw0GCMdJNeFdIleA==; tiktok_webapp_theme=light; odin_tt=4046b7b1d26a7a21691a64e1e48c55d5b0c9b6834b22c9ba5d86240512956c37c0478906d648534749be7c7a3d2611519d3458ed9d3dba4eacaf431862cc1b3fda117170f017010994be7c9e5dfef12b; passport_csrf_token=5a1d79b2180e7f45fe7001c62a757a8b; passport_csrf_token_default=5a1d79b2180e7f45fe7001c62a757a8b; perf_feed_cache={%22expireTimestamp%22:1717135200000%2C%22itemIds%22:[%227347290048968002834%22%2C%227372200034365951238%22]}; tt_csrf_token=DSwJTcai-oW7ypV-g78ydPNhVSwr4bTP-0MI; ak_bmsc=689A4F59C1A849F2746E68EAF1B1440F~000000000000000000000000000000~YAAQjb8CehrF37qPAQAAXtS+xxf+xJgXGTcscpFvbR3zbtRS28+JrAt4ecUJT88Ca1TImejvBrpUQWBtV9cI/2OATkZWqq2LrEKurDPZV1LRJbQ+hE6LM6GFUltVsLVP+CXErqwvb+NCYF4lnw/tUGiacKRZbFH0bkoqk4wh0Wo7lTZ66lGpnBFH8CBdDz6K2+iOfI9WDs+7+UkGjG2UI18Wrjv7k1GpAzMWekwKVBVipkEXd4prlQtM1IumZ6SFFE1UhYwTdL+8vrmcb6tk3G3qrEmO3WR9SVNTLCPct11fjsnpHtLG2ffFCHVokI7vaJaKvebixeM/00zL5IkfGnMGw71L0lzDqyleHDBdvd7heep1mI7aywjWUAKIUm/+B0wXdu7zspfoIdw=; msToken=VaqtPhaNBxniXsuPGNCFeUPa0cvHOVau-Ji5Q73lzgc4POS4jmp7Pxa52ANNhMgE5sJ56TwOvoMESQjmUeeStbwePvPfE_6QzxcX3YQFnh6xuHnAqxR3_kDa4Cw=; msToken=Oo4HSNQylX9_QlCNRWFkIIWUc52cvfSSdZ4Tah8vlmLVjgfdauRllVRIQ5N-xwLJDEIobSqSYcwnt1Dd-YyHJYr05du3wpAbzacuFMm79IUH6O4Z5GlKFrd1bbMWzd0UaOj1haZ-5h0ap0ALyPU=; bm_sv=9F7F8E8CE4E03AB378E938E1148B5CCF~YAAQjL8CevyTabSPAQAAwdoayBemyEx2/xNIvsW7B0M3tKnB6sBRTylRqeX9yHvakKuCTTV9OpMoWN4QTmtVYLLTMDTJnbp9oRXDZ3PhwwBBHdOfxTCtrE/fYnAvzLrXQD9XXfde+nHp5qSEh79d/gs5N4kDr2v/jpLHXltXug52Sh3rzePhydEXeKZhYW1OusbiA3ljHSpGyCsHNBqRi0HKdUwdAcrd24Qz4KZRMaGUrnb8C66IUwjDbaxyaAX2~1; ttwid=1%7CrW2of6oKjt5wjlZTaa868n4daZuS5r5AoMYOXEk09NM%7C1717049156%7C1ba88604f3fe6f313ddcd9fa7ef160aef6a5a24b60965f7be0fc3a5a21304c82'
}
for i in ajax_url:
    ajax_response = requests.get(i, headers = headers)
#parsing json response and getting ID of each video to build the links
    content = ajax_response.json()
    for i in content['itemList']:
        id_for_links.append(i['id'])

#video links is composed of the base url + /video/id
for i in id_for_links:
    link = url + "/video/" + i
    video_links.append(link)

#printing output
print ("Header info:")
for i in header_content:
    print (i)
print ("Video Links:")
for i in video_links:
    print (i)

#writing to csv
with open('scraped_data', 'w', encoding = 'UTF8') as f:
    writer = csv.writer(f)
    writer.writerow(header_content)
    writer.writerow(video_links)