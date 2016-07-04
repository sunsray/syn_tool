# -*- coding: utf-8 -*-

"""
Module implementing MW_Query_Youka_LiveUser.
"""

from __future__ import division

from PyQt4.QtCore import pyqtSignature
from PyQt4.QtGui import QMainWindow
from PyQt4.QtGui import QAbstractItemView
from PyQt4.QtGui import QTableWidgetItem
from PyQt4.QtGui import QMessageBox
from PyQt4.QtGui import QFileDialog
from PyQt4.QtCore import QDateTime
from .Ui_Query_Youka_LiveUser import Ui_MainWindow
from dev_config import Youka
from helper import tool
from pickle_dump import make_all_func_clik
import xlsxwriter
import calendar, datetime
import os,sys

class MW_Query_Youka_LiveUser(QMainWindow, Ui_MainWindow):
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

        self.run_path = sys.argv[0]
        self.init_date()
        self.lst_youka_liveuser = None
        # init table_results
        self.tb_liveuser.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tb_liveuser.setColumnCount(9)
        self.tb_liveuser.setRowCount(0)
        self.tb_liveuser.setHorizontalHeaderLabels(
            [u'大区', u'代码', u'学校', u'当前用户数', u'4月1号用户数', u'上周点击量', u'本周点击量', u'差额', u'本周点击率'])

    # 初始化日期控件为   上周时间段：上上周六 至上周六  本周时间段：上周六 至本周六
    def init_date(self):
        date_from_last = str(tool.get_lastweek_someday(calendar.MONDAY) + datetime.timedelta(days=-9)) + ' 00:00:00'
        self.date_from_last.setDateTime(QDateTime.fromString(date_from_last, 'yyyy-MM-dd hh:mm:ss'))
        date_end_last = str(tool.get_lastweek_someday(calendar.MONDAY) + datetime.timedelta(days=-2)) + ' 00:00:00'
        self.date_end_last.setDateTime(QDateTime.fromString(date_end_last, 'yyyy-MM-dd hh:mm:ss'))
        date_from = str(tool.get_lastweek_someday(calendar.MONDAY) + datetime.timedelta(days=-2)) + ' 00:00:00'
        self.date_from.setDateTime(QDateTime.fromString(date_from, 'yyyy-MM-dd hh:mm:ss'))
        date_end = str(tool.get_current_week_someday(5)) + ' 00:00:00'
        self.date_end.setDateTime(QDateTime.fromString(date_end, 'yyyy-MM-dd hh:mm:ss'))

    @pyqtSignature("")
    def on_btn_query_clicked(self):
        """
        Slot documentation goes here.
        """

        self.tb_liveuser.clearContents()
        date_from_last = self.date_from_last.text().replace('/', '-')
        date_end_last = self.date_end_last.text().replace('/', '-')
        date_from = self.date_from.text().replace('/', '-')
        date_end = self.date_end.text().replace('/', '-')
        if (self.date_from.date() >= self.date_end.date() or self.date_from_last.date() >= self.date_end_last.date()):
            QMessageBox.information(self, "QMessageBox.information()", u'结束时间不能小于或等于开始时间!')
            return
        if (self.date_from.date().addMonths(2) < self.date_end.date() or self.date_from_last.date().addMonths(
                2) < self.date_end_last.date()):
            QMessageBox.information(self, "QMessageBox.information()", u'查询时间不能超过两个月！')
            return
        sqlstr = Youka.LIVEUSER_SQL.format(date_from_last, date_end_last, date_from, date_end)
        # print str((self.date_end.date().addDays(-1)).toString('yyyy_MM_dd'))
        self.lst_youka_liveuser = tool.runsql(Youka.HOST, Youka.ACCOUNT, Youka.PASSWORD, Youka.DB, sqlstr)
        self.tb_liveuser.setRowCount(len(self.lst_youka_liveuser))
        self.statusBar().showMessage(u'总: {} 记录'.format(len(self.lst_youka_liveuser)))
        if self.lst_youka_liveuser:
            i = 0
            for item in self.lst_youka_liveuser:
                if item['Area'] == 'HuaBei':
                    item['Area'] = u'华北'
                elif item['Area'] == 'HuaDong':
                    item['Area'] = u'华东'
                elif item['Area'] == 'HuaZhong':
                    item['Area'] = u'华中'
                elif item['Area'] == 'HuaNan':
                    item['Area'] = u'华南'
                elif item['Area'] == 'XiBei':
                    item['Area'] = u'西北'
                elif item['Area'] == 'DongBei':
                    item['Area'] = u'东北'
                elif item['Area'] == 'XiNan':
                    item['Area'] = u'西南'
                else:
                    item['Area'] = u'未知'

                item['AprilOneUser'] = item['AprilOneUser'] is not None and item['AprilOneUser'] or 0
                item['LastWeekCount'] = item['LastWeekCount'] is not None and item['LastWeekCount'] or 0
                item['currentWeekCount'] = item['currentWeekCount'] is not None and item['currentWeekCount'] or 0
                item['currentUser'] = item['currentUser'] is not None and item['currentUser'] or 0

                data_item = QTableWidgetItem(item['Area'])
                self.tb_liveuser.setItem(i, 0, data_item)

                data_item = QTableWidgetItem(item['SchoolCode'])
                self.tb_liveuser.setItem(i, 1, data_item)

                data_item = QTableWidgetItem(item['SchoolName'])
                self.tb_liveuser.setItem(i, 2, data_item)

                data_item = QTableWidgetItem(str(item['currentUser']))
                self.tb_liveuser.setItem(i, 3, data_item)

                data_item = QTableWidgetItem(str(item['AprilOneUser']))
                self.tb_liveuser.setItem(i, 4, data_item)

                data_item = QTableWidgetItem(str(item['LastWeekCount']))
                self.tb_liveuser.setItem(i, 5, data_item)

                data_item = QTableWidgetItem(str(item['currentWeekCount']))
                self.tb_liveuser.setItem(i, 6, data_item)

                if item['Minus'] is None:
                    item['Minus'] = item['currentWeekCount'] - item['LastWeekCount']
                data_item = QTableWidgetItem(str(item['Minus']))
                self.tb_liveuser.setItem(i, 7, data_item)

                if int(item['currentUser']) > 0:
                    item['click_rate'] = round(item['currentWeekCount'] / item['currentUser'], 2)
                else:
                    item['click_rate'] = None

                # print '{}:{}/{}'.format(item['SchoolCode'],item['currentWeekCount'],item['currentUser'])
                data_item = QTableWidgetItem(str(item['click_rate']))
                self.tb_liveuser.setItem(i, 8, data_item)
                i += 1

    @pyqtSignature("")
    def on_btn_make_chart_clicked(self):
        """
        Slot documentation goes here.
        """
        # 选择存放目录
        directory = QFileDialog.getExistingDirectory(self, "QFileDialog.getExistingDirectory()", 'unknown para')

        filename = directory + '\\' + 'Chart' + self.date_from.date().toString('yyyy_MM_dd') + '__' + (
            self.date_end.date().addDays(-1)).toString('yyyy_MM_dd') + '.xlsx'
        try:
            res = make_all_func_clik(str(filename))
        except Exception as e:
            QMessageBox.information(self, "QMessageBox.information()", str(e) + os.getcwd()+sys.argv[0])
        if res > 0:
            QMessageBox.information(self, "QMessageBox.information()", u'导出到目录{}成功!'.format(directory))
        else:
            QMessageBox.information(self, "QMessageBox.information()", u'本周记录已添加!')

    @pyqtSignature("")
    def on_btn_export_excel_clicked(self):
        """
        Slot documentation goes here.
        """
        if self.lst_youka_liveuser:
            # 选择存放目录
            directory = QFileDialog.getExistingDirectory(self, "QFileDialog.getExistingDirectory()", 'unknown para')
            filename = directory + '\\' + 'Youka' + self.date_from.date().toString('yyyy_MM_dd') + '__' + (
                self.date_end.date().addDays(-1)).toString('yyyy_MM_dd') + '.xlsx'

            # Create a workbook and add a worksheet.
            workbook = xlsxwriter.Workbook(str(filename))
            worksheet = workbook.add_worksheet('liveUser')

            # Add a bold format to use to highlight cells.
            bold = workbook.add_format({'bold': 1})

            # Adjust the column width.
            worksheet.set_column(1, 1, 15)
            worksheet.set_column(1, 2, 15)
            worksheet.set_column(1, 3, 20)
            worksheet.set_column(1, 4, 15)
            worksheet.set_column(1, 5, 15)
            worksheet.set_column(1, 6, 15)
            worksheet.set_column(1, 7, 15)

            # Write  headers.
            worksheet.write('A1', u'大区')
            worksheet.write('B1', u'代码')
            worksheet.write('C1', u'学校')
            worksheet.write('D1', u'当前用户数')
            worksheet.write('E1', u'4月1号用户数')
            worksheet.write('F1', u'上周点击量')
            worksheet.write('G1', u'本周点击量')
            worksheet.write('H1', u'差额')
            worksheet.write('I1', u'本周点击率')

            # Start from the first cell below the headers.
            row = 1
            col = 0

            for item in self.lst_youka_liveuser:
                worksheet.write_string(row, col, item['Area'])
                worksheet.write_string(row, col + 1, item['SchoolCode'])
                worksheet.write_string(row, col + 2, item['SchoolName'])
                worksheet.write(row, col + 3, item['currentUser'])
                worksheet.write(row, col + 4, item['AprilOneUser'])
                worksheet.write(row, col + 5, item['LastWeekCount'])
                worksheet.write(row, col + 6, item['currentWeekCount'])
                worksheet.write(row, col + 7, item['Minus'])
                worksheet.write(row, col + 8, item['click_rate'])
                row += 1

            workbook.close()
            QMessageBox.information(self, "QMessageBox.information()", u'导出到目录{}成功!'.format(directory))
        else:
            QMessageBox.information(self, "QMessageBox.information()", u'数据查询为空!')

            # @pyqtSignature("QDate")
            # def on_date_end_dateChanged(self, date):
            #     """
            #     Slot documentation goes here.
            #
            #     @param date DESCRIPTION
            #     @type QDate
            #     """
            #     """
            #     选取本周结束时间时触发，
            #     """
