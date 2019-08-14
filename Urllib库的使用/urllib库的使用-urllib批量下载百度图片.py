import re
import urllib.request
start_url = 'http://image.baidu.com/search/index?ie=utf-8&tn=baiduimage&word=%E5%85%81%E5%84%BF%E5%A3%81%E7%BA%B8'
# req = urllib.request.urlopen(url)#解析图片地址
# print(req.read())#查看获取的数据

#获取网页源代码的数据
response = urllib.request.urlopen(start_url).read().decode()

#通过正则表达式，在页面中匹配图片的url地址
image_urls = re.findall(r'"thumbURL":"(.*?)"',response,re.S)
print(image_urls)
#保存图片
def save_image(url):
    '''
    对url进行分割，然后保存图片
    :param url:
    :return:
    '''
    file_path = url.split('/')[-1]
    headers ={
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36",
        'Referer':start_url,
    }
    print('url',url)
    # response = urllib.request.urlopen(url).read()
    req = urllib.request.Request(url, headers=headers)
    response = urllib.request.urlopen(req).read()
    with open(file_path,'wb') as f:
        f.write(response)
for image_url in image_urls:
    save_image(image_url)

