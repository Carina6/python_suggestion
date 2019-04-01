#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup


def test_drag():
    res = requests.get(url='http://jr.jd.com')
    bs = BeautifulSoup(res.content, 'html.parser')
    # 找到所有class为 nav-item-primary 的a 标签
    text_list = bs.find_all('a', 'nav-item-primary')
    for i in text_list:
        print(i.get_text())
