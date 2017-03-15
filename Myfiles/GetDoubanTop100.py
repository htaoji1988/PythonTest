#!/usr/bin/python
# coding=utf-8

import re
import urllib2

r1 = re.compile(r'helloworld')
if r1.match('helloworld'):
    print 'match succeeds'
else:
    print 'match fails'
