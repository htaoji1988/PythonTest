#!/usr/bin/python
# coding=utf-8

import pexpect


class SendCommond:
    def __init__(self, *args):
        for i in args:
            print i


SendCommond(1, 2, 3)
