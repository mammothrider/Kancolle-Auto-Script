#coding: UTF-8
import win32gui
import win32api
import win32con
import time
from PIL import ImageGrab
from PIL import Image

class MouseController:
	def __init__(self):
		print "class MouseController online"
		self.game_hwnd = 0
		return 
	
	def hwndCallback(self, hwnd, extra):
		if "KanColleViewer.exe" in win32gui.GetClassName(hwnd):
			str = win32gui.GetWindowText(hwnd)
			a = "\xcc\xe1\xb6\xbd" #part of the title utf-8 code
			if a in str:
				#print win32gui.GetClassName(hwnd)
				self.game_hwnd = hwnd
			
	
	def getWindowHandler(self):
		#game_hwnd = win32gui.FindWindow("HwndWrapper[KanColleViewer.exe;;26a926b8-7533-4371-93c1-1ca324e75719]", None)

		self.flag = 0
		win32gui.EnumWindows(self.hwndCallback, None) #enumerate each window

		print " "
		print "Game Handler: ", self.game_hwnd
		print "Class Name:   ", win32gui.GetClassName(self.game_hwnd)
		print "Window Title: ", win32gui.GetWindowText(self.game_hwnd)
		if self.game_hwnd == 0:
			print "handler not found"
			exit(1)
			
	def getwindowposition(self):
		"""
		Active the window and get the window position
		"""
		self.getWindowHandler()
		
		win32gui.ShowWindow(self.game_hwnd, win32con.SW_SHOWNORMAL)
		win32gui.SetForegroundWindow(self.game_hwnd)
		game_rect = win32gui.GetWindowRect(self.game_hwnd)
		return game_rect
		
	def screenshot(self, rect):
		"""
		create a screenshot
		"""
		src_image = ImageGrab.grab((rect[0],\
									rect[1],\
									rect[2],\
									rect[3]))
		#src_image.show()
		return src_image
			
	def mouseMoveTo(self, x, y):
		time.sleep(1)
		print "move mouse to:", x, y
		#win32api.SetCursorPos((x, y)) 
		MOUSEEVENTF_MOVE = 0x0001 # mouse move
		MOUSEEVENTF_ABSOLUTE = 0x8000 # absolute move
		MOUSEEVENTF_MOVEABS = MOUSEEVENTF_MOVE + MOUSEEVENTF_ABSOLUTE
		
		SCREEN_WIDTH = win32api.GetSystemMetrics (0)
		SCREEN_HEIGHT = win32api.GetSystemMetrics (1)
		print SCREEN_WIDTH, SCREEN_HEIGHT
		
		nx = int(x*65535.0/SCREEN_WIDTH)
		ny = int(y*65535.0/SCREEN_HEIGHT)
		win32api.mouse_event(win32con.MOUSEEVENTF_MOVE | win32con.MOUSEEVENTF_ABSOLUTE, nx, ny)
		#http://stackoverflow.com/questions/3720938/win32-moving-mouse-with-setcursorpos-vs-mouse-event
		#mouse_event is a low level control
		
	def mouseLeftClick(self):
		win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0) 
		time.sleep(0.1)
		win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
			
if __name__ == '__main__':
	mc = MouseController()
	rect = mc.getwindowposition()
	print rect
	mc.mouseMoveTo(rect[0], rect[1])
	mc.mouseLeftClick()
	mc.mouseMoveTo(rect[2], rect[3])