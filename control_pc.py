
import pyautogui
import pywinauto
from pywinauto.application import Application
from pywinauto.win32functions import SetFocus
from pywinauto import mouse
from pywinauto.keyboard import send_keys
from pynput.mouse import Listener
from time import sleep

def a():
	app_url = 'C:/Users/cherishzhang/AppData/Local/JpegminiPro3/JPEGminiPro.exe'
	app = Application(backend="win32")
	# app.start(app_url)
	# app.connect(path=app_url)
	app.connect(process=39564)
	dlg = app.windows(title='JPEGmini Pro')
	dlg = dlg[0]
	# dlg.type_keys('^o')
	# dlg_open = app['打开']
	# dlg_open.Edit.set_text('D:/download/test')
	# dlg_open['打开'].click()
	print(dlg)

def on_click(x, y, button, pressed):  # 监听鼠标点击
	print('{0} at {1}'.format('Pressed' if pressed else 'Released', (x, y)))
	if not pressed:  # 如果没有按压就结束程序（即，单击一下鼠标会结束程序）
		# Stop listener
		return False

def move_and_click(x, y):
	pyautogui.moveTo(x, y)
	pyautogui.click()

def b():
	print(pyautogui.position())
	x = 1384
	y1 = 1675	# 2星
	y2 = 1290	# 选择2星
	y3 = 1750	
	move_and_click(x, y1)
	move_and_click(x, y2)
	sleep(3)
	pyautogui.keyDown('ctrl')
	pyautogui.press('a');
	pyautogui.keyUp('ctrl')
	pyautogui.moveTo(x, y3)
	pyautogui.rightClick()
	A=1

def __get_element_postion(element):
	"""获取元素的中心点位置"""
	# 元素坐标
	element_position = element.rectangle()
	# 算出中心点位置
	center_position = (int((element_position.left + element_position.right) / 2), int((element_position.top + element_position.bottom) / 2))
	return center_position


def ctrl_mini_app():
	# app = Application(backend='win32').connect(path="C:\Program Files (x86)\Tencent\WeChat\WeChatApp.exe")
	app = Application(backend='win32').connect(process=18500)
	weixin_pc_window = app.window(title=u"猜歌王", class_name="Chrome_WidgetWin_0")
	weixin_pc_window.set_focus()


def ctrl_wechat():
	# app = Application(backend='uia').connect(path="C:\Program Files (x86)\Tencent\WeChat\WeChat.exe")
	app = Application(backend='uia').connect(process=8400)
	weixin_pc_window = app.window(title=u"微信", class_name="WeChatMainWndForPC")
	weixin_pc_window.set_focus()

	# 1. 获取左侧【聊天】切换元素
	chat_list_element = weixin_pc_window.child_window(title="聊天", control_type="Button")
	# 2、点击进入到聊天列表
	mouse.click(button='left', coords=__get_element_postion(chat_list_element))

	# 3、点击【文件传输助手】进入到聊天页面
	file_helper_element = weixin_pc_window.child_window(title="文件传输助手", control_type="ListItem")

	mouse.click(button='left', coords=__get_element_postion(file_helper_element))
# 4、获取输入框元素，模拟输入
	edit_element = weixin_pc_window.child_window(title="输入", control_type="Edit")
	sleep(2)
	# 输入内容
	edit_element.type_keys("hebe")
	# 使用键盘模拟回车，即：发送
	send_keys('{ENTER}')
	 # 结束进程，释放资源
	# app.kill()
	a=1

# 连接事件以及释放
# with Listener(on_click=on_click) as listener:
# 	listener.join()
input('aaa')

