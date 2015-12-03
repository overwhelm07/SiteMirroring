import os
import urllib2
import codecs
from bs4 import BeautifulSoup

def get_soup(_url):
	url = _url
	html = urllib2.urlopen(url)
	soup = BeautifulSoup(html, "lxml")
	return soup

soup = get_soup('https://www.ted.com/watch/ted-ed')
 
head = soup.find("head")
header = soup.find("header")
div_main = soup.find("div", class_="pages-main")

index = header.find("a", class_="g-logo-small banner__logo")
index['href'] = './index.html'

videoLink = soup.find("div", class_="row-sm-4up")
videoHref = videoLink.find_all("a")
cnt = 1
for a in videoHref:
	if(cnt == 1 or cnt == 2):
		a['href'] = './video1'
	elif(cnt == 3 or cnt == 4):
		a['href'] = './video2' 
	elif(cnt == 5 or cnt == 6):
		a['href'] = './video3' 
	elif(cnt == 7 or cnt == 8):
		a['href'] = './video4'
	elif(cnt == 9 or cnt == 10):
		a['href'] = './video5'
	elif(cnt == 11 or cnt == 12):
		a['href'] = './video6'
	elif(cnt == 13 or cnt == 14):
		a['href'] = './video7'
	elif(cnt == 15 or cnt == 16):
		a['href'] = './video8'	
	cnt += 1	
	# print a['href'] 


for a in header.find_all("a", class_="nav__link"):
	a.extract()
for input_header in header.find_all("input"):
	input_header.extract()
for a_banner__account__link in header.find_all("a", class_="banner__account__link"):
	a_banner__account__link.extract()

u_head = unicode(str(head), "utf-8")
u_header = unicode(str(header), "utf-8")
u_div_main = unicode(str(div_main), "utf-8")

f = codecs.open(os.curdir + "/index.html", "w", "utf-8")
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
