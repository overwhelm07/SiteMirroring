import os
import urllib2
import codecs
from bs4 import BeautifulSoup

# Get soup object from html page
def get_soup(_url):
	url = _url
	html = urllib2.urlopen(url)
	soup = BeautifulSoup(html, "lxml")
	return soup

# Extract header elements except logo
def extract_header(_header):
	for a in _header.find_all("a", class_="nav__link"):
		a.extract()
	for input_header in _header.find_all("input"):
		input_header.extract()
	for a_banner__account__link in _header.find_all("a", class_="banner__account__link"):
		a_banner__account__link.extract()

# Remove contents not related to the video
def prettify_video_soup(soupVideo):
	div_talk_section = soupVideo.find_all("div", class_="talk-section")
	a_talk_subsection = soupVideo.find("div", class_="talk-subsection").find_all("a")
	for div_video in div_talk_section:
		div_video.extract()
	for a_talk in a_talk_subsection:
		a_talk['href'] = "https://www.ted.com" + a_talk['href']

	extract_header(soupVideo.find("header"))
	soupVideo.find("footer").extract()
	soupVideo.find("a", class_="player-hero__teaser").extract()
	speaker = soupVideo.find("a", class_="talk-speaker__image")
	speaker_name = soupVideo.find("a", class_="talk-speaker__link")
	speaker['href'] = speaker_name['href'] = "https://www.ted.com" + speaker['href']

# Main Page Parsing
soup = get_soup('https://www.ted.com/watch/ted-ed')

head = soup.find("head")
header = soup.find("header")
div_main = soup.find("div", class_="pages-main")

index = header.find("a", class_="g-logo-small banner__logo")
index['href'] = './index.html'

extract_header(header)
soup.find("footer").extract()
a_copy = soup.find("div", class_="copy").p.a.extract()
a_pages_link = soup.find_all("a", class_="pages-featured-link")[1]
a_pages_link['href'] = "https://www.ted.com" + a_pages_link['href']

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

f = codecs.open(os.curdir + "/index.html", "w", "utf-8")
f.write(soup.prettify())
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
		prettify_video_soup(soupVideo1)
		f.write(soupVideo1.prettify())
	elif(i == 2):
		prettify_video_soup(soupVideo2)
		f.write(soupVideo2.prettify())
	elif(i == 3):
		prettify_video_soup(soupVideo3)
		f.write(soupVideo3.prettify())
	elif(i == 4):
		prettify_video_soup(soupVideo4)
		f.write(soupVideo4.prettify())
	elif(i == 5):
		prettify_video_soup(soupVideo5)
		f.write(soupVideo5.prettify())
	elif(i == 6):
		prettify_video_soup(soupVideo6)
	elif(i == 7):
		prettify_video_soup(soupVideo7)
		f.write(soupVideo7.prettify())
	elif(i == 8):
		prettify_video_soup(soupVideo8)
		f.write(soupVideo8.prettify())	
	f.close()