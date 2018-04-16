#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 18-4-16 上午10:08
# @Author  : Evan
# @File    : geopy_usage.py
# @Software: PyCharm Community Edition
from geopy.geocoders import baidu
# 可以使用geopy库来查询地址，国家，城市，地标，geopy使用的是第三方的geo解析器(包括谷歌地图，必应地图，Nominatim等)和一些数据源来获取地理信息
apikey = '0123456789' # 从网站申请 http://lbsyun.baidu.com/apiconsole/key?application=key
geolocator = baidu.Baidu(apikey)
location1 = geolocator.geocode('深圳市 龙岗大道2001号')
print location1.address
location2 = geolocator.reverse("52.509669, 13.376294")
print location2.address
print location1.latitude, location1.longitude