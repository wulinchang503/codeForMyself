import requests
import re
from lxml import etree


novel_name = "吞天记"
novel_url = "https://vipreader.qidian.com/chapter/1016399199"
all_list = 10
first_title = 493128796


for i in range(all_list):
    headers = {
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'zh-CN,zh;q=0.9',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
            'cookie': 'e2={"pid":"qd_P_xiangqing","eid":"qd_G16","l1":3}; ' \
                      'e1={"pid":"qd_P_xiangqing","eid":"qd_G55","l1":14}; ' \
                      '_csrfToken=bR1FJuFb3p9Nej5PRfzcNRYyZhcR0ScMnScskMVp; newstatisticUUID=1616945527_497961104; qdrs=0|3|0|0|1; qdgd=1; ' \
                      'showSectionCommentGuide=1; _yep_uuid=ff57b02d-bfaa-757c-49fd-5f9dd2febbde; ' \
                      'e1={"pid":"qd_P_limitfree","eid":"qd_E01","l1":4}; e2={"pid":"qd_P_free","eid":""}; ' \
                      'lrbc=1016397637|493097374|0,1010711198|394020908|0,1209977|23724364|1;rcr=1016397637,1010711198,1966074,1209977; bc=1016397637 '
        }

    url = f"{novel_url}/{first_title+i}"
    print(url,f"第{i+1}章")
    res = requests.get(url, headers=headers)
    res.encoding = "utf8"
    # print(res.text)
    title = re.findall(r'<span class="content-wrap">(.+?)</span>',res.text)
    with open(novel_name + ".txt", "a", encoding="utf8") as f:
        f.write(f"{title}\n")
    html = etree.HTML(res.text)
    text_res = html.xpath('//div[@class="read-content j_readContent"]/p')
    # print(text_res)
    for j in text_res:
        with open(novel_name + ".txt", "a", encoding="utf8") as f:
            f.write(f'{j.text}\n')


