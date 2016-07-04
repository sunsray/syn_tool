# syn_tool
Use Python 2.7.3, Pyqt4,xlsxwriter to  query data and generate Excel chart

Remark: dev_config.py is a file  like:

#!/usr/bin/python
# -*- coding: utf-8 -*-
class Config:
    AUTHOR = u'sunsray'
    MEMU_ABOUT_MESSAGE = u'\n欢迎提出宝贵意见'
    DISABLE_TIME = 3  # Month


class Youka(Config):
    HOST = 'xxx.xxx.com:PORT'
    ACCOUNT = 'ACCOUNT'
    PASSWORD = 'PASSWORD'
    DB = 'dreams_mobile_plat'
    CSV_HEAD = ['SchoolCode', 'SchoolName', 'increaseCount']
    FIELDS = ['SchoolCode', 'SchoolName', 'allcount']

    LIVEUSER_SQL = '''
      select  sc.Area ,sc.SchoolCode ,sc.SchoolName,cc.currentUser,nc.AprilOneUser,cl.LastWeekCount,clnow.currentWeekCount,(clnow.currentWeekCount-cl.LastWeekCount) as 'Minus' from (
      select  s.Area,s.CreateTime,s.SchoolName,s.SchoolCode from schools s where s.IsEnable=1 and s.AppCode='AppCloudPlat'
       ) sc left join (
       select schoolcode,COUNT(*) currentUser from Customers group by SchoolCode)cc
       on sc.SchoolCode=cc.SchoolCode
       left join (
       select schoolcode,COUNT(*) AprilOneUser from Customers where CreateTime<'2016-04-01 00:00:00' group by SchoolCode
       )nc on sc.SchoolCode=nc.SchoolCode
       left join (
       select A.SchoolCode,SUM(A.Count) as LastWeekCount from (
      select *  from ClickLogs  where ModifyTime
      between   '{}' and '{}'  )A  group by A.SchoolCode
      ) cl on sc.SchoolCode=cl.SchoolCode
      left join (
      select A.SchoolCode,SUM(A.Count) as currentWeekCount from (
      select *  from ClickLogs  where ModifyTime
      between '{}' and '{}' )A  group by A.SchoolCode
      ) clnow on sc.SchoolCode =clnow.SchoolCode

      order by currentUser desc,Area'''
    FUNC_CLICK_SQL = ' select FuncName,SUM(Count) counts from ClickLogs group by FuncName'
