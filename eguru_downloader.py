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

SAVE_DIR = "D:\\영화,만화,드라마,애니\\진격의거인_만화\\".decode('utf-8')

########################################################
#
# 
# 각 책 링크 파싱
# 
#
########################################################

base_url = "https://eguru.tumblr.com"

main = urlopen("https://eguru.tumblr.com/shingeki-no-kyojin").read()		#진격의거인

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
	if os.path.exists(book_name.decode('utf-8')):		# if already downloaded
		continue										# 폴더 존재하면 이미 다운로드한것으로 간주하고 스킵시켰음.
	os.mkdir(book_name.decode('utf-8'))					# 책이름으로 폴더 생성
	os.chdir(book_name.decode('utf-8'))
	_url = base_url + now_link
	# print _url

	_html = urlopen(_url).read()

	bs = BeautifulSoup(_html, 'html.parser')

	body = bs.find('div', attrs={'class': 'body-text'})

	#print body

	image_links =  re.findall(' src=\"(.*?\....)\"', str(body))
	#print image_links

	for i in range(0,len(image_links)):
		print book_name + '_' + str(i) + " downloading"
		urllib.urlretrieve(image_links[i], book_name.decode('utf-8') + '_' + str(i) + '.' + image_links[i].split('.')[-1])	
			# 저장 파일명 예시: 진격의-거인-1권_0.jpg, 진격의-거인-1권_1.jpg, ...
			# 다운링크 마지막 파일포맷(.jpg, .png 등 포함 저장)

	os.chdir("..")