# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\Iwork\DevlopMy\python27work\Syn_pycharm\ui\Query_Youka_LiveUser.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(938, 604)
        self.centralWidget = QtGui.QWidget(MainWindow)
        self.centralWidget.setObjectName(_fromUtf8("centralWidget"))
        self.lbl_query_liveuser = QtGui.QLabel(self.centralWidget)
        self.lbl_query_liveuser.setGeometry(QtCore.QRect(50, 0, 201, 20))
        self.lbl_query_liveuser.setObjectName(_fromUtf8("lbl_query_liveuser"))
        self.date_from_last = QtGui.QDateTimeEdit(self.centralWidget)
        self.date_from_last.setGeometry(QtCore.QRect(120, 30, 194, 22))
        self.date_from_last.setObjectName(_fromUtf8("date_from_last"))
        self.date_end_last = QtGui.QDateTimeEdit(self.centralWidget)
        self.date_end_last.setGeometry(QtCore.QRect(490, 30, 194, 22))
        self.date_end_last.setObjectName(_fromUtf8("date_end_last"))
        self.lbl_date_from_last = QtGui.QLabel(self.centralWidget)
        self.lbl_date_from_last.setGeometry(QtCore.QRect(30, 30, 71, 20))
        self.lbl_date_from_last.setObjectName(_fromUtf8("lbl_date_from_last"))
        self.lbl_date_end_last = QtGui.QLabel(self.centralWidget)
        self.lbl_date_end_last.setGeometry(QtCore.QRect(400, 32, 91, 20))
        self.lbl_date_end_last.setObjectName(_fromUtf8("lbl_date_end_last"))
        self.btn_query = QtGui.QPushButton(self.centralWidget)
        self.btn_query.setGeometry(QtCore.QRect(150, 110, 75, 23))
        self.btn_query.setObjectName(_fromUtf8("btn_query"))
        self.btn_export_excel = QtGui.QPushButton(self.centralWidget)
        self.btn_export_excel.setGeometry(QtCore.QRect(410, 110, 75, 23))
        self.btn_export_excel.setObjectName(_fromUtf8("btn_export_excel"))
        self.tb_liveuser = QtGui.QTableWidget(self.centralWidget)
        self.tb_liveuser.setGeometry(QtCore.QRect(30, 140, 881, 411))
        self.tb_liveuser.setObjectName(_fromUtf8("tb_liveuser"))
        self.tb_liveuser.setColumnCount(0)
        self.tb_liveuser.setRowCount(0)
        self.lbl_date_from = QtGui.QLabel(self.centralWidget)
        self.lbl_date_from.setGeometry(QtCore.QRect(40, 80, 54, 12))
        self.lbl_date_from.setObjectName(_fromUtf8("lbl_date_from"))
        self.date_end = QtGui.QDateTimeEdit(self.centralWidget)
        self.date_end.setGeometry(QtCore.QRect(490, 70, 194, 22))
        self.date_end.setObjectName(_fromUtf8("date_end"))
        self.lbl_date_end = QtGui.QLabel(self.centralWidget)
        self.lbl_date_end.setGeometry(QtCore.QRect(410, 80, 54, 12))
        self.lbl_date_end.setObjectName(_fromUtf8("lbl_date_end"))
        self.date_from = QtGui.QDateTimeEdit(self.centralWidget)
        self.date_from.setGeometry(QtCore.QRect(120, 70, 194, 22))
        self.date_from.setObjectName(_fromUtf8("date_from"))
        self.btn_make_chart = QtGui.QPushButton(self.centralWidget)
        self.btn_make_chart.setGeometry(QtCore.QRect(730, 40, 101, 41))
        self.btn_make_chart.setObjectName(_fromUtf8("btn_make_chart"))
        MainWindow.setCentralWidget(self.centralWidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.lbl_query_liveuser.setText(_translate("MainWindow", "本工具提供优卡活跃用户数查询：", None))
        self.lbl_date_from_last.setText(_translate("MainWindow", "上周起始日期", None))
        self.lbl_date_end_last.setText(_translate("MainWindow", "上周结束日期", None))
        self.btn_query.setText(_translate("MainWindow", "查询", None))
        self.btn_export_excel.setText(_translate("MainWindow", "导出到Excel", None))
        self.lbl_date_from.setText(_translate("MainWindow", "起始日期", None))
        self.lbl_date_end.setText(_translate("MainWindow", "结束日期", None))
        self.btn_make_chart.setText(_translate("MainWindow", "生成EXCEL图表", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

