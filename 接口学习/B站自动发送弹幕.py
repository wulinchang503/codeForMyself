import requests
import time
from tkinter import *
import random
import faker
from fake_useragent import UserAgent

# headers = {"user-agent": UserAgent().random}
# ip_fake = faker.Faker().ipv4(network=False)
# proxies = {'http': ip_fake}
lis_text = ['光头会', '光头会', '光头会', '光头会', '光头会', '光头会', '光头会', '光头会', '光头会',
            '光头会']


def send():
    a = 0
    while True:
        time.sleep(1)
        send_meg = random.choice(lis_text)
        roomid = "21590631"  # entry.get()
        ti = int(time.time())
        url = 'https://api.live.bilibili.com/msg/send'
        data = {
            'color': '16777215',
            'fontsize': '25',
            'mode': '1',
            # 'msg': f"{send_meg}{a}",
            'msg': f"{send_meg}",
            'rnd': '{}'.format(ti),
            'roomid': '{}'.format(roomid),
            'bubble': '0',
            'csrf_token': '8b52699e0882b4a07832f06137c1e192',
            'csrf': '8b52699e0882b4a07832f06137c1e192',
        }

        headers = {
            'cookie': "_uuid=3AD5C2C2-43ED-CF4C-272C-7C03A893C5CC39111infoc; buvid3=0A3ADA68-9D6F-41C7-8A2C-F3905106498D18533infoc; buvid_fp=0A3ADA68-9D6F-41C7-8A2C-F3905106498D18533infoc; CURRENT_FNVAL=80; blackside_state=1; rpdid=|(RlllJmRYl0J'uYul|u~J)R; LIVE_BUVID=AUTO2616150447854086; CURRENT_QUALITY=80; fingerprint3=5b6467edc561dd793253b501c22712be; fingerprint_s=c03b491ecd8a10b8671d821035618f71; bp_t_offset_472634717=514946383855846131; fingerprint=f1d6f0dea95aeb5b62f2579b6a246ea6; buvid_fp_plain=3058751B-D375-4F3B-A685-1C23E6923F56143084infoc; SESSDATA=2695ae7a,1634475670,0b510*41; bili_jct=8b52699e0882b4a07832f06137c1e192; DedeUserID=472634717; DedeUserID__ckMd5=53f5f88dc3cec9e9; sid=8o6siocl; bp_video_offset_472634717=515762230071997435; _dfcaptcha=560bdf02c26ceeb05c49956cf64bd557; bp_article_offset_472634717=515712807891359857; PVID=4",
            'origin': 'https://live.bilibili.com',
            'referer': 'https://live.bilibili.com/blanc/1029?liteVersion=true',
            'user-agent': UserAgent().chrome
        }
        a += 1
        response = requests.post(url=url, data=data, proxies={"http": faker.Faker().ipv4(network=False)},
                                 headers=headers)
        print(response, a)
        # print(faker.Faker().ipv4(network=False))
        # print(UserAgent().random)
        text.insert(END, '第{}条弹幕发送成功'.format(a))
        # 文本框滚动
        text.see(END)
        # 更新
        text.update()
        text.insert(END, f'发送内容：{send_meg}')


root = Tk()
root.title('B站自动发送弹幕')
root.geometry('560x450+400+200')

label = Label(root, text='请输入房间ID:', font=('华文行楷', 20))
label.grid()

entry = Entry(root, font=('隶书', 20))
entry.grid(row=0, column=1)

text = Listbox(root, font=('隶书', 16), width=50, heigh=15)
text.grid(row=2, columnspan=2)

button1 = Button(root, text='开始发送', font=('隶书', 15), command=send)
button1.grid(row=3, column=0)

button2 = Button(root, text='退出程序', font=('隶书', 15), command=root.quit)
button2.grid(row=3, column=1)

root.mainloop()
