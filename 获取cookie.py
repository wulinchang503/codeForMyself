from selenium import webdriver
# import requests
import json
from time import sleep

driver = webdriver.Chrome()

# cookies = {
#     "LIVE_BUVID": "AUTO1116119254591287",
#     "_uuid": "A45D86D3-DAA1-33E6-B2BE-6B57F5A510DF62022infoc",
#     "buvid3": "1FC24313-B4E6-4D1F-AA27-F5261FAADD4D185012infoc",
#     "finger": "1571944565",
#     "sid": "6xhzd55r",
#     "fingerprint": "db3848bae598a38f0c4da481bf135236",
#     "buvid_fp": "1FC24313-B4E6-4D1F-AA27-F5261FAADD4D185012infoc",
#     "buvid_fp_plain": "1FC24313-B4E6-4D1F-AA27-F5261FAADD4D185012infoc",
#     "DedeUserID": 472634717,
#     "DedeUserID__ckMd5": "53f5f88dc3cec9e9",
#     "SESSDATA": "aa7e6aca,1627477628,30411*11",
#     "bili_jct": "e6d243e1ec1494b85f2007ff309a62c2",
#     "PVID": 2
# }
# driver.add_cookie(cookie_dict=cookies)
driver.maximize_window()
driver.get("https://passport.bilibili.com/login")
driver.delete_all_cookies()
driver.find_element_by_id("login-username").send_keys("18374560250")
driver.find_element_by_id("login-passwd").send_keys("wo1990112")

driver.find_element_by_class_name("btn-login").click()
sleep(20)

dictcookie = driver.get_cookies()
jsoncookie = json.dumps(dictcookie)

driver.close()

with open('cookie.txt', 'w') as f:
    f.write(jsoncookie)

print('cookie is ok')
