# coding=utf-8
#! /usr/bin/env python# -*- coding: utf-8 -*-
import requests, json, re, os

session = requests.session()
# 配置用户名（一般是邮箱）
email = os.environ.get('EMAIL')

# 配置用户名对应的密码 和上面的email对应上
passwd = os.environ.get('PASSWD')

# AnPlus
AnPlus = os.environ.get('AnPlus')

def push(content):
    if AnPlus != '1' :
        payload = {
            "title": u"ikuuu签到:"+content,
            "content": content,
            "channel": "97024"
        }

        headers = {
            "Content-Type": "application/x-www-form-urlencoded"
        }

        response = requests.post("https://api.anpush.com/push/"+AnPlus, headers=headers, data=payload)
        print('AnPlus消息推送推送成功' if response.status_code == 200 else 'AnPlus消息推送推送失败')
    else:
        print('未使用消息推送推送！')

# 会不定时更新域名，记得Sync fork

login_url = 'https://ikuuu.pw/auth/login'
check_url = 'https://ikuuu.pw/user/checkin'
info_url = 'https://ikuuu.pw/user/profile'

header = {
        'origin': 'https://ikuuu.me',
        'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'
}
data = {
        'email': email,
        'passwd': passwd
}
try:
    print('进行登录...')
    response = json.loads(session.post(url=login_url,headers=header,data=data).text)
    print(response['msg'])
    # 获取账号名称
    info_html = session.get(url=info_url,headers=header).text
#     info = "".join(re.findall('<span class="user-name text-bold-600">(.*?)</span>', info_html, re.S))
#     print(info)
    # 进行签到
    result = json.loads(session.post(url=check_url,headers=header).text)
    print(result['msg'])
    content = result['msg']
    # 进行推送
    push(content)
except:
    content = '签到失败'
    print(content)
    push(content)