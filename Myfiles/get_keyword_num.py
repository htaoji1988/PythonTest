#!/usr/bin/python
# coding=utf-8

import time
import re

date_now = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
date1 = time.strftime('%Y-%m-%d %H:%M', time.localtime(time.time() - 60 * 5))
date2 = time.strftime('%Y-%m-%d %H:%M', time.localtime(time.time() - 60 * 4))
date3 = time.strftime('%Y-%m-%d %H:%M', time.localtime(time.time() - 60 * 3))
date4 = time.strftime('%Y-%m-%d %H:%M', time.localtime(time.time() - 60 * 2))
date5 = time.strftime('%Y-%m-%d %H:%M', time.localtime(time.time() - 60 * 1))
date_strings = [date1, date2, date3, date4, date5]


def log_out(logfile, content):
    with open(logfile, 'a') as f:
        f.write(content)


def test(files, date, keyword):
    number = 0
    with open(files, "r") as filename:
        for line in filename:
            match = re.search(date, line)
            if match is None:
                continue
            match = re.search(keyword, line)
            if match is None:
                continue
            number += 1
    return number


def get_num():
    num = 0
    for date_keyword in date_strings:
        num = num + test("/data1/logs/interface/kafka_produce_41.log", date_keyword, "Kafka异常")
        num = num + test("/data1/logs/interface/kafka_produce_42.log", date_keyword, "Kafka异常")
    if num > 50:
        log_out("/tmp/test.txt", date_now + " fail:kafka-produce响应异常\n")
    else:
        log_out("/tmp/test.txt", date_now + " success\n")


if __name__ == "__main__":
    get_num()
