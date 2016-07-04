# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\Iwork\DevlopMy\python27work\Syn_pycharm\ui\Query_Youka_User.ui'
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

class Ui_Youka_User_Window(object):
    def setupUi(self, Youka_User_Window):
        Youka_User_Window.setObjectName(_fromUtf8("Youka_User_Window"))
        Youka_User_Window.resize(800, 600)
        self.centralWidget = QtGui.QWidget(Youka_User_Window)
        self.centralWidget.setObjectName(_fromUtf8("centralWidget"))
        self.table_results = QtGui.QTableWidget(self.centralWidget)
        self.table_results.setGeometry(QtCore.QRect(30, 70, 711, 461))
        self.table_results.setObjectName(_fromUtf8("table_results"))
        self.table_results.setColumnCount(0)
        self.table_results.setRowCount(0)
        self.layoutWidget = QtGui.QWidget(self.centralWidget)
        self.layoutWidget.setGeometry(QtCore.QRect(40, 0, 671, 71))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.gridLayout = QtGui.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(5, 5, 10, 5)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.date_from = QtGui.QDateTimeEdit(self.layoutWidget)
        self.date_from.setObjectName(_fromUtf8("date_from"))
        self.gridLayout.addWidget(self.date_from, 0, 1, 2, 1)
        self.btn_Query = QtGui.QPushButton(self.layoutWidget)
        self.btn_Query.setObjectName(_fromUtf8("btn_Query"))
        self.gridLayout.addWidget(self.btn_Query, 1, 2, 2, 1)
        self.btn_ExportCsv = QtGui.QPushButton(self.layoutWidget)
        self.btn_ExportCsv.setObjectName(_fromUtf8("btn_ExportCsv"))
        self.gridLayout.addWidget(self.btn_ExportCsv, 1, 3, 2, 1)
        self.lbl_EndTime = QtGui.QLabel(self.layoutWidget)
        self.lbl_EndTime.setObjectName(_fromUtf8("lbl_EndTime"))
        self.gridLayout.addWidget(self.lbl_EndTime, 2, 0, 1, 1)
        self.date_end = QtGui.QDateTimeEdit(self.layoutWidget)
        self.date_end.setObjectName(_fromUtf8("date_end"))
        self.gridLayout.addWidget(self.date_end, 2, 1, 1, 1)
        self.lbl_StartTime = QtGui.QLabel(self.layoutWidget)
        self.lbl_StartTime.setObjectName(_fromUtf8("lbl_StartTime"))
        self.gridLayout.addWidget(self.lbl_StartTime, 0, 0, 2, 1)
        Youka_User_Window.setCentralWidget(self.centralWidget)

        self.retranslateUi(Youka_User_Window)
        QtCore.QMetaObject.connectSlotsByName(Youka_User_Window)

    def retranslateUi(self, Youka_User_Window):
        Youka_User_Window.setWindowTitle(_translate("Youka_User_Window", "优卡用户查询", None))
        self.btn_Query.setText(_translate("Youka_User_Window", "查询", None))
        self.btn_ExportCsv.setText(_translate("Youka_User_Window", "导出", None))
        self.lbl_EndTime.setText(_translate("Youka_User_Window", "结束时间：", None))
        self.lbl_StartTime.setText(_translate("Youka_User_Window", "起始时间：", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Youka_User_Window = QtGui.QMainWindow()
    ui = Ui_Youka_User_Window()
    ui.setupUi(Youka_User_Window)
    Youka_User_Window.show()
    sys.exit(app.exec_())

