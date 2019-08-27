# -*- coding:utf-8 -*-
#@Time  : 2019/7/12 14:44
#@Author: dongyani
#学习django-1

from selenium import webdriver
import unittest

browser = webdriver.Firefox()
assert 'To-Do' in browser.title

# class NewVisitorTest(unittest.TeatCase):
#
# 	def setUp(self):
# 		self.browser = webdriver.Firefox()
#
# 	def tearDown(self):
# 		self.browser.quit()
#
# 	def test_can_start_a_list_and_retrieve_it_later(self):
		#做一个在线代办事项的应用
		#去看下这个应用的首页
		# self.browser.get("http://localhost:8000")
		
		#用户注意到网页的标题和头部都包含“To-Do”这个词
		#assert 'To-Do' in browser.title, "Browser title was " + browser.title
		# self.assertIn('To-Do', self.browser.title)
		# self.fail('Finish the test!')
		
		#应用邀请用户加入一个代办事项

# if __name__ == '__main__':
# 	#禁止抛出ResourceWarning异常
# 	unittest.main(warnings='ignore')
	

# browser = webdriver.Firefox()

#做一个在线代办事项的应用
#去看下这个应用的首页
# browser.get("http://localhost:8000")

#用户注意到网页的标题和头部都包含“To-Do”这个词
# assert 'To-Do' in browser.title, "Browser title was " + browser.title

#应用邀请用户加入一个代办事项


#用户要在一个文本框中输入了“buy peacock feathers” (买孔雀羽毛)
#假设用户的爱好是使用假苍蝇做诱饵鱼

#用户按回车键之后，页面更新了
#待办事项表格中显示了“1：buy peacock feathers”

#页面中又显示了一个文本框，可以输入其他的待办事项
#用户输入了“use peacock feathers to make a fly” (使用孔雀羽毛做假苍蝇)
#用户做事很有条理

#页面再次更新，她的清单中显示了这两个待办事项

#用户很想知道这个网站是否会记住她的清单
#她看到网站为她做了一个唯一的URL
#而且页面中有一些文字解说这个功能

#她访问那个URL，发现她的待办事项列表还在

#她很满意，去睡觉了

browser.quit()

