import re
import requests


def spider_novel(novel_name, novel_main_url):
    headers = {
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36"
    }
    res = requests.get(novel_main_url, headers=headers)
    res.encoding = 'utf8'
    author = re.findall(r'author" content="(.+?)"/>', res.text)
    with open(novel_name + '.txt', 'a', encoding='utf8') as file:
        file.write(f'作者：{author[0]}\n网址：{novel_main_url}\n\n')
    novel_url_list = re.findall(r'<a href="(\d+.html)">', res.text)
    a = 1
    for x in novel_url_list:
        res1 = requests.get(f'{novel_main_url}{x}', headers=headers)
        res1.encoding = 'utf8'
        novel_header = re.findall(r'<h1>(.+?)</h1>', res1.text)
        if "第" in novel_header[0]:
            novel_text = re.findall(r'&nbsp;&nbsp;&nbsp;&nbsp;(.+?)<br/>', res1.text)
            novel_text_str = str(novel_text).replace("['", "").replace("', '", "\n").replace("']", "")
            with open(novel_name + '.txt', 'a', encoding='utf8') as file:
                file.write(f'{novel_header[0]}\n{novel_text_str}\n\n')
            print(f'{novel_header[0]}\t\t写入成功，已完成{format(a / len(novel_url_list) * 100, ".2f")}%')
        a += 1


# 本脚本仅支持域名为： http://www.bswtan.com/ 的小说网页，需在下面更改 name 和 main_url 两个参数，novel_main_url参数是进入小说章节列表浏览器地址栏上的地址。
if __name__ == '__main__':
    name = "武神"
    main_url = "http://www.bswtan.com/2/2374/"
    print(f'《{name}》开始下载，请耐心等待……')
    with open(name + '.txt', 'a', encoding='utf8') as f:
        f.write(f'书名：《{name}》\n')
    spider_novel(name, main_url)
    print(f"《{name}》已下载成功，尽情阅读吧^_^")
