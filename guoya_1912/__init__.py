#!/usr/bin/env python
# -*- coding:utf-8 -*-
''''#获取随机数字
import random
a = random.randint("23,45")
print(a)
#有序的可迭代对象 （）里面可以放字符串，列表，元组
c = random.choice
print(c)'''
import os
try:
    os.mkdir("guaya_b")
except FileExistsError:
    print("文件夹已存在")
else:
    print("创建文件夹成功")
finally:
    print("创建文件夹结束")
'''import os
try:
    os.mkdir("guaya_b")
except FileExistsError:
    print("文件夹已存在")
else:
    print("创建文件夹成功")
finally:
    print("创建文件夹结束")'''
