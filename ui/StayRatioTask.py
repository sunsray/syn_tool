# -*- coding: utf-8 -*-
import sys

from PyQt4.QtGui import QApplication
from PyQt4.QtCore import QThreadPool, QObject, QRunnable, pyqtSignal
from dev_config import Youka
import datetime, time
from helper import tool

data = []


class GenerWork:
    def __init__(self, ar):
        self.ar = ar

    def str_to_date(self, str):
        t = time.strptime(str, "%Y-%m-%d")
        y, m, d = t[0:3]
        date = datetime.datetime(y, m, d)
        return date

    def get_workers(self):
        return self.workers

    def get_shell_data(self):
        return self.shell_data

    def generateWorkers(self):

        self.workers = []

        self.shell_data = []
        for _ in self.ar:
            row_data = []
            _2 = self.str_to_date(_)

            for __ in self.ar:
                conditon2 = self.str_to_date(__)

                if _2 == conditon2:
                    row_data.append('100%')
                elif conditon2 < _2:
                    row_data.append('--')
                else:
                    tag1, tag2 = _, self.ar[self.ar.index(_) + 1]
                    if __ == self.ar[-1]:
                        tag3 = __
                        conditon2plus = conditon2 + datetime.timedelta(1)
                        tag4 = conditon2plus.strftime('%Y-%m-%d')
                    else:
                        tag3, tag4 = __, self.ar[self.ar.index(__) + 1]

                    sql_str = Youka.STAY_USER_SQL.format(tag1, tag2, tag3, tag4, tag1, tag2, )
                    # print sql_str

                    worker = Worker(sql_str, _, __)
                    # print '#' * 60

                    self.workers.append(worker)

            print row_data
            self.shell_data.append(row_data)
        print self.shell_data
        # print '#' * 60


class WorkerSignals(QObject):
    result = pyqtSignal(str)


class Worker(QRunnable):
    def __init__(self, sql_str, _, __):
        super(Worker, self).__init__()

        self.sql_str = sql_str
        self.data_key = _ + "|" + __
        self.signals = WorkerSignals()

    def run(self):
        # print 'Sending', self.task
        # self.signals.result.emit(self.task)
        self.handle()

    def handle(self):
        self.dat_result = tool.testcon(Youka.HOST, Youka.ACCOUNT, Youka.PASSWORD, Youka.DB, self.sql_str)

        stay_ratio = self.dat_result[0].strip()
        data.append(self.data_key + ':' + stay_ratio)
        print ' 留存率：%s' % (stay_ratio)

        self.signals.result.emit(str(len(data)))


class Tasks(QObject):
    def __init__(self, ar, process_result):
        super(Tasks, self).__init__()
        self.ar = ar
        self.process_result = process_result
        self.pool = QThreadPool()
        self.pool.setMaxThreadCount(10)

    # def process_result(self, rev):
    #     # print 'Receiving', rev
    #     self.ref.setText(rev)

    def start(self):
        self.factory = GenerWork(self.ar)

        self.factory.generateWorkers()
        workers = self.factory.get_workers()

        # print workers
        for worker in workers:
            worker.signals.result.connect(self.process_result)

            self.pool.start(worker)

        self.pool.waitForDone()
        return data

    def get_shell_data(self):
        return self.factory.get_shell_data()


if __name__ == "__main__":
    import sys

    ar2 = ['2016-10-21', '2016-10-22', '2016-10-23', '2016-10-24', '2016-10-25', '2016-10-26', '2016-10-27',
           '2016-10-28',
           '2016-10-29', '2016-10-30', '2016-10-31', '2016-11-01', '2016-11-02', '2016-11-03']

    app = QApplication(sys.argv)
    main = Tasks(ar2, None)
    main.start()
    sys.exit(app.exec_())
