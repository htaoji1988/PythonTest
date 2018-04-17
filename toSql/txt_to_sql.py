#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 功能：根据校验目录和文件内容去校验数据文件，校验成功，则会把文件加入到解析的列表，将会被解析。如果文件校验有问题和没有校验文件的数据文件，则不被加入到解析列表，将不会被解析 脚本执行过程中会把数据文件分割成256M大小的文件进行多进程解析。
# 脚本执行方式：python txt_to_sql.py 进程数
# author: renjt

import sys
import time
import multiprocessing
import re
import os
from os.path import join

# 定义数据目录
source_path = os.getcwd()

# 定义检验文件和数据文件的目录和文件的字典
check_dict = {}
file_dict = {}

# 定义字段列表
filed_list_Account = ['Level2ID', 'Level1ID', 'Accounttype', 'Loginaccount', 'Deleteflag', 'Createtime', 'Updatetime']
filed_list_Personal = ['Level2Id', 'Sourceid', 'Sex', 'Age', 'Height', 'Weight']
filed_list_Contact = ['Level2Id', 'Sourceid', 'Mailaddress']
filed_list_Career = ['Level2Id', 'Sourceid', 'Profession', 'Company', 'Position', 'Income', 'Createtime', 'Updatetime']
filed_list_Education = ['Level2Id', 'Sourceid', 'Degree', 'School', 'Createtime', 'Updatetime']
filed_list_Individuality = ['Level2Id', 'Sourceid', 'Nickname', 'Image1']
filed_list_Sociality = ['Level2Id', 'Sourceid', 'Attentions', 'Fans', 'Medals']
filed_list_Finance = ['Level2Id', 'Sourceid', 'Escropay', 'Paytype', 'Ispwdpay', 'Vip_Info', 'Vip_Validity', 'Books',
                      'Migu_Card', 'Migu_Diamond', 'Migu_Beans', 'Internet_Traffic', 'Game_Dot', 'Game_Mi',
                      'Monthly_Ticket', 'Createtime', 'Updatetime']
filed_list_Escrow = ['Level2Id', 'Sourceid', 'Thirdid', 'Thirdidtype', 'Createtime', 'Updatetime']
filed_list_Otherinfo = ['Level2Id', 'Sourceid', 'Muischangepw', 'Receivelev', 'Privacylev', 'Infopercent',
                        'Securitylev', 'Bkimage', 'Ivr', 'Registerip', 'Registerfrom', 'Recomder', 'Isidmp',
                        'Gameaccount', 'Suittype', 'Iswxs', 'Createtime', 'Updatetime']
filed_list_Logistics = ['Level2Id', 'Sourceid', 'Orderid', 'Username', 'Msisdn', 'Provincialcity', 'Detailedaddress',
                        'Postcode', 'Defaultaddressflag', 'Createtime', 'Updatetime']

# 定义字段列表 New Table
filed_list_Behavior = ['Level2Id', 'Sourceid', 'Grade', 'Run_Info', 'Train_Info', 'Best_Running', 'Best_Cycling',
                       'Equipments']
filed_list_Sociality_Attention_Anchor = ['Level2Id', 'Sourceid', 'Id', 'Attention_Anchor_Name', 'Createtime',
                                         'Updatetime']
filed_list_Sociality_Attention_Dvd = ['Level2Id', 'Sourceid', 'Id', 'Attention_Dvd_Name', 'Createtime', 'Updatetime']
filed_list_Sociality_Attention_Edg = ['Level2Id', 'Sourceid', 'Id', 'Attention_Edg_Name', 'Createtime', 'Updatetime']
filed_list_Sociality_Attention_Group = ['Level2Id', 'Sourceid', 'Id', 'Group_Name']
filed_list_Finance_Movie_Ticket = ['Level2Id', 'Sourceid', 'Id', 'Movie_Ticket_Name', 'Movie_Ticket_Balance',
                                   'Movie_Ticket_Period', 'Createtime', 'Updatetime']
filed_list_Finance_Gift_Coupon = ['Level2Id', 'Sourceid', 'Id', 'Gift_Coupon_Name', 'Createtime', 'Updatetime']
filed_list_Finance_Rebates_Ticket = ['Level2Id', 'Sourceid', 'Id', 'Rebates_Ticket_Name', 'Rebates_Ticket_Balance',
                                     'Rebates_Ticket_Period', 'Createtime', 'Updatetime']
filed_list_Finance_Exchange_Ticket = ['Level2Id', 'Sourceid', 'Id', 'Exchange_Ticket_Name', 'Exchange_Ticket_Period',
                                      'Createtime', 'Updatetime']
filed_list_Finance_Vip_Card = ['Level2Id', 'Sourceid', 'Id', 'Vip_Card_Name', 'Vip_Card_Period', 'Createtime',
                               'Updatetime']
filed_list_Finance_Gift = ['Level2Id', 'Sourceid', 'Id', 'Gift_Name', 'Gift_Period', 'Createtime', 'Updatetime']
filed_list_Finance_Ticket = ['Level2Id', 'Sourceid', 'Id', 'Ticket_Name', 'Ticket_Period', 'Createtime', 'Updatetime']
filed_list_Finance_Prize_Usable = ['Level2Id', 'Sourceid', 'Id', 'Prize_Usable_Name', 'Createtime', 'Updatetime']
filed_list_Finance_Prize_Used = ['Level2Id', 'Sourceid', 'Id', 'Prize_Used_Name', 'Createtime', 'Updatetime']
filed_list_Finance_Prize_Expired = ['Level2Id', 'Sourceid', 'Id', 'Prize_Expired_Name', 'Createtime', 'Updatetime']


