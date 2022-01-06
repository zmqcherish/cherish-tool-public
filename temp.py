import pyautogui
from pynput.mouse import Listener
from threading import Thread
from util import *
click_pos = {
	'enable': False,
	'x': 0,
	'y': 0
}

def on_click(x, y, button, pressed):  # 监听鼠标点击
	# print('{0} at {1}'.format('Pressed' if pressed else 'Released', (x, y)))
	if pressed and click_pos['enable']:
		click_pos['x'] = x
		click_pos['y'] = y
		click_pos['enable'] = False
	# else:  # 如果没有按压就结束程序（即，单击一下鼠标会结束程序）
		# Stop listener
		# return False

def move_and_click(x, y):
	pyautogui.moveTo(x, y)
	pyautogui.click()

def move_and_right_click(x, y):
	pyautogui.moveTo(x, y)
	pyautogui.rightClick()


def get_click():
	with Listener(on_click=on_click) as listener:
		listener.join()

if __name__ == "__main__":
	t1 = Thread(target=get_click)
	t1.start()

	print('请点击第一个置顶对话')
	# get_click()
	click_pos['enable'] = True
	while True:
		sleep(1)
		if click_pos['enable']:
			continue
		break
	for i in range(4):
		move_and_right_click(click_pos['x'], click_pos['y'])
		sleep(1)
		move_and_click(click_pos['x'] + 5, click_pos['y'] + 5)
		sleep(4)