#!/usr/bin/python
# coding=utf-8

import os
import time
import glob

date_now = time.strftime('%Y-%m-%d', time.localtime(time.time()))
path = "C:/Users/tt/Desktop/test/test?-" + date_now + ".log"


def path_list(keyword):  # 用来匹配文件
    files = glob.glob(keyword)
    return files


def size_files(files):  # 用来回去文件大小
    size = 0
    for n in path_list(files):
        size = size + os.path.getsize(n)
    return size


def compare_size():  # 主程序，用来比较不同时间内文件大小是否变化
    size1 = size_files(path)
    time.sleep(10)
    size2 = size_files(path)
    if size1 == size2:
        print "Err:File not refreshed!"
    else:
        print "File refreshed."


if __name__ == "__main__":
    compare_size()
