import re
import requests

url = "https://book.qidian.com/info/1016399199#Catalog"
headers = {
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'zh-CN,zh;q=0.9',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36',
            'cookie': 'e2={"pid":"qd_P_xiangqing","eid":"qd_G16","l1":3}; ' \
                      'e1={"pid":"qd_P_xiangqing","eid":"qd_G55","l1":14}; ' \
                      '_csrfToken=bR1FJuFb3p9Nej5PRfzcNRYyZhcR0ScMnScskMVp; newstatisticUUID=1616945527_497961104; qdrs=0|3|0|0|1; qdgd=1; ' \
                      'showSectionCommentGuide=1; _yep_uuid=ff57b02d-bfaa-757c-49fd-5f9dd2febbde; ' \
                      'e1={"pid":"qd_P_limitfree","eid":"qd_E01","l1":4}; e2={"pid":"qd_P_free","eid":""}; ' \
                      'lrbc=1016397637|493097374|0,1010711198|394020908|0,1209977|23724364|1;rcr=1016397637,1010711198,1966074,1209977; bc=1016397637 '
        }
res = requests.get(url=url,headers=headers)
res.encoding = "utf8"
print(res.text)