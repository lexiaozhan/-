#!/usr/bin/env python
# -*- coding:utf-8 -*-
class Product():
    size = "6"
    def __init__(self,color):
        self.color = color
    def call(self):
        ptint("hello")
phone1 = Product("土豪金")
print(phone1.color)
print(phone1.size)
