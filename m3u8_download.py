import m3u8
from util import *

def pre_handle_file(in_path, out_path, prefix):
	data = get_txt_file(in_path)
	for d in data:
		if '.ts' in d:
			d = prefix + d
			append_txt_file(out_path, d)

# def merge_file(segs, base_path):
# # 合并ts片段，存为与文件夹同名的ts文件
# 	print('开始合并文件:')
# 	fn = '1.mp4'
# 	with open(fn, 'wb') as f:
# 		for sm in segs:
# 			# file_path = os.path.join(directory, f'{n}.ts')
# 			with open(base_path + sm.uri, 'rb') as g:
# 				f.write(g.read())
# 	print('合并文件完毕。。。')

def merge_file(m3u8_file, output_name):
	cmd = f'ffmpeg -allowed_extensions ALL -i {m3u8_file} -c copy {output_name}'
	os.system(cmd)

source_file = 'file/1.m3u8'
output_file = 'file/index.m3u8'
desc_file = '1.mp4'
base_path = 'm3u8f/'
base_uri = 'https://1252524126.vod2.myqcloud.com/2919df88vodtranscq1252524126/7ad2c5ff3701925924054622328/'

# def download_single(url):
# 	pass


def download_seqments(seq):
	print('开始下载 ts列表...')
	for sm in seq:
		local_path = base_path + sm.uri
		download_path = base_uri + sm.uri
		urlretrieve(download_path, local_path)
		sm.uri = local_path


m = m3u8.load(source_file)
# for i, pl in enumerate(m.playlists):
# 	print(f"{i}:{pl.stream_info}")

# pl = m.playlists[0]
# m2 = m3u8.load(pl.absolute_uri)

download_seqments(m.segments)
m.dump(output_file)
merge_file(output_file, desc_file)
