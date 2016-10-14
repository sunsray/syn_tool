# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Administrator\PycharmProjects\syn_tool\ui\MainWindow.ui'
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
        MainWindow.resize(946, 629)
        self.centralWidget = QtGui.QWidget(MainWindow)
        self.centralWidget.setObjectName(_fromUtf8("centralWidget"))
        self.gridLayoutWidget = QtGui.QWidget(self.centralWidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 0, 931, 601))
        self.gridLayoutWidget.setObjectName(_fromUtf8("gridLayoutWidget"))
        self.MainGridLayout = QtGui.QGridLayout(self.gridLayoutWidget)
        self.MainGridLayout.setObjectName(_fromUtf8("MainGridLayout"))
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtGui.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 946, 23))
        self.menuBar.setObjectName(_fromUtf8("menuBar"))
        self.menu_query = QtGui.QMenu(self.menuBar)
        self.menu_query.setObjectName(_fromUtf8("menu_query"))
        self.menu_about = QtGui.QMenu(self.menuBar)
        self.menu_about.setObjectName(_fromUtf8("menu_about"))
        MainWindow.setMenuBar(self.menuBar)
        self.ac_query_youka_user = QtGui.QAction(MainWindow)
        self.ac_query_youka_user.setObjectName(_fromUtf8("ac_query_youka_user"))
        self.actionAbout = QtGui.QAction(MainWindow)
        self.actionAbout.setObjectName(_fromUtf8("actionAbout"))
        self.ac_quit = QtGui.QAction(MainWindow)
        self.ac_quit.setObjectName(_fromUtf8("ac_quit"))
        self.ac_query_youka_live = QtGui.QAction(MainWindow)
        self.ac_query_youka_live.setObjectName(_fromUtf8("ac_query_youka_live"))
        self.ac_query_StayUser = QtGui.QAction(MainWindow)
        self.ac_query_StayUser.setObjectName(_fromUtf8("ac_query_StayUser"))
        self.menu_query.addAction(self.ac_query_youka_user)
        self.menu_query.addAction(self.ac_query_youka_live)
        self.menu_query.addAction(self.ac_query_StayUser)
        self.menu_about.addAction(self.actionAbout)
        self.menu_about.addAction(self.ac_quit)
        self.menuBar.addAction(self.menu_query.menuAction())
        self.menuBar.addAction(self.menu_about.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.menu_query.setTitle(_translate("MainWindow", "查询", None))
        self.menu_about.setTitle(_translate("MainWindow", "关于", None))
        self.ac_query_youka_user.setText(_translate("MainWindow", "优卡新增用户查询", None))
        self.actionAbout.setText(_translate("MainWindow", "About", None))
        self.ac_quit.setText(_translate("MainWindow", "退出", None))
        self.ac_query_youka_live.setText(_translate("MainWindow", "优卡活跃用户查询", None))
        self.ac_query_StayUser.setText(_translate("MainWindow", "用户留存率查询", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

