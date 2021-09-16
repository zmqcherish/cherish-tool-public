import xlwt
from datetime import datetime
import pickle
from os import path
from util import *
wbk = xlwt.Workbook()

style_header = xlwt.easyxf("pattern: pattern solid, fore_color pale_blue; font: height 300; align: horiz center; borders : right 1, top 1, bottom 1")

style_default = xlwt.easyxf("pattern: pattern solid, fore_color white; font: height 250; align: horiz center; borders : right 1, top 1, bottom 1")

style_total = xlwt.easyxf("pattern: pattern solid, fore_color white; font: height 250, colour_index 2; align: horiz center; borders : right 1, top 1, bottom 1")

style_index = xlwt.easyxf("pattern: pattern solid, fore_color white; font: height 250; align: horiz center, vert center; borders : right 1, top 1, bottom 1")

style_addr = xlwt.easyxf("pattern: pattern solid, fore_color white; font: height 250; align: horiz left, vert center; borders : right 1, top 1, bottom 1")

good_names = ['[ 悬日 ] T-Shirt 4:43 黑色'] * 4 + ['[ 悬日 ] T-Shirt 4:43 白色'] * 4 + ['[ 悬日 ] T-Shirt 4:43 灰色'] * 4 + ['[ 善良的混蛋 ] 毛巾 5:45 ', '[ 未来 现在 过去 ] 节气历 5:07', '[ 对未来的慷慨 ] 原子笔 5:11 ', '[ 时间的尺 ] 沙漏 4:52 ', '[ 生活的载体 ] 机能小包 5:58 ', '田馥甄一一演唱会海报 ', '运费']
t_sizes = ['S', 'M', 'L', 'XL'] * 3
money_list = [220,] * 12 + [145, 145, 40, 170, 205, 50, 15] 

sheet = wbk.add_sheet('main', cell_overwrite_ok=True)


def pre_main():
	cmp_data = dict()
	data = dict()
	items = get_txt_file()
	# for item in items:
	# 	_, _, name, phone, address, *other  = item.split(',')
	# 	cmp_data = f'{name}{phone}{address}'
	# 	if phone in cmp_data:
	# 		pre_cmp_data = cmp_data[phone]
	# 		if pre_cmp_data != cmp_data:
	# 			print('error', pre_cmp_data, cmp_data)
	# 		pre_data = data[phone]

	# 	else:
	# 		cmp_data[phone] = cmp_data
	# 		data[phone] = item
	main(items)

def main(items):
	start_row = 1
	money_count_all_all = 0
	num = 1
	for item in items:
		good_count = 0
		_, _, name, phone, address, all_money, yunfei, all_money2, *goods  = item.split(',')
		money_count_all = 0
		if len(goods) != 18:
			print(item)
			continue
		goods.append('1')
		for i in range(len(goods)):
			good_num = int(goods[i])
			if not good_num:
				continue
			good_name = good_names[i]
			good_size = '-'
			if i < 12:
				good_size = t_sizes[i] + '号'
			money = '￥' + str(money_list[i])
			money_count = money_list[i] * good_num
			money_count_all += money_count
			row = start_row + good_count
			sheet.write(row, 1, good_name, style_default)
			sheet.write(row, 2, good_size, style_default)
			sheet.write(row, 3, money, style_default)
			sheet.write(row, 4, good_num, style_default)
			sheet.write(row, 5, f'￥{money_count}', style_default)
			good_count += 1
		money_count_all_all += money_count_all
		if int(all_money2) != money_count_all:
			print('------', item)
			return
		send_dist = f'{name} {address} {phone}'
		sheet.write(start_row + good_count, 5, f'￥{money_count_all}', style_default)
		sheet.write(start_row + good_count, 4, '匯款金額總計', style_total)
		sheet.write_merge(start_row, start_row + good_count - 1, 0, 0, num, style_index)
		sheet.write_merge(start_row, start_row + good_count - 1, 6, 6, send_dist, style_addr)
		start_row += good_count + 2
		num += 1
	print('----------', money_count_all_all)


def write_header():
	header = ['序号', '产品名称', '规格', '售價', '发货数量', '金額小計', '收货人 & 地址 &電話']
	[sheet.write(0, i, header[i], style_header) for i in range(len(header))]

def save_file():
	wbk.save('0831.xls')

sheet.col(0).width = 256 * 10
sheet.col(1).width = 256 * 40
sheet.col(2).width = 256 * 12
sheet.col(3).width = 256 * 12
sheet.col(4).width = 256 * 12
sheet.col(5).width = 256 * 12
sheet.col(6).width = 256 * 100
write_header()
pre_main()
save_file()