# -*- coding: utf-8 -*-

"""
Module implementing MW_StayUserRatio.
"""

from PyQt4.QtCore import pyqtSignature
from PyQt4.QtGui import QDialog
from PyQt4.QtGui import QMessageBox
from PyQt4.QtGui import QFileDialog
from PyQt4.QtCore import QDateTime
from .Ui_StayUserRatio import Ui_Dialog
from helper import tool
import datetime, time
from dev_config import Youka
from helper import tool
import xlsxwriter


class MW_StayUserRatio(QDialog, Ui_Dialog):
    """
    Class documentation goes here.
    """

    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        QDialog.__init__(self, parent)
        self.setupUi(self)

        self.init_date()

    def init_date(self):
        today = datetime.date.today()
        date_end = str(today) + ' 00:00:00'
        self.dt_EndTime_StayUser.setDateTime(QDateTime.fromString(date_end, 'yyyy-MM-dd hh:mm:ss'))
        from_day = str(today + datetime.timedelta(-14)) + ' 00:00:00'
        self.dt_FromTime_StayUser.setDateTime(QDateTime.fromString(from_day, 'yyyy-MM-dd hh:mm:ss'))

    @pyqtSignature("")
    def on_btn_Quey_StayUser_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        # raise NotImplementedError
        # self.query_date_from = self.dt_FromTime_StayUser.text()
        # self.query_date_end = self.dt_EndTime_StayUser.text()
        # print self.query_date_from
        #
        # print  type((self.dt_FromTime_StayUser.date().toPyDate() - self.dt_EndTime_StayUser.date().toPyDate()).days)
        self.fromdate = self.dt_FromTime_StayUser.date().toPyDate()
        self.enddate = self.dt_EndTime_StayUser.date().toPyDate()
        days = (self.enddate - self.fromdate).days + 1

        ar = [str(self.enddate + datetime.timedelta(-_)) for _ in range(1, days)]
        self.ar_header = [(self.enddate + datetime.timedelta(-_)).strftime('%m.%d') for _ in range(1, days)]
        self.ar_header.sort()

        ar.sort()
        print ar
        threads = []
        global data
        data = []
        self.shell_data = []
        for _ in ar:
            row_data = []
            _2 = self.str_to_date(_)

            for __ in ar:
                __2 = self.str_to_date(__)
                if _2 == __2:
                    row_data.append('100%')
                elif __2 < _2:
                    row_data.append('--')
                else:
                    tag1, tag2 = _, ar[ar.index(_) + 1]
                    if __ == ar[-1]:
                        tag3 = __
                        __2plus = __2 + datetime.timedelta(1)
                        tag4 = __2plus.strftime('%Y-%m-%d')
                    else:
                        tag3, tag4 = __, ar[ar.index(__) + 1]
                    # row_data.append(__ + ":" + 'OK')
                    # print '%s-%s : %s-%s' % (tag1, tag2, tag3, tag4)
                    sql_str = Youka.STAY_USER_SQL.format(tag1, tag2, tag3, tag4, tag1, tag2, )
                    # self.dat_result = tool.runsql(Youka.HOST, Youka.ACCOUNT, Youka.PASSWORD, Youka.DB, sql_str)
                    # print '%s-%s : %s-%s  留存率：%s' % (tag1, tag2, tag3, tag4, self.dat_result[0]['stay_ratio'].strip())
                    t = QueryThread(sql_str, _, __, data)
                    t.start()
                    threads.append(t)

            print row_data
            self.shell_data.append(row_data)
            # data.append({_: row_data})
            print '#' * 60
        for t in threads:
            t.join()
        print 'self.shell_data:'
        print self.shell_data
        print "main Thread"
        print data
        maked_data = self.print_data(ar, data)

        print 'maked data:'
        print maked_data

        for item in self.shell_data:
            item.extend(maked_data[self.shell_data.index(item)])

        print "after inject data:"
        print self.shell_data

    def print_data(self, ar, data):
        lst = []
        for item in ar:
            a2 = [_ for _ in data if item in _]
            a22 = [_ for _ in a2 if _.split("|")[0] == item]
            a22_format = [_.split('|')[1] for _ in a22]
            a22_format.sort()
            a22_format = [_.split(":")[1] for _ in a22_format]
            print '%s%s留存率%s' % ('*' * 40, item, '*' * 40)
            print a22_format

            lst.append(a22_format)
        return lst

    @pyqtSignature("")
    def on_btn_export_StayuserRatio_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        # raise NotImplementedError
        if self.shell_data:
            # 选择存放目录
            directory = QFileDialog.getExistingDirectory(self, "QFileDialog.getExistingDirectory()", 'unknown para')
            filename = directory + '\\' + 'Yo_stayUserRatio' + self.fromdate.strftime(
                '%Y-%m-%d') + '__' + self.enddate.strftime(
                '%Y-%m-%d') + '.xlsx'

            # Create a workbook and add a worksheet.
            workbook = xlsxwriter.Workbook(str(filename))
            worksheet = workbook.add_worksheet('stayRatio')
            worksheet.set_column(1, 1, 13)
            worksheet.set_column(0, 0, 6)

            format = workbook.add_format()
            format.set_pattern(1)  # This is optional when using a solid fill.
            format.set_bg_color('orange')
            format.set_font_size(11)
            format.set_bold()

            format2 = workbook.add_format()
            format2.set_font_size(18)

            format3 = workbook.add_format()
            format3.set_font_size(13)
            format3.set_bold()

            format_silver = workbook.add_format()
            format_silver.set_bg_color('silver')

            # Add a bold format to use to highlight cells.
            bold = workbook.add_format({'bold': 1})

            worksheet.write(0, 0, u'留存用户分析', format2)
            worksheet.write(1, 0, u'日期', format)
            worksheet.write(1, 1, u'新增用户数', format)
            c = 2
            # Write  headers.
            for _ in self.ar_header:
                worksheet.write(1, c, _ + "\n" + '留存率', format)
                worksheet.set_column(c, c, 13)
                c += 1
            # Write columns headers
            r = 2
            for _ in self.ar_header:
                worksheet.write(r, 0, _, format)
                r += 1

            # Start from the first cell below the headers.
            row = 2
            col = 2

            for item in self.shell_data:
                worksheet.write_row(row, col, tuple(item), format_silver)
                row += 1

            # Create a format to use in the merged range.
            merge_format = workbook.add_format({
                'bold': 1,
                'border': 1,
                'align': 'center',
                'valign': 'top',
                'fg_color': 'yellow'})
            memo = u'''注：1．留存用户：是指某段时间的新增用户在下个时间段再次启动应用的用户。
                          2．这部分用户占当时新增用户的比例即为留存率。留存率=新增用户中登录用户数/新增用户数*100%
                          3. 例如：次日留存率：（当天新增的用户中，在第2天还登录的用户数）/第一天新增总用户数；
                           第3日留存率：（第一天新增用户中，在往后的第3天还有登录的用户数）/第一天新增总用户数；'''
            worksheet.merge_range('B19:H26', memo, merge_format)

            workbook.close()
            QMessageBox.information(self, "QMessageBox.information()", u'导出到目录{}成功!'.format(directory))
        else:
            QMessageBox.information(self, "QMessageBox.information()", u'数据查询为空!')

    """
    常用时间转换：
    1. 获得前三天时间
    print datetime.datetime.now()
    print datetime.datetime.now() - datetime.timedelta(days=3)

    print datetime.date.tody()
    print datetime.date.tody() - datetime.timedelta(days=3)

    2.格式转换
    dt = datetime.datetime.now() 时间数组格式
    dt.strftime("%Y-%m-%d" %H:%M:%S) 转成字符串

    3、字符串---》日期
    dt1 = '2016-10-15'
    dt2 = datetime.datetime.strptime(dt1, '%Y-%m-%d').date()
    """

    def str_to_date(self, str):
        t = time.strptime(str, "%Y-%m-%d")
        y, m, d = t[0:3]
        return datetime.datetime(y, m, d)


from threading import Thread


# 利用多线程 将数据库查询结果 存储到  全局的数组

class QueryThread(Thread):
    def __init__(self, sql_str, _, __, lst):
        Thread.__init__(self)
        self.sql_str = sql_str
        self.data_key = _ + "|" + __
        self.lst = lst

    def run(self):
        self.handle()

    def handle(self):
        dat_result = tool.testcon(Youka.HOST, Youka.ACCOUNT, Youka.PASSWORD, Youka.DB, self.sql_str)
        # print '%s-%s : %s-%s  留存率：%s' % (tag1, tag2, tag3, tag4, self.dat_result[0]['stay_ratio'].strip())
        print ' 留存率：%s' % (dat_result[0].strip())
        stay_ratio = dat_result[0].strip()
        self.lst.append(self.data_key + ':' + stay_ratio)
