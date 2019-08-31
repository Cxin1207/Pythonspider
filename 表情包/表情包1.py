import re
import requests
import urllib.request
url = 'https://www.fabiaoqing.com/biaoqing'

#获取源代码数据
response = urllib.request.urlopen(url).read().decode()

#通过正则表达式，在页面当中匹配图片的url地址
#
image_urls =re.findall(r'data-original="(.*?)"', response, re.S)

def save_image(url):
	'''
	对url进行切割 然后保存图片
	'''
	print(url)
	file_path = url.split('/')[-1]
	print(file_path)
	response = urllib.request.urlopen(url).read()
	# with open(file_path, 'wb') as f:
	# 	f.write(response)

for image_url in image_urls:
	save_image(image_url)

