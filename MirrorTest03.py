#-*- coding: cp949 -*-
import os
import urllib2
import codecs

from bs4 import BeautifulSoup



url = 'http://naver.com/'

#f = open(os.curdir + "/index.html", 'w')
f = codecs.open(os.curdir + "/index.html", "w", "utf-8")
html = urllib2.urlopen(url)
soup = BeautifulSoup(html, "lxml")
f.write(soup.prettify())
f.close()



#titles = soup.find_all("div", "mvp_block")
#print titles
#print(soup.prettify())
#print soup

