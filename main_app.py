#!/usr/bin/python
        
from PyQt4.QtGui import QApplication
from ui.SynMain import SynMain
import _mssql
import uuid

def main():
    import sys
    app = QApplication(sys.argv)
    wnd = SynMain()
    wnd.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
