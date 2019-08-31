import re
import requests
import urllib.request
page = 5

def save_image(url):
    '''
    对url进行切割 然后保存图片
    '''

    file_path = url.split('/')[-1]
    headers = {
    #httpbin.org/get
     "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36",
     "Refer":start_url,
    }
    # response = urllib.request.urlopen(url).read()
    req = urllib.request.Request(url,headers=headers)
    response = urllib.request.urlopen(req).read()
    with open(file_path, 'wb') as f:
        f.write(response)

for pn in range(int(page)):
    # url = 'https://www.fabiaoqing.com/biaoqing'
    # start_url = 'https://www.fabiaoqing.com/biaoqing/lists/page/{}.html'.format(pn)
    # start_url = 'https://www.fabiaoqing.com/biaoqing/lists/page/{}.html'.format(pn)
    start_url = 'http://www.bee-ji.com/s?w=%E5%A5%BD%E7%9A%84'

    #获取源代码数据
    response = urllib.request.urlopen(start_url).read().decode()

    #通过正则表达式，在页面当中匹配图片的url地址

    image_urls =re.findall(r'alt=".*？" src="(.*？)" style', response, re.S)
    # resp = requests.get('http://tieba.baidu.com/f?kw={}&ie=utf-8&pn={}'.format(key,pn*50)).text

    for image_url in image_urls:
        save_image(image_url)

