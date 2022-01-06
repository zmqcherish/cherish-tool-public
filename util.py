import sys
import os
import requests
import logging
import json
import re
import shutil
from dateutil import parser
from time import sleep
from datetime import datetime, timedelta
from urllib.request import urlretrieve
import pandas as pd
# import numpy as np

proxies={
	'http':'http://127.0.0.1:1080',
	'https':'https://127.0.0.1:1080'
}

def get_today_time():
	return get_time('%Y%m%d')


def get_time(fmt='%Y-%m-%d %H:%M:%S'):
	return datetime.now().strftime(fmt)


def get_csv_data(file_path):
	df = pd.read_csv(file_path, encoding='gb18030')
	return df

def except_decorative(func):
	def decorator(*args, **keyargs):
		try:
			return func(*args, **keyargs)
		except Exception as e:
			logging.error(f'handle {func.__name__} error: {e}')
	return decorator


def get_txt_file(file_path='1.txt'):
	content = ''
	with open(file_path, encoding='utf8') as txt_file:
		content = txt_file.readlines()
	return [c.strip('\n') for c in content]


def get_txt_file_raw(file_path='1.txt'):
	content = ''
	with open(file_path, encoding='utf8') as txt_file:
		content = txt_file.read()
	return content


def append_txt_file(file_path, save_item, end='\n'):
	with open(file_path, 'a', encoding='utf-8') as txt_file:
		txt_file.write(save_item + end)

def get_json_file(file_path):
	with open(file_path, 'r', encoding='utf-8') as json_file:
		return json.load(json_file)


def append_csv_file(file_path, save_item, end='\n'):
	with open(file_path, 'a', encoding='utf-8-sig') as txt_file:
		txt_file.write(save_item + end)

def convert_str2date(t):
	return parser.parse(t)

@except_decorative
def get_xlsx_data(file_path, col, start_row, end_row, sheet_index=0):
	data = pd.read_excel(file_path, sheet_name=sheet_index, usecols=col, skiprows=start_row - 2, nrows=end_row - start_row + 1)
	return data

def get_province_data():
	data = get_json_file('citys.json')
	return [item['name'].replace('省', '').replace('市', '') for item in data['data']]

def get_path_size(dir):
	size = 0
	for root, dirs, files in os.walk(dir):
		size += sum([os.path.getsize(os.path.join(root, name)) for name in files])
	return size

def create_folder(path):
	if os.path.exists(path):
		return
	os.mkdir(path)


def get_file_suffix(path):
	return os.path.splitext(path)[-1]