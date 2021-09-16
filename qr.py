import zxing
import requests
import os
import re
import json
from time import time, sleep
import urllib.parse as urlparse
from bs4 import BeautifulSoup
from urllib.request import urlretrieve

qr_reader = zxing.BarCodeReader()
phone = '13718595330'

def download(src):
	if not src:
		return
	file_name = f'temp\{time()}.jpg'
	if src[:2] == '//':
		src = 'http:' + src
	urlretrieve(src, file_name)

def get_qr(f):
	bar_code = qr_reader.decode(f)
	if not bar_code:
		return
	return bar_code.parsed


def get_imgs(url):
	a = requests.get(url)
	soup = BeautifulSoup(a.text)

	for img in soup.find_all('img'):        #获取网页中所有图片链接
		attrs = img.attrs
		src = attrs.get('src', None) or attrs.get('data-src', None)
		download(src)


def handle_qr(url):
	if not url or url.find('diditaxi') == -1:
		return
	# print(url)
	parsed = urlparse.urlparse(url)
	return urlparse.parse_qs(parsed.query)['g_channel'][0]


def get_last_url(url):
	a = requests.get(url)
	soup = BeautifulSoup(a.text)
	the_script = None
	for script in soup.find_all('script'):
		if script.text.find('didiActivityData') > -1:
			the_script = script.text
			break
	if the_script:
		match = re.match('.*?(\{.*\}).*Omega.*', the_script, re.S)
		if match:
			url = f"https:{json.loads(match.group(1))['open_url']}&phone=%2B86{phone}&lang=zh-CN"
			return url


def get_gift(channel, url):
	headers = {
		'accept': "application/json",
		'referer': f"https://gsactivity.diditaxi.com.cn/gulfstream/activity/v2/giftpackage/index?g_channel={channel}&from=singlemessage",
		'x-requested-with': "XMLHttpRequest",
		'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36"
    }
	res = requests.get(url, headers=headers).json()
	if res.get('errno', -1) in [6, 7]:
		print(res['errmsg'])
	else:
		print(res)


if __name__ == "__main__":
	url = 'https://mp.weixin.qq.com/s?__biz=MzAwNDIyOTg1NA==&mid=2650564766&idx=1&sn=21a4a825b1d53e847c95175b4841df55&chksm=8327d72fb4505e391f72d928a1b4a09e21f7cc82d2d5734dbb1a575cd855550e629395a79a28&scene=0&xtrack=1&key=9ae2f418e0a2e110c9a84d9a7c2cea7e417fd8dc9581a3fa0874002524ebb66ae701df73c5d91c9bfee81eb07426d23e7cefcaf7281a22f0d88a2962513f0bd82c60a9c493eb6aaebfc710ece7dd591d&ascene=1&uin=MTM3MDUzNzg0Mg%3D%3D&devicetype=Windows+10&version=62060739&lang=zh_CN&pass_ticket=Un%2FXnCEze%2BKXIOEYiT%2BuM%2FHtAYWBQXta5eBZydjGNQXkNjp4TNOnxslKtNOMGB7t'
	get_imgs(url)
	files = os.listdir('temp')
	for f in files:
		url = get_qr(f'temp//{f}')
		channel = handle_qr(url)
		if not channel:
			continue
		url = get_last_url(url)
		if url:
			get_gift(channel, url)
			sleep(1)


