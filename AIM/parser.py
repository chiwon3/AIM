from __future__ import unicode_literals
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "AIM.settings")
import django
django.setup()
import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen
import time
import json


# def Webtoon():
#     naver_request = requests.get('http://comic.naver.com/webtoon/weekday.nhn')
#     naver_html = naver_request.text
#     naver_request.raise_for_status()
#     naver_soup = BeautifulSoup(naver_html, 'html.parser')

#     # naver_day = naver_soup.select('.col h4 span')
#     naver_webtoon = naver_soup.select('.col ul li')

#     # for day in naver_day:
#     #     print(day.string)
#     print(naver_webtoon)
#     naver_toon_title = []

#     # naver_toon_img = {}
#     # naver_toon_link = {}
#     # print(naver_webtoon)

#     # test =Webtoon.objects.all()
#     # print(test)

#     for toon in naver_webtoon:

#         link = ("http://comic.naver.com"+toon.a['href'])
#         Webtoon.objects.create(title=toon.img['title'] , img= toon.img['src'] , link=link )
#         toon_item = {
#             "title" : toon.img['title'],
#             "img" : toon.img['src'],
#             "link" : link
#         }
#         # print(toon.img['title'])
#         naver_toon_title.append(toon_item)

#         # naver_toon_title["title"] = toon.img['title']
#         # naver_toon_title["img"] = toon.img['src']
#         # naver_toon_title["link"] = ("http://comic.naver.com"+toon.a['href'])

#         # qs = Webtoon(title = toon.img['title'], img = toon.img['src'], link = ("http://comic.naver.com"+toon.a['href']))
#         # qs.save()
#     # print(naver_toon_title)
#     return naver_toon_title
    # return null



# if __name__ == '__main__':
#     data_dict = Webtoon()
#     for t, i, l in data_dict.items():
#         Webtoon(title=t, img=i, link=l,).save()

def daumwebtoon():
    daum_request = requests.get('http://webtoon.daum.net/data/pc/webtoon/list_serialized/')
    daum_mon_html = daum_request.text+"fri"
    daum_mon_soup = BeautifulSoup(urlopen('http://webtoon.daum.net/data/pc/webtoon/list_serialized/fri'), 'html.parser')
    # daum_mon_toon = daum_mon_soup.findChildren("ul")
    #find_all("a",{"class":"link_wt"})
    # daum_day = daum_list.find({"class":"btn_comm"})
    # print(daum_mon_list)
    # print(daum_mon_soup.data)
    tmp_json = json.loads(daum_mon_soup.text)
    # print(tmp_json)
    print(tmp_json.get('data')[0])
    
    print("#"*100)
    for i in tmp_json.get('data')[0]:
        print(i)
    # temp = daum_mon_list.find("li>a").text
    # for i in daum_mon_list.find("li>a").text:
        # print(i)
    # print(temp)
    # daum_mon_toon_list = []
    # for mon_toons in daum_mon_toon:
    #     print(mon_toons)
    #     link = "http://webtoon.daum.net/" + mon_toons.a['href']
    #     toon_list ={
    #         "title" : mon_toons.img['alt'],
    #         "img" : mon_toons.img['src'],
    #         "link" : link
    #     }
    #     daum_toon_title.append(toon_list)
    # print(daum_mon_toon_list)
    return tmp_json

if __name__ == '__main__':
    daumwebtoon()
