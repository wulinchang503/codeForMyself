# 本脚本仅支持小说主页：https://www.mzljy.cn/
import requests
import re


def novel(novel_name, novel_number):
    # 小说主页
    main_url = "https://www.mzljy.cn/"
    # 拼接小说章节主页
    novel_url = f"{main_url}xiaoshuo/{novel_number}.html"
    # print(novel_url)
    # 请求头
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36"
    }
    # 请求网页
    res = requests.get(url=novel_url, headers=headers)
    # 转码
    res.encoding = 'gbk'
    # 匹配网址（换小说这里要改）
    author = re.findall(f'author" content="(.*?)"/>', res.text, flags=0)
    with open(novel_name + '.txt', 'a', encoding='utf8')as a:
        a.write(f'作者：{str(author[0])}\n网址：{novel_url}\n\n')
    url_all = re.findall(f'/xiaoshuo/{novel_number}/.+html">', res.text, flags=0)
    # print(url_all)

    # 循环去掉网址上多余的符号
    url_list = []
    for x in url_all:
        url_list.append(x.rstrip('">'))
    print("------------小说正在写入文件，请耐心等待------------")
    # 章节循环写入txt文件
    # for y in [url_list[0], url_list[1], url_list[2]]:# （暂时试下载前三章）
    for y in url_list:
        # 请求章节内容
        res1 = requests.get(f'https://www.mzljy.cn{y}', headers=headers)
        # print(f'https://www.mzljy.cn{url_list[0]}')
        # 转码
        res1.encoding = 'gbk'
        # 正则取章节名
        novel_title = re.findall(r'<h1>(.*?)</h1>', res1.text, flags=0)
        # 判断一下章节名是否有章这个字，没有这个字就没有正文。
        if "章" in novel_title[0]:
            # 正则取章节内容
            novel_text = re.findall(r'&nbsp;&nbsp;&nbsp;&nbsp;(.*?)<', res1.text, flags=0)
            # 将正文列表转换为字符串，并换行和去掉多余的符号。
            str_novel_text = str(novel_text).replace("['", "").replace("', '", "\n").replace("']", "")
            # 追加到小说txt文件
            with open(novel_name + '.txt', 'a', encoding='utf8')as a:
                a.write(f'{str(novel_title[0])}\n{str(str_novel_text)}\n\n')
            print(f"{str(novel_title[0])}--->已下载,离结束越来越近了^_^")
        else:
            pass


if __name__ == '__main__':
    print("------------程序开始执行------------")
    novel_name = '我刷题就涨灵力值'
    novel_number = "40864"

    with open(novel_name + '.txt', 'a', encoding='utf8') as a:
        a.write(f'书名：《{novel_name}》\t')
    novel(novel_name, novel_number)
    print(f"《{novel_name}》已下载成功，尽情阅读吧^_^")
