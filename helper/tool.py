#!/usr/bin/python
# -*- coding: utf-8 -*-
import csv
import codecs
import _mssql
import pymssql
import collections
import decimal
import datetime


# 获取上一个周几，如周五，星期五
# parm   like calendar.FRIDAY
def get_lastweek_someday(day):
    re_date = datetime.date.today()
    oneday = datetime.timedelta(days=1)

    while re_date.weekday() != day:
        re_date -= oneday
    return re_date

#获取本周周几
# 周一为0, 周日为6
def get_current_week_someday(station):
    today = datetime.date.today()
    weekday = today.weekday()
    delta = datetime.timedelta(station - weekday)
    return_date = today + delta
    return return_date


def export_csv(data_list, filename, fieldnames, fields):
    with open(filename + '.csv', 'w') as csvfile:
        csvfile.write(codecs.BOM_UTF8)
        writer = csv.DictWriter(csvfile, fieldnames=fields)

        writer.writeheader()
        if data_list:
            for item in data_list:

                item_obj = {}
                for field in fields:
                    item_obj[field] = (item[field] is not None) and item[field] or 0
                    if field == 'SchoolName':
                        item_obj[field] = item[field].encode('utf-8')
                        # print item_obj

                writer.writerow(item_obj)  # 'Name': item['Name']


def runsql(server, user, pwd, db, sqlstr):
    l = []
    with pymssql.connect(server, user, pwd, db) as conn:
        with conn.cursor(as_dict=True) as cursor:
            cursor.execute(sqlstr)
            for row in cursor:
                # print('----------------------------')
                # print(row)
                l.append(row)
                # try。。。
                # 声明一个队列，依次入队或者一个list 然后展示
                # print("ID=%d, FeeState=%s" % (row['ID'], row['FeeState']))
    return l
