#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/1/15 11:22 PM
# @Author  : hlliu

from PIL import Image, ImageDraw, ImageFont

img = Image.open("front.png")
draw = ImageDraw.Draw(img)

front = ImageFont.truetype('SimHei.ttf', 16)
draw.text((73, 40), '刘红莲', fill=(0, 25, 25), font=front)
draw.text((73, 72), '女', fill=(0, 25, 25), font=front)
draw.text((152, 72), '汉', fill=(0, 25, 25), font=front)
draw.text((73, 100), '1989', fill=(0, 25, 25), font=front)
draw.text((135, 100), '11', fill=(0, 25, 25), font=front)
draw.text((175, 100), '6', fill=(0, 25, 25), font=front)
draw.text((73, 127), '长沙市岳麓区金星北路517号', fill=(0, 25, 25), font=front)
draw.text((131, 202), '430581198911064948', fill=(0, 25, 25), font=front)
img.show()
img.save("tmp.png")
