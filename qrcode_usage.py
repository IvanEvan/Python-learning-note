#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 18-4-16 上午10:35
# @Author  : Evan
# @File    : qrcode_usage.py
# @Software: PyCharm Community Edition
import qrcode
from PIL import Image

qr = qrcode.QRCode(version=5, error_correction=qrcode.constants.ERROR_CORRECT_H, box_size=8, border=4,)
# img = qrcode.make('Some data here')
qr.add_data('ahhahahahahaha')
qr.make(fit=True)

# img = qr.make_image(fill_color='orange', back_color='black')
img = qr.make_image()
img = img.convert('RGBA')

icon = Image.open('/home/yn/Pictures/witcher.jpg')

img_w, img_h = img.size
factor = 4
size_w = int(img_w / factor)
size_h = int(img_h / factor)

icon_w, icon_h = icon.size
if icon_w > size_w:
    icon_w = size_w
if icon_h > size_h:
    icon_h = size_h
icon = icon.resize((icon_w, icon_h), Image.ANTIALIAS)

w = int((img_w - icon_w)/2)
h = int((img_h - icon_h)/2)
icon = icon.convert("RGBA")
img.paste(icon, (w, h), icon)

img.show()
img.save('/home/yn/Pictures/test-qr1.png')
