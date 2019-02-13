#-*- coding: utf-8 -*-

########################################################
#
# eguru 사이트 파싱을 통한 진격의 거인 다운로드
# OS: Windows
# python2.7
# contact: popjy0312@gmail.com
#
########################################################



from urllib2 import *
from bs4 import BeautifulSoup
import urllib
import re

SAVE_DIR = "D:\\movie\\진격의거인\\".decode('utf-8')

########################################################
#
# 
# 각 책 링크 파싱
# 
#
########################################################

base_url = "https://eguru.tumblr.com"

main = urlopen("https://eguru.tumblr.com/%EC%A7%84%EA%B2%A9%EC%9D%98-%EA%B1%B0%EC%9D%B8").read()		#진격의거인

bs = BeautifulSoup(main, 'html.parser')

body = bs.find('div', attrs={'class': 'body-text'})

book_links =  re.findall('href=\"(.*?)\" target', str(body))
#print links


########################################################
#
# watching url parsing done
#
# parsing image url start
#
########################################################

if not os.path.exists(SAVE_DIR):
    os.mkdir(SAVE_DIR)
os.chdir(SAVE_DIR)

for now_link in book_links:
	book_name = unquote(now_link.split('/')[-1])
	print book_name + " download start"
	if os.path.exists(book_name.decode('utf-8')):		#if already downloaded
		continue
	os.mkdir(book_name.decode('utf-8'))
	os.chdir(book_name.decode('utf-8'))
	_url = base_url + now_link
	# print _url

	_html = urlopen(_url).read()

	bs = BeautifulSoup(_html, 'html.parser')

	body = bs.find('div', attrs={'class': 'body-text'})

	#print body

	image_links =  re.findall(' src=\"(.*?\.jpg)\"', str(body))
	#print image_links

	for i in range(0,len(image_links)):
		print book_name + '_' + str(i) + " downloading"
		urllib.urlretrieve(image_links[i], book_name.decode('utf-8') + '_' + str(i) + '.jpg')
	os.chdir("..")