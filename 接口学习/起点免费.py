from lxml import etree
import re
import requests


def novel_spider(name, url):
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
    url = f'{url}#Catalog'
    # url = "https://book.qidian.com/info/1016397637#Catalog"
    res = requests.get(url, headers=headers)
    res.encoding = "utf8"
    # print(res.text)
    author = re.findall(r"authorName: '(.+?)',", res.text)
    with open(name + ".txt", "a", encoding="utf8") as f:
        # f.write(f'作者：{author[0]}\n\n')
        f.write(f'作者：佚名\n\n')
    novel_url_list = re.findall(r'<a href="//(read.qidian.com/chapter/.+?)" target', res.text)
    for x in novel_url_list:
        res1 = requests.get(f"https://{x}", headers=headers)
        html = etree.HTML(res1.text)
        # 章节标题
        title_text = html.xpath('//h3[@class="j_chapterName"]/span')
        with open(name + ".txt", "a", encoding="utf8") as f:
            f.write(f'{title_text[0].text}\n')
        # 章节正文
        text_res = html.xpath('//div[@class="read-content j_readContent"]/p')
        for t in text_res:
            with open(name + ".txt", "a", encoding="utf8") as f:
                f.write(f'{t.text}\n\n')


# 爬起点中文网免费小说，仅限免费小说。
if __name__ == '__main__':
    novel_name = "回到三国战五胡"
    novel_url = "https://book.qidian.com/info/1023805447"
    with open(novel_name + ".txt", "a", encoding="utf8") as a:
        a.write(f'小说：《{novel_name}》\t网址：{novel_url}\n')
    novel_spider(novel_name, novel_url)
    print(f'《{novel_name}》下载完成，愉快的阅读吧 ^_^ ')
