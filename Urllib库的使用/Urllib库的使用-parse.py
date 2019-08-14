import urllib.parse
# print(urllib.parse.quote('阿里云'))
# print(urllib.parse.unquote('%E9%98%BF%E9%87%8C%E4%BA%91'))
data = {'user':'忘仙','password':'123455'}
print(urllib.parse.urlencode(data))#将user和password链接到一起

