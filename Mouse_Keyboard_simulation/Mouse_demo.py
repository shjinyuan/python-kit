#!/usr/bin/env python
# coding=utf-8
#
# Key.py
#
# Copyright (C) 2018-2023 jinyuan  <jinyuan@company.com>. All Rights Reserved.
#
# History:
#    2020/01/07 - [jinyuan] Created file
#
# Maintainer: jinyuan <jinyuan@email.com>
#    Created: 2020-01-07
# LastChange: 2020-01-07
#    Version: v0.0.01
#
from pymouse import *
import time

m = PyMouse()
while(1):
    m.click(16,16)
    time.sleep(1)

class ClickOnAcci(PyMouseEvent):
    def __init__(self):
        PyMouseEvent.__init__(self)

    def click(self, x, y, button, press):
        print(time.time(),x,y,button,press)

c = ClickOnAcci()
c.run()

m = PyMouse()
m.click(10,10)
#m.click(x,y,button,n)
#x,y #坐标
#button #1：左键 #2：右键
#n 点击次数，默认1次,2表示双击
