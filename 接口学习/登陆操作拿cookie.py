import requests
import json
import re

headers = {
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest'
}
login_url = "http://192.168.205.128:8080/recruit.students/login/in"
datas = {
    "account": "admin",
    "pwd": "660B8D2D5359FF6F94F8D3345698F88C"
}
# session = requests.session()
resp = requests.get(url=login_url, headers=headers, params=datas)
# cookiejar = resp.cookies
# cookiedict = requests.utils.dict_from_cookiejar(cookiejar)

# print(cookiejar)
# print(cookiedict)

print(resp.cookies)
print(resp.headers)
print(resp.status_code)
