import requests
import json
from urllib import request
import os

headers = {
    'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.72 Safari/537.36"}


def get_huya_girls(page):
    url = f"https://www.huya.com/cache.php?m=LiveList&do=getLiveListByPage&gameId=2168&tagAll=0&callback=getLiveListJsonpCallback&page={page}"
    response = requests.get(url=url, headers=headers)
    # print(response.text)
    result = json.loads(response.text[len("getLiveListJsonpCallback("):-1])
    # print(result)
    girls_list = result["data"]["datas"]
    for girl in girls_list:
        nick = girl["nick"]
        img = girl["screenshot"]
        # print(nick, img)
        try:
            request.urlretrieve(img, f"虎牙颜值主播图片/{page}-{nick}.png")
            request.urlcleanup()
            print(f"{page}-{nick}.png 下载完成")
        except Exception as e:
            print(f"error:{e}")


if __name__ == '__main__':
    if not os.path.exists(f"虎牙颜值主播图片"):
        os.mkdir(f"虎牙颜值主播图片")
    for i in range(2, 6):
        get_huya_girls(i)
