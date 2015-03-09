import cv2
import numpy as np
from matplotlib import pyplot as plt
import os, sys

class TMatching:
	def __init__(self):
		print "class TMatching online"
		self.pic = []
		self.tempic = []
		self.temw = 0
		self.temh = 0
		self.top_left = 0
		self.bottom_right = 0
		self.res = 0
		return
		
	def readpic(self, _string):
		"""
		read the big picture for matching
		"""
		print "reading picture"
		self.pic = cv2.imread(_string, 0)
		if self.pic is None:
			print "Picture read error"
			return 1
		
	def setpic(self, pil_image):
		"""
		read big picture from PIL
		"""
		print "setting picture"
		open_cv_image = np.array(pil_image) 
		self.pic = cv2.cvtColor(open_cv_image, cv.COLOR_RGB2GREY)
		
	def readtempic(self, _string):
		"""
		read the small picture for matching
		"""
		print "reading template"
		self.tempic = cv2.imread(_string, 0)
		if self.tempic is None:
			print "Picture read error"
			return 1
		self.temw, self.temh = self.tempic.shape[::-1]
		
	def matching(self):
	#http://opencv-python-tutroals.readthedocs.org/en/latest/py_tutorials/py_imgproc/py_template_matching/py_template_matching.html
		print "matching"
		method = eval("cv2.TM_SQDIFF_NORMED")
		
		self.res = cv2.matchTemplate(self.pic, self.tempic, method)
		min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(self.res)
		
		print min_val
		self.top_left = min_loc
		self.bottom_right = (self.top_left[0] + self.temw, self.top_left[1] + self.temh)
		return self.top_left, self.bottom_right, min_val
	
	def testMatching(self):
		cv2.rectangle(self.pic, self.top_left, self.bottom_right, 255, 2)
		plt.subplot(121),plt.imshow(self.res,cmap = 'gray')
		plt.title('Matching Result'), plt.xticks([]), plt.yticks([])
		plt.subplot(122),plt.imshow(self.pic,cmap = 'gray')
		plt.title('Detected Point'), plt.xticks([]), plt.yticks([])
		plt.show()
		
if __name__ == "__main__":
	path = os.path.abspath(sys.argv[0])
	path = os.path.dirname(path)+"/" 
	tm = TMatching()

	if tm.readpic(path + "whole3.jpg"):
		os.exit() 
	if tm.readtempic(path + "yz2state.png"):
		os.exit()
	tm.matching()
	tm.testMatching()