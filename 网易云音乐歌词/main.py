import json
import requests
from selenium import webdriver

# 教程 http://get.ftqq.com/7430.get
lrc_url = 'http://music.163.com/api/song/lyric?os=pc&id={}&lv=-1&kv=-1&tv=-1'
chrome_path = 'chromedriver.exe'

id_list = []


def get_ids():
    album_id = [29447, 29443, 2704008, 34746074, 35181017, 38045107, 3190030, 2948183]
    # album_id = [29447]
    for aid in album_id:
        driver = webdriver.Chrome(chrome_path)
        # aid = 29443
        driver.get('http://music.163.com/#/album?id={}'.format(aid))
        frame = driver.find_element_by_tag_name('iframe')
        driver.switch_to.frame(frame)
        songs = driver.find_element_by_tag_name('tbody').find_elements_by_xpath('//span[@class="txt"]/a')

        for song in songs:
            song_id = song.get_attribute('href')
            # song.get_attribute('text')
            id_list.append(song_id[song_id.find('id=') + 3:])
        driver.quit()
        # driver.switch_to.parent_frame()
        # break


get_ids()
for sid in id_list:
    res = json.loads(requests.get(lrc_url.format(sid)).text)
    lrc = res['lrc']['lyric']
    # res = json.loads(requests.get('http://music.163.com/api/song/detail/?id={}&ids=%5B{}%5D'.format(296871, 296871)).text)
    # name = res['songs'][0]['name']
    with open('all.txt', 'a', encoding='utf8') as f:
        f.write(lrc)
    a=1



