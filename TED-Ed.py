#-*- coding: cp949 -*-
import os
import urllib2
import codecs
from bs4 import BeautifulSoup

url = 'https://www.ted.com/watch/ted-ed'
html = urllib2.urlopen(url)
soup = BeautifulSoup(html, "lxml")
 
f = open(os.curdir + "/index.html", 'w')
f = codecs.open(os.curdir + "/ted-ed.html", "w", "utf-8")
div_main = soup.find("div", class_="pages-main")
u_div_main = unicode(str(div_main), "utf-8")
f.write(u_div_main)
f.close()

# divs = soup.prettify()