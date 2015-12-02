# -*- coding: cp949 -*-
import os
import urllib2
import codecs
from bs4 import BeautifulSoup


for page in range(1, 10):
        url = "http://comic.naver.com/webtoon/list.nhn?titleId=20853&weekday=fri&page=" + str(page)
        num = ['1', '2', '3']
        for n in num:
            # Create URL
            URL = url + n
            # Parse the page using BeautifulSoup
            page = urllib2.urlopen(URL)
            soup = BeautifulSoup(page, "lxml")
            #f = open(os.curdir + "/index" + n + ".html", 'w')
            f = codecs.open(os.curdir + "/index" + n + ".html", "w", "utf-8")    
            f.write(soup.prettify())
            f.close()