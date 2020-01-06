#!/usr/bin/python
# -*- coding: utf-8 -*-


import requests
url = str("http://www.taobao.com")
while True:
    if url == "http://www.taobao.com1":
        break
    else:
        r = requests.get(url)
        print(r.text)