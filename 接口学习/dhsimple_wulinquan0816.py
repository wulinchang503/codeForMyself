# -*- coding: utf-8 –*-
import requests, re, faker
from fake_useragent import UserAgent

url = "https://www.dhgate.com/store/products/21261418"
url_list, a = [], 0
for i in range(4):
    res = requests.get(url=f"{url}/{i}.html", proxies={'http': faker.Faker().ipv4(network=False)},
                       headers={"user-agent": UserAgent().random})
    res.encoding = "utf8"
    url_path = r"(https://www.dhgate.com/product/.+?html)"
    url_tmp = re.findall(url_path, res.text)
    for j in url_tmp:
        if j not in url_list:
            url_list.append(j)
# print(url_list)
while True:
    for x in range(len(url_list)):
        a += 1
        response = requests.get(url=url_list[x], proxies={'http': faker.Faker().ipv4(network=False)},
                                headers={"user-agent": UserAgent().random})
        if response.status_code == 200:
            print(f"返回码:{response.status_code} 正常, 运行{a}次")
        else:
            print(f"返回码:{response.status_code} 异常, 请结束程序")
            break
    if a % (len(url_list)) != 0:
        break
    else:
        pass