# 定义获取目录并写入存入字典的函数
def dir_to_dict(dirpath, datatype=''):
    # 子公司简称列表
    # child_list = ['V','G','M','R','G']
    child_list = ['G']

    # 表名列表
    # inf_list = ['Account','Personal','Contact','Career','Education','Individuality','Sociality','Finance','Escrow','Otherinfo','Logistics','Behavior','Sociality_Attention_Anchor','Sociality_Attention_Dvd','Sociality_Attention_Edg','Sociality_Attention_Group','Finance_Movie_Ticket','Finance_Gift_Coupon','Finance_Rebates_Ticket','Finance_Exchange_Ticket','Finance_Vip_Card','Finance_Gift','Finance_Ticket','Finance_Prize_Usable','Finance_Prize_Used','Finance_Prize_Expired']
    inf_list = ['Account', 'Personal', 'Individuality', 'Contact', 'Behavior', 'Sociality', 'Sociality_Attention_Group']

    for j in [i for i in os.walk(dirpath)]:
        # print j
        for child in child_list:
            for inf in inf_list:
                # j=('./data/migu2user', [], ['i_20180124_Account_G_1.txt'])
                for k in j[2]:
                    if (child in k) and (inf in k):
                        file_dict[j[0]] = j[2]
    return file_dict


# 加工列表成指定字符串
def r_fileds(list, filed_value=0):
    fileds = ''
    for value in list:
        # filed = value.strip()
        filed = value
        fd = filed.replace('"', r'\"')

        if fileds == '':
            fileds = fileds + filed
        else:
            if filed_value == 0:
                fileds = fileds + '","' + fd
            elif filed_value == 1:
                fileds = fileds + ',' + filed
            else:
                fileds = ""
    return fileds


# 将txt文本解析成sql语句
def txt_to_sql(f_name, table, list_f, seq='€'):
    # print source_path+'/'+f_name
    read_f = open(source_path + '/' + f_name, 'r')
    # print source_path+'/'+f_name.split('.')[0] + '.sql'
    write_f = open(source_path + '/' + f_name.split('.')[0] + '.sql', 'w')
    # logerror = open('/home/logserv/yly/error.log', 'w')

    for line in read_f:
        line = line.replace("\n", "")
        line_list = line.split(seq)
        if line_list[0] == 'A':
            value_list = line_list[1:]
            write_f.write(
                'insert into %s (%s) values ("%s");\n' % (table, r_fileds(list_f[0:], 1), r_fileds(value_list, 0)))
        elif line_list[0] == 'U':
            pass
        else:
            value_list = line_list[0:]
            write_f.write(
                'insert into %s (%s) values ("%s");\n' % (table, r_fileds(list_f[0:], 1), r_fileds(value_list, 0)))

    read_f.close()
    write_f.close()
    # logerror.close()


# 定义切分数据文件函数默认大小256
def splitfile(fl, filename, sizelimit=32 * 1000 * 1000):
    file_list = []
    size = 0
    # 将a设置成全局变量
    a = 0
    out = open('%s_%03d.tmp' % (filename, a), 'w')
    file_list.append('%s_%03d.tmp' % (filename, a))
    f = open(fl, 'r')
    for line in f:
        # 文件达到256M前，累加处理的所有行的字节数
        size = size + len(line)
        if (size > 32 * 1000 * 1000):
            size = len(line)
            out.close()
            a = a + 1
            out = open('%s_%03d.tmp' % (filename, a), 'w')
            file_list.append('%s_%03d.tmp' % (filename, a))
        out.write(line)
    a = a + 1
    out.close()
    f.close()

    # 返回切分的文件名列表
    return file_list


if __name__ == '__main__':

    # 接受脚本参数作为开启的进程数
    process_count = int(sys.argv[1])
    # 获取当前目录下的所有数据文件
    print
    source_path
    dir_to_dict(source_path)
    print
    dir_to_dict(source_path)
    # print source_path
    pattern = re.compile(r'.*\_\d+\.txt')

    for key in file_dict.keys():
        for f in file_dict[key]:  # f=i_20180124_Account_G_1.txt
            dir_name = key
            print
            dir_name
            print
            f
            # table 中过滤掉无效文件名，只保留数据文件名
            match = pattern.match(f)
            if match:
                # 使用 '_' 将文件名进行分割，['i', '20180124', 'Account', 'G', '2.txt']
                t = f.split('_')
                print
                t
            # table = t[3] + '_' + t[2]  # G_Account
        if len(t) > 5:
            # print len(t)
            table = t[5] + '_' + t[2] + '_' + t[3] + '_' + t[4]
            filed_list_name = eval('filed_list_' + t[2] + '_' + t[3] + '_' + t[4])
            child = t[5]
            print
            "tgt5"
            print
            table
        else:
            print
            "lt5"
            table = t[3] + '_' + t[2]
            child = t[3]
            filed_list_name = eval('filed_list_' + t[2])  # filed_list_Account
            print
            filed_list_name
            # if 'txt' in f:
            # 分割文件

            F_list = splitfile(dir_name + '/' + f, dir_name + '/' + f.split('.')[0])
            pool = multiprocessing.Pool(processes=process_count)

            for fl in F_list:
                tf_name = fl.split('/')[6]
                # tf_name = source_path+'/tmp/'+ tf_name
                pool.apply_async(txt_to_sql, (tf_name, table, filed_list_name))
                pool.close()
                pool.join()
    # os.system('mv /home/logserv/yly/*.sql /home/logserv/yly/sql')
    # os.system('mv /home/logserv/yly/*.tmp /home/logserv/yly/tmp')
    os.system('rm ' + os.getcwd() + '/*.tmp')
