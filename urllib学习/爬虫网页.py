from urllib.request import Request, urlopen
from urllib.parse import urlencode

args = {
    "ie": "utf-8",
    "wd": "尚学堂"
}
url = f"http://www.baidu.com/s?{urlencode(args)}"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.72 Safari/537.36'}
requests = Request(url, headers=headers)
response = urlopen(requests)
print(response.read().decode())
