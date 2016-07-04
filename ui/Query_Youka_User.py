# -*- coding: utf-8 -*-

"""
Module implementing Youka_User_Window.
"""

import sys
import datetime
from PyQt4.QtCore import QDateTime
from PyQt4.QtCore import pyqtSignature
from PyQt4.QtGui import QMainWindow
from PyQt4.QtGui import QMessageBox
from PyQt4.QtGui import QTableWidgetItem, QAbstractItemView
from PyQt4.QtGui import QFileDialog
import _mssql
import pymssql
import collections
import decimal
from helper import tool
from dev_config import Youka

from .Ui_Query_Youka_User import Ui_Youka_User_Window


class Youka_User_Window(QMainWindow, Ui_Youka_User_Window):
    """
    Class documentation goes here.
    """

    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        QMainWindow.__init__(self, parent)
        self.setupUi(self)

        # init event
        # self.btn_Query.clicked.connect(self.on_btn_Query_clicked)

        # 获得系统默认编码格式
        self.sysCharType = sys.getfilesystemencoding()

        self.data_list_youka = None

        now_time = str(datetime.date.today()) + ' 00:00:00'
        from_time_default = get_default_time(-1)
        self.date_from.setDateTime(QDateTime.fromString(from_time_default, 'yyyy-MM-dd hh:mm:ss'))
        self.date_end.setDateTime(QDateTime.fromString(now_time, 'yyyy-MM-dd hh:mm:ss'))
        # init table_results
        self.table_results.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.table_results.setColumnCount(3)
        self.table_results.setRowCount(0)
        self.table_results.setHorizontalHeaderLabels([u'学校代码', u'学校名称', u'增长数量'])

    @pyqtSignature("")
    def on_btn_Query_clicked(self):
        """
        Slot documentation goes here.
        """
        self.data_list_youka = None
        self.table_results.clearContents()

        if (self.date_from.date() >= self.date_end.date()):
            QMessageBox.information(self, "QMessageBox.information()", u'结束时间不能小于或等于开始时间!')
            return
        if (self.date_from.date().addMonths(2) < self.date_end.date()):
            QMessageBox.information(self, "QMessageBox.information()", u'查询时间不能超过两个月！')
            return
        # date_from = '2016-6-26 00:00:00'
        date_from = self.date_from.text().replace('/', '-')
        # date_to = '2016-6-27 00:00:00'
        date_to = self.date_end.text().replace('/', '-')

        sqlstr = "select sc.*,cc.allcount from (select SchoolCode,SchoolName from Schools s where s.IsEnable=1 and s.AppCode='AppCloudPlat') sc left join (select SchoolCode , COUNT(*) allcount  from Customers where CreateTime between '{}' and '{}' group by SchoolCode ) cc on sc.SchoolCode=cc.SchoolCode order by cc.allcount desc".format(
            date_from, date_to)
        # print sqlstr
        self.data_list_youka = runsql(Youka.HOST, Youka.ACCOUNT, Youka.PASSWORD, Youka.DB, sqlstr)
        self.table_results.setRowCount(len(self.data_list_youka))
        self.statusBar().showMessage(u'总: {} 记录'.format(len(self.data_list_youka)))
        if self.data_list_youka:
            i = 0
            for item in self.data_list_youka:
                data_item = QTableWidgetItem(item['SchoolCode'])
                self.table_results.setItem(i, 0, data_item)

                data_item = QTableWidgetItem(item['SchoolName'])
                self.table_results.setItem(i, 1, data_item)

                data_item = QTableWidgetItem(str(item['allcount']))
                self.table_results.setItem(i, 2, data_item)
                i += 1

    @pyqtSignature("")
    def on_btn_ExportCsv_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        # raise NotImplementedError

        if self.data_list_youka is not None:
            directory = QFileDialog.getExistingDirectory(self, "QFileDialog.getExistingDirectory()", 'unknown para')

            filename = directory + '\\' + self.date_from.text().replace('/', '_').replace(':', '_').replace(' ',
                                                                                                            '_') + '__' + self.date_end.text().replace(
                '/', '_').replace(':', '_').replace(' ', '_')
            # QMessageBox.information(self, "QMessageBox.information()", filename)
            tool.export_csv(self.data_list_youka, filename, Youka.CSV_HEAD, Youka.FIELDS)
            QMessageBox.information(self, "QMessageBox.information()", u'导出到程序目录{}成功!'.format(directory))

        else:
            QMessageBox.information(self, "QMessageBox.information()", u'数据查询为空!')
    


def get_default_time(add_days=0):
    return str(datetime.date.today() + datetime.timedelta(days=add_days)) + ' 00:00:00'


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

