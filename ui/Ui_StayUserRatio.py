# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Administrator\PycharmProjects\syn_tool\ui\StayUserRatio.ui'
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

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(812, 582)
        font = QtGui.QFont()
        font.setPointSize(10)
        Dialog.setFont(font)
        Dialog.setSizeGripEnabled(True)
        self.lbl_fromTime_StayUser = QtGui.QLabel(Dialog)
        self.lbl_fromTime_StayUser.setGeometry(QtCore.QRect(60, 50, 81, 16))
        self.lbl_fromTime_StayUser.setObjectName(_fromUtf8("lbl_fromTime_StayUser"))
        self.lbl_endTime_StayUser = QtGui.QLabel(Dialog)
        self.lbl_endTime_StayUser.setGeometry(QtCore.QRect(410, 50, 71, 16))
        self.lbl_endTime_StayUser.setObjectName(_fromUtf8("lbl_endTime_StayUser"))
        self.lbl_title_StayUser = QtGui.QLabel(Dialog)
        self.lbl_title_StayUser.setGeometry(QtCore.QRect(40, 0, 221, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_title_StayUser.setFont(font)
        self.lbl_title_StayUser.setObjectName(_fromUtf8("lbl_title_StayUser"))
        self.dt_FromTime_StayUser = QtGui.QDateTimeEdit(Dialog)
        self.dt_FromTime_StayUser.setGeometry(QtCore.QRect(150, 50, 194, 22))
        self.dt_FromTime_StayUser.setObjectName(_fromUtf8("dt_FromTime_StayUser"))
        self.dt_EndTime_StayUser = QtGui.QDateTimeEdit(Dialog)
        self.dt_EndTime_StayUser.setGeometry(QtCore.QRect(500, 50, 194, 22))
        self.dt_EndTime_StayUser.setObjectName(_fromUtf8("dt_EndTime_StayUser"))
        self.btn_Quey_StayUser = QtGui.QPushButton(Dialog)
        self.btn_Quey_StayUser.setGeometry(QtCore.QRect(150, 100, 75, 23))
        self.btn_Quey_StayUser.setObjectName(_fromUtf8("btn_Quey_StayUser"))
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(120, 440, 601, 111))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(70, 450, 21, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.table_StayUser = QtGui.QTableWidget(Dialog)
        self.table_StayUser.setGeometry(QtCore.QRect(40, 150, 741, 261))
        self.table_StayUser.setObjectName(_fromUtf8("table_StayUser"))
        self.table_StayUser.setColumnCount(0)
        self.table_StayUser.setRowCount(0)
        self.btn_export_StayuserRatio = QtGui.QPushButton(Dialog)
        self.btn_export_StayuserRatio.setGeometry(QtCore.QRect(340, 100, 75, 23))
        self.btn_export_StayuserRatio.setObjectName(_fromUtf8("btn_export_StayuserRatio"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.lbl_fromTime_StayUser.setText(_translate("Dialog", "起始时间：", None))
        self.lbl_endTime_StayUser.setText(_translate("Dialog", "结束时间：", None))
        self.lbl_title_StayUser.setText(_translate("Dialog", "本工具提供优卡留存率查询：", None))
        self.btn_Quey_StayUser.setText(_translate("Dialog", "查询", None))
        self.label.setText(_translate("Dialog", "<html><head/><body><p><span style=\" color:#55aa00;\">1．留存用户：是指某段时间的新增用户在下个时间段再次启动应用的用户。</span></p><p><span style=\" color:#55aa00;\">2．这部分用户占当时新增用户的比例即为留存率。留存率=新增用户中登录用户数/新增用户数*100%</span></p><p><span style=\" color:#55aa00;\">3. 例如：次日留存率：（当天新增的用户中，在第2天还登录的用户数）/第一天新增总用户数；</span></p><p><span style=\" color:#55aa00;\">第3日留存率：（第一天新增用户中，在往后的第3天还有登录的用户数）/第一天新增总用户数； </span></p></body></html>", None))
        self.label_2.setText(_translate("Dialog", "注：", None))
        self.btn_export_StayuserRatio.setText(_translate("Dialog", "导出Excel", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

