'''
Created on 2015. 11. 29.

@author: Kim
'''
#-*- coding: cp949 -*-
import urllib


from bs4 import BeautifulSoup


html = urllib.urlopen('http://comic.naver.com/webtoon/weekday.nhn')
soup = BeautifulSoup(html, "lxml")
titles = soup.find_all("a", "title")

print titles
'''  
for title in titles:
    print 'title:{0:10s} link:{1:20s}\n'.format(title['title'].encode('utf-8'), title['href'].encode('utf-8'))
'''