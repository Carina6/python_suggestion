#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date  : 2019/6/5 11:09
# @Author: hlliu
import requests

# 统计url页面中Python的出现次数
print(str(requests.get(url='https://www.ershicimi.com/').content.decode('utf-8')).count('Python'))