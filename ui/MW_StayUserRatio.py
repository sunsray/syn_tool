# -*- coding: utf-8 -*-

"""
Module implementing MW_StayUserRatio.
"""

from PyQt4.QtCore import pyqtSignature
from PyQt4.QtGui import QDialog
from PyQt4.QtCore import QDateTime
from .Ui_StayUserRatio import Ui_Dialog
from helper import tool
import datetime, time


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
        days = (self.dt_EndTime_StayUser.date().toPyDate() - self.dt_FromTime_StayUser.date().toPyDate()).days + 1
        today = datetime.date.today()
        ar = [str(today + datetime.timedelta(-_)) for _ in range(1, days)]

        ar.sort()
        print ar

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
                    row_data.append('ok')
            print row_data

    @pyqtSignature("")
    def on_btn_export_StayuserRatio_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        raise NotImplementedError

    def str_to_date(self, str):
        t = time.strptime(str, "%Y-%m-%d")
        y, m, d = t[0:3]
        return datetime.datetime(y, m, d)
