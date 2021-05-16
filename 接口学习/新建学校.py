import requests
from pprint import pprint

url = 'http://192.168.147.129:8080/recruit.students/school/manage/addSchoolInfo'
headers = {
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest'
}
cookie = {
    'JSESSIONID': 'F9BBFF661E352978C877C7E8D065FE82',
    'userInfoCookie': ''
}
data = {
    'schoolName': 'requests测试学校',
    'listSchoolType[0].id': 4,
    'canRecruit': 0,
    'remark': '这是测试用requests调用接口新建学校。'
}
res = requests.post(url, data=data, headers=headers, cookies=cookie)

pprint(res.json())
