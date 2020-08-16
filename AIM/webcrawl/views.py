from django.shortcuts import render
from .models import NaverWebtoon
# Create your views here.
import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "AIM.settings")
import time
import json

def save_webtoon_data(request):
    naver_request = requests.get('http://comic.naver.com/webtoon/weekday.nhn')
    naver_html = naver_request.text
    naver_request.raise_for_status()
    naver_soup = BeautifulSoup(naver_html, 'html.parser')
    naver_webtoon = naver_soup.select('.col ul li')

    # naver_toon_title = []

    cnt = 0
    for toon in naver_webtoon:
        cnt += 1
        link = ("http://comic.naver.com"+toon.a['href'])
        NaverWebtoon.objects.create(title=toon.img['title'] , img= toon.img['src'] , link=link )
        print(f"{cnt}번째 데이터 저장완료")


def save_daum_webtoon_data(request):
    # daum_request = requests.get('http://webtoon.daum.net/data/pc/webtoon/list_serialized/')
    # daum_mon_html = daum_request.text+"fri"
    daum_mon_soup = BeautifulSoup(urlopen('http://webtoon.daum.net/data/pc/webtoon/list_serialized/mon'), 'html.parser')
    tmp_json = json.loads(daum_mon_soup.text)
    tmp_items = []
    tmp_items = tmp_json.get('data')
    print(tmp_items[0])
    # for i in tmp_json.get('data'):
    #     print(i)

if __name__ == '__main__':
    save_daum_webtoon_data()