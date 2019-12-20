#!/usr/bin/env python
# -*- coding:utf-8 -*-
'''from guoya_1912.module_1912 import Product

phone1 = Product("土豪金")
print(phone1.color)
print(phone1.size)

import os
#获取文件的绝对路径
d = os.path.abspath("123.txt")
print(d)
#获取文件夹路径
p = os.path.dirname(d)
print(p)
#获取文件名
f = os.path.basename(d)
print(f)
# 拼接目录和文件路径
path = os.path.join(d,f)
print(path)
# 创建文件夹
os.mkdir("ga_c")'''

import os
try:
    os.mkdir("guaya_b")
except FileExistsError:
    print("文件夹已存在")
else:
    print("创建文件夹成功")
finally:
    print("创建文件夹结束")


