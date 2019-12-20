#!/usr/bin/env python
# -*- coding:utf-8 -*-
import os
try:
    os.mkdir("guaya_b")
except FileExistsError:
    print("文件夹已存在")
else:
    print("创建文件夹成功")
finally:
    print("创建文件夹结束")