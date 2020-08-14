from __future__ import unicode_literals
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "AIM.settings")
import django
django.setup()
import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen
from webcrawl.models import naverwebtoon

def naverwebtoon():
    naver_request = requests.get('http://comic.naver.com/webtoon/weekday.nhn')
    naver_html = naver_request.text
    naver_soup = BeautifulSoup(naver_html, 'html.parser')

    naver_day = naver_soup.select('.col h4 span')
    naver_webtoon = naver_soup.select('.col ul li')

    for day in naver_day:
        print(day.string)

    naver_toon_title = {}
    naver_toon_img = {}
    naver_toon_link = {}


    for toon in naver_webtoon:
        naver_toon_title[toon.text] = toon.img['title']
        naver_toon_img[toon.text] = toon.img['src']
        naver_toon_link[toon.text] = ("http://comic.naver.com"+toon.a['href'])

        # print(toon.img['title']),
        # print(toon.img['src']),
        # print("http://comic.naver.com"+toon.a['href']),
    print(naver_toon_img)

    return naver_toon_title
    return naver_toon_img
    return naver_toon_link
    
if __name__ == '__main__':
    data_dict = naverwebtoon()
    for t, i, l in data_dict.items():
        naverwebtoon(title=t, img=i, link=l).save()

# daum_mon_html = requests.get('http://webtoon.daum.net/#day=mon&tab=day')
# daum_mon_soup = BeautifulSoup(daum_mon_html.text, 'html.parser')
# daum_mon_list = daum_mon_soup.find_all("ul",{"class":"list_wt"})
# daum_mon_toon = daum_mon_soup.findChildren("ul")
# #find_all("a",{"class":"link_wt"})
# # daum_day = daum_list.find({"class":"btn_comm"})

# # print(daum_mon_toon)

# daum_mon_toon_list = []

# for mon_toons in daum_mon_toon:
#     print(mon_toons)
    # daum_mon_toon_list.append(
    #     mon_toons.img['alt'],
    #     mon_toons.img['src'],
    #     "http://webtoon.daum.net/" + mon_toons.a['href']
    # )

# print(daum_mon_toon_list)