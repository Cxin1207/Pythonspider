import urllib.error
import urllib.request
try:
    req = urllib.request.urlopen('https://www.jianshu.com/')
except urllib.error.URLError as e:
    print(e.code)
    print(e.reason)
    print(e.headers)
