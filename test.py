#!/usr/bin/python
# coding=utf-8

a = 40  # 创建对象  <40>
b = a  # 增加引用， <40> 的计数
c = [b]  # 增加引用.  <40> 的计数

del a  # 减少引用 <40> 的计数
b = 100  # 减少引用 <40> 的计数
c[0] = -1  # 减少引用 <40> 的计数
