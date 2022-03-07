from util import *
import requests
from bs4 import BeautifulSoup
# from db_helper import *

@except_decorative
def download_single(_id, name):
	if os.path.isfile(name):
		return True
	real_url = f'http://music.163.com/song/media/outer/url?id={_id}.mp3'
	r = requests.get(real_url, headers={"Connection":"keep-alive",
"Pragma":"no-cache",
"Cache-Control":"no-cache",
"Upgrade-Insecure-Requests":"1",
"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.85 Safari/537.36",
"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
"Accept-Encoding":"gzip, deflate",
"Accept-Language":"zh-CN,zh;q=0.9,en;q=0.8"})
	if '404' in r.url:
		return False
	urlretrieve(r.url, name)

def main():
	text = get_txt_file_raw('file/wyy.html')
	soup = BeautifulSoup(text)
	item = soup.find('div', {'id':'auto-id-Bw27QfImkVbeqJHT'})
	items = item.find_all('div', {'class':'f-cb'})
	for item in items:
		title = item.b['title']
		_id = item.a['href'][9:]
		print(title, _id)
		file_name = f'mp3\天气之子\{title}.mp3'
		download_single(_id, file_name)
	
download_single(528303, '届かない気持ち（无法传达的心意）.mp3')
# main()