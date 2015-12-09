import os
import urllib2
import codecs
from bs4 import BeautifulSoup

def get_soup(_url):
	url = _url
	html = urllib2.urlopen(url)
	soup = BeautifulSoup(html, "lxml")
	return soup
# Main Page Parsing
soup = get_soup('https://www.ted.com/watch/ted-ed')
 
head = soup.find("head")
header = soup.find("header")
div_main = soup.find("div", class_="pages-main")

index = header.find("a", class_="g-logo-small banner__logo")
index['href'] = './index.html'

# Download images from div .pages-module
div_pages_module = soup.find("div", class_="pages-module")
div_pages_image = div_pages_module.find_all("div", class_="pages-carousel__image")
for div in div_pages_image:
	style = div['style']
	image_url = "http:" + div['style'][21:-2]
	image_file_name = image_url.split('/')[-1].split('?')[0]
	print image_file_name
	image_object = urllib2.urlopen(image_url)
	image_file = open(os.curdir + "/" + image_file_name, "wb")
	image_file.write(image_object.read())
	image_file.close()
	div['style'] = style.replace(style[:], "background-image:url(./" + image_file_name + ")")

videoLink = soup.find("div", class_="row-sm-4up")
videoHref = videoLink.find_all("a")
cnt = 1
for a in videoHref:
	if(cnt == 1 or cnt == 2):
		video1 = 'http://www.ted.com' + a['href']
		a['href'] = './video1.html'
	elif(cnt == 3 or cnt == 4):
		video2 = 'http://www.ted.com' + a['href']
		a['href'] = './video2.html' 
	elif(cnt == 5 or cnt == 6):
		video3 = 'http://www.ted.com' + a['href']
		a['href'] = './video3.html' 
	elif(cnt == 7 or cnt == 8):
		video4 = 'http://www.ted.com' + a['href']
		a['href'] = './video4.html'
	elif(cnt == 9 or cnt == 10):
		video5 = 'http://www.ted.com' + a['href']
		a['href'] = './video5.html'
	elif(cnt == 11 or cnt == 12):
		video6 = 'http://www.ted.com' + a['href']
		a['href'] = './video6.html'
	elif(cnt == 13 or cnt == 14):
		video7 = 'http://www.ted.com' + a['href']
		a['href'] = './video7.html'
	elif(cnt == 15 or cnt == 16):
		video8 = 'http://www.ted.com' + a['href']
		a['href'] = './video8.html'	
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

# Video Site
soupVideo1 = get_soup(video1)
soupVideo2 = get_soup(video2)
soupVideo3 = get_soup(video3)
soupVideo4 = get_soup(video4)
soupVideo5 = get_soup(video5)
soupVideo6 = get_soup(video6)
soupVideo7 = get_soup(video7)
soupVideo8 = get_soup(video8)
for i in range(1, 9):	
	f = codecs.open(os.curdir + "/video"+str(i)+".html", "w", "utf-8")
	if(i == 1):
		f.write(soupVideo1.prettify())
	elif(i == 2):
		f.write(soupVideo2.prettify())
	elif(i == 3):
		f.write(soupVideo3.prettify())
	elif(i == 4):
		f.write(soupVideo4.prettify())
	elif(i == 5):
		f.write(soupVideo5.prettify())
	elif(i == 6):
		f.write(soupVideo6.prettify())
	elif(i == 7):
		f.write(soupVideo7.prettify())
	elif(i == 8):
		f.write(soupVideo8.prettify())	
	f.close()


