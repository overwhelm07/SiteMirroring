#-*- coding: cp949 -*-
import os
import urllib2
import codecs
from bs4 import BeautifulSoup

url = 'https://www.ted.com/watch/ted-ed'
html = urllib2.urlopen(url)
soup = BeautifulSoup(html, "lxml")
 
head = soup.find("head")
header = soup.find("header")
div_main = soup.find("div", class_="pages-main")
u_head = unicode(str(head), "utf-8")
u_header = unicode(str(header), "utf-8")
u_div_main = unicode(str(div_main), "utf-8")
f = open(os.curdir + "/index.html", 'w')
f = codecs.open(os.curdir + "/ted-ed.html", "w", "utf-8")
f.write(u"<html>\n")
f.write(u_head)
f.write(u"\n")
f.write(u_header)
f.write(u"\n")
f.write(u"<body>\n")
f.write(u_div_main)
f.write(u"\n")
f.write(u"</body>\n")
f.write(u"</html>\n")
f.close()

# divs = soup.prettify()