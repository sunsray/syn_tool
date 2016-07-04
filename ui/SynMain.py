# -*- coding: utf-8 -*-

"""
Module implementing SynMain.
"""

from PyQt4.QtCore import pyqtSignature
from PyQt4.QtGui import QMainWindow
from PyQt4.QtGui import QMessageBox

from .Ui_MainWindow import Ui_MainWindow

from .Query_Youka_User import Youka_User_Window
from MW_Query_Youka_LiveUser import MW_Query_Youka_LiveUser
from dev_config import Youka


class SynMain(QMainWindow, Ui_MainWindow):
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

        # self.write_reg()
        # self.ac_query_youka_user.setDisabled(True)
        self.setWindowTitle(u'新中新运维部支持工具')
        self.child_query_youka = Youka_User_Window()  # 注意在init在构造函数初始化child窗体
        self.child_query_youka_liveuser = MW_Query_Youka_LiveUser()

    @pyqtSignature("")
    def on_ac_query_youka_user_triggered(self):
        """
        Slot documentation goes here.
        """

        self.MainGridLayout.addWidget(self.child_query_youka)
        self.child_query_youka.show()

    @pyqtSignature("")
    def on_ac_query_youka_live_triggered(self):
        """
        Slot documentation goes here.
        """
        self.MainGridLayout.addWidget(self.child_query_youka_liveuser)
        self.child_query_youka_liveuser.show()

    @pyqtSignature("")
    def on_actionAbout_triggered(self):
        """
        Slot documentation goes here.
        """
        QMessageBox.information(None, "QMessageBox.information()", Youka.MEMU_ABOUT_MESSAGE)

    @pyqtSignature("")
    def on_ac_quit_triggered(self):
        """
        Slot documentation goes here.
        """
        self.close()

    # def write_reg(self):
    #     import _winreg
    #     key = _winreg.OpenKey(_winreg.HKEY_CURRENT_USER, r"Software\SynTool\Youka")
    #     newKey = _winreg.CreateKey(key, "MyNewkey")
    #     # 给新创建的键添加键值
    #
    #     _winreg.SetValue(newKey, "ValueName", 0, "ValueContent")
    #     if key:
    #         _winreg.CloseKey(key)
