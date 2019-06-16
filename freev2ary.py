#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os
import re
import urllib2
from bs4 import BeautifulSoup
from datetime import datetime
import time

# TARGET="v2ary.json"
TIME = float(os.environ.get('TIME'))
TARGET=os.environ.get('TARGET')
TEMPLATE=os.environ.get('TEMPLATE')

def start():
    url = "https://connect.freev2ray.org"
    response = urllib2.urlopen(url)
    html_doc = response.read()
    # 创建一个BeautifulSoup对象
    soup = BeautifulSoup(html_doc,"html.parser",from_encoding="utf-8")
    # 获取uuid
    global uuid
    uuid = soup.find("span", {"id": "uuid"}).text.replace("\n", "").strip()
    # 获取ip
    global ip
    ip = soup.find("span", {"id": "ip"}).text.replace("\n", "").strip()
    # 获取port
    global port
    port = soup.find("span", {"id": "port"}).text.replace("\n", "").strip()
    # 获取alterid
    global alterid
    alterid = soup.select("#intro > div > div > header > p:nth-child(6)")[0].text.replace("\n", "").replace("AlterID:", "").strip()
def generateJson():
    start()

    print("uuid: "+ uuid)
    print("ip: "+ ip)
    print("port: "+ port)
    print("alterid: "+ alterid)
    # 模版文件
    template = open(TEMPLATE,'r+')
    # 生成的目标文件
    target = open(TARGET, 'w')
    infos = template.readlines()
    template.seek(0,0)
    target.seek(0)
    for line in infos:
        # 替换找出的文件
        line_new = line.replace('$address', ip).replace('${id}', uuid).replace('${id}', uuid).replace('${alterId}', alterid).replace('${port}', port)
        target.write(line_new)
    target.close()
    template.close()
# 每n秒执行一次
def timer(n, fun):
    while True:
        print("-------------------------------update: " + datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        fun()
        time.sleep(n)

# generateJson()
timer(TIME, generateJson)
# open('v2ary_temp.json', 'w').write(
#     re.sub(r'$address', ip, open('v2ary_temp.json').read())
#     )