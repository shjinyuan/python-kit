#!/usr/bin/env python
# coding=utf-8
#
# KeyBoard.py
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
# ref: www.jb51.net/article/118588.htm
from pykeyboard import *
import time

k = PyKeyboard()

k.type_string('test KeyBoard simulator')
k.press_key('H')#模拟键盘按住H键
k.release_key('H')#模拟键盘松开H键
k.tap_key('H') #模拟点击H键


class TapRecord(PyKeyboardEvent):
    def __init__(self):
        PyKeyboardEvent.__init__(self)

    def tap(self, keycode, character, press):
        print(time.time(), keycode, character, press)

t = TapRecord()
t.run()
