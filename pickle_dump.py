#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys, os

reload(sys)
sys.setdefaultencoding('utf-8')
import pickle
import pprint
import xlsxwriter
from helper import tool
from dev_config import Youka
import datetime


def init_data():
    data = {'all_func_clik': [
        [u'2016年3月31号',
         u'2016年4月08号',
         u'2016年4月15号',
         u'2016年4月22号',
         u'2016年4月29号',
         u'2016年5月06号',
         u'2016年5月13号',
         u'2016年5月20号',
         u'2016年5月27号',
         u'2016年6月03号',
         u'2016年6月08号',
         u'2016年6月17号',
         u'2016年6月24号'],
        [14143,
         23399,
         35900,
         50737,
         68330,
         88816,
         111728,
         136804,
         165425,
         194595,
         215484,
         254825,
         306726],
        [15664,
         22733,
         30132,
         39354,
         49362,
         56794,
         65667,
         74369,
         83484,
         92459,
         97088,
         105969,
         116085],
        [118772,
         201786,
         249611,
         289741,
         335941,
         383004,
         432956,
         486752,
         542147,
         600297,
         634968,
         709441,
         820983],
        [17459,
         28284,
         39622,
         49517,
         60183,
         71509,
         82911,
         93903,
         104107,
         116616,
         123098,
         135491,
         147034],
        [20588,
         31583,
         45180,
         60846,
         77663,
         94864,
         115614,
         138001,
         161670,
         186599,
         202331,
         232106,
         266599],
        [16262,
         26225,
         37680,
         49230,
         60748,
         71026,
         83484,
         96004,
         108186,
         121298,
         129631,
         143458,
         158748],
        [1199,
         1902,
         2638,
         2647,
         2647,
         2647,
         2647,
         2647,
         2647,
         2647,
         2647,
         2647,
         2647],
        [13461,
         20871,
         28909,
         36923,
         44727,
         52722,
         60466,
         67951,
         75421,
         83531,
         88216,
         98756,
         110466],
        [16032,
         30904,
         44640,
         61994,
         79209,
         95689,
         111281,
         125147,
         137635,
         149413,
         155309,
         166534,
         181632]

    ],
        'all_func_clik_increase': [
            [u'2016年3月31号',
             u'2016年4月08号',
             u'2016年4月15号',
             u'2016年4月22号',
             u'2016年4月29号',
             u'2016年5月06号',
             u'2016年5月13号',
             u'2016年5月20号',
             u'2016年5月27号',
             u'2016年6月03号',
             u'2016年6月08号',
             u'2016年6月17号',
             u'2016年6月24号'],
            [6244,
             9256,
             12501,
             14837,
             17593,
             20486,
             22912,
             25076,
             28621,
             29170,
             20889,
             39341,
             51901],
            [6955,
             7069,
             7399,
             9222,
             10008,
             7432,
             8873,
             8702,
             9115,
             8975,
             4629,
             8881,
             10116],
            [63351,
             83014,
             47825,
             40130,
             46200,
             47063,
             49952,
             53796,
             55395,
             58150,
             34671,
             74473,
             111542],
            [7892,
             10825,
             11338,
             9895,
             10666,
             11326,
             11402,
             10992,
             10204,
             12509,
             6482,
             12393,
             11543],
            [7970,
             10995,
             13597,
             15666,
             16817,
             17201,
             20750,
             22387,
             23669,
             24929,
             15732,
             29775,
             34493],
            [7371,
             9963,
             11455,
             11550,
             11518,
             10278,
             12458,
             12520,
             12182,
             13112,
             8333,
             13827,
             15290],
            [591,
             703,
             736,
             9,
             0,
             0,
             0,
             0,
             0,
             0,
             0,
             0,
             0],
            [5618,
             7410,
             8038,
             8014,
             7804,
             7995,
             7744,
             7485,
             7470,
             8110,
             4685,
             10540,
             11710],
            [13105,
             14872,
             13736,
             17354,
             17215,
             16480,
             15592,
             13866,
             12488,
             11778,
             5896,
             11225,
             15098]
        ]
    }

    # 持久化到pickle文件
    with open('func_click.pkl', 'wb') as f:
        pickle.dump(data, f)


def add():
    item = [u'2016年7月01号', 357488, 128482, 934814, 156666, 299626, 176978, 2647, 121640, 198298]
    item_increase = [u'2016年7月01号', 50762, 12397, 113831, 9632, 33027, 18230, 0, 11174, 16666]
    with open('func_click.pkl', 'rb') as f:
        data_all = pickle.load(f)
        data = data_all['all_func_clik']
        data_increase = data_all['all_func_clik_increase']
        for d in data:
            d.append(item[data.index(d)])
        for i in data_increase:
            i.append(item_increase[data_increase.index(i)])
        print data_all
    # 持久化到pickle文件
    with open('func_click.pkl', 'wb') as f:
        pickle.dump(data_all, f)


def pop(count=1):
    with open('func_click.pkl', 'rb') as f:
        data_all = pickle.load(f)
        data = data_all['all_func_clik']
        data_increase = data_all['all_func_clik_increase']
        for i in range(0, count):
            for item in data:
                print item.pop()
            for item2 in data_increase:
                print item2.pop()

        print data_all

    # 持久化到pickle文件
    with open('func_click.pkl', 'wb') as f:
        pickle.dump(data_all, f)


def make_all_func_clik(filename='mychart.xlsx'):
    os.chdir(os.path.dirname(sys.argv[0]))
    workbook = xlsxwriter.Workbook(filename)
    worksheet = workbook.add_worksheet('sheet_source')
    worksheet2 = workbook.add_worksheet('sheet_chart')
    bold = workbook.add_format({'bold': 1})
    headings = [u'报表时间', u'转账充值', u'查询账单', u'校园卡基本信息', u'补助流水查询', u'当日流水查询', u'历史流水查询', u'修改用户密码', u'拾卡信息', u'饭堂日记']
    today = datetime.date.today().strftime(u'%Y年%m月%d号')
    tag = 1
    # load data from pickle file
    with open('func_click.pkl', 'rb') as f:
        data_all = pickle.load(f)
        # pprint.pprint(data_all)

    if today in data_all['all_func_clik'][0][-1] or today in data_all['all_func_clik_increase'][0][-1]:
        tag = -1
    # 查询最新数据
    data = data_all['all_func_clik']
    # tab =1 时才向数据库查询
    if tag == 1:
        new_data_record = tool.runsql(Youka.HOST, Youka.ACCOUNT, Youka.PASSWORD, Youka.DB, Youka.FUNC_CLICK_SQL)
        # print new_data_record
        record = []
        if new_data_record:
            for head in headings:
                for item in new_data_record:
                    if head == item['FuncName']:
                        record.append(item['counts'])

        if record:
            record.reverse()
            for item in data[1:]:
                item.append(record.pop())
            # 给data[0]添加日期

            data[0].append(today)
        # print data
        # 指向原数组
        data_all['all_func_clik'] = data
    worksheet.write('A1', '主要功能点击量')
    worksheet.write_row('A2', headings, bold)

    worksheet.write_column('A3', data[0])
    worksheet.write_column('B3', data[1])
    worksheet.write_column('C3', data[2])
    worksheet.write_column('D3', data[3])
    worksheet.write_column('E3', data[4])
    worksheet.write_column('F3', data[5])
    worksheet.write_column('G3', data[6])
    worksheet.write_column('H3', data[7])
    worksheet.write_column('I3', data[8])
    worksheet.write_column('J3', data[9])

    #######################################################################
    #
    # Create a new column chart.
    #
    chart1 = workbook.add_chart({'type': 'column'})
    # Iterate all rows
    # for i in range(1, len(headings)):
    #     chart1.add_series({
    #         'name': ['sheet_source', 0, i],
    #         'categories': ['sheet_source', 1, 0, 13, 0],
    #         'values': ['sheet_source', 1, i, 13, i],
    #     })

    colors = ['red', 'gray', 'orange', 'cyan', 'green', 'yellow', 'purple', 'brown', 'magenta', 'red']
    for i in range(1, len(headings)):
        chart1.add_series({
            'name': ['sheet_source', 1, i],  # 表头列
            'categories': ['sheet_source', len(data[1]), 0, len(data[1]) + 1, 0],  # 行标题
            'values': ['sheet_source', len(data[1]), i, len(data[1]) + 1, i],  # 此处是起始
            'fill': {'color': colors[i]},
            'data_labels': {'value': True}
        })

    # # Configure the first series.
    # chart1.add_series({
    #     'name': '=sheet_source!$B$1',
    #     'categories': '=sheet_source!$A$2:$A$7',
    #     'values': '=sheet_source!$B$2:$B$7',
    # })
    #
    # # Configure a second series. Note use of alternative syntax to define ranges.
    # chart1.add_series({
    #     'name':       ['sheet_source', 0, 2],
    #     'categories': ['sheet_source', 1, 0, 13, 0],
    #     'values':     ['sheet_source', 1, 2, 13, 2],
    # })

    # Add a chart title and some axis labels.
    chart1.set_title({'name': u'点击总量趋势图'})
    # chart1.set_x_axis({'name': 'Test number'})
    # chart1.set_y_axis({'name': 'Sample length (mm)'})

    # Set an Excel chart style.
    chart1.set_style(11)

    # Insert the chart into the worksheet (with an offset).
    worksheet2.insert_chart('A1', chart1, {'x_offset': 25, 'y_offset': 10})

    # add increase data and chart
    data_increase = data_all['all_func_clik_increase']

    # tag == 1 才添加新增数据
    if tag == 1:
        a = [item[-1] for item in data[1:]]
        b = [item[-2] for item in data[1:]]
        a_minus_b = [a[b.index(i)] - i for i in b]
        if a_minus_b:
            a_minus_b.reverse()
            for item in data_increase[1:]:
                item.append(a_minus_b.pop())
            # 给data[0]添加日期

            data_increase[0].append(today)
    end_station = str(len(data[1]) + 6)
    worksheet.write('A' + str(int(end_station) - 1), '主要功能点击增量')
    worksheet.write_row('A' + end_station, headings, bold)

    end_station_and1 = str(int(end_station) + 1)
    worksheet.write_column('A' + end_station_and1, data_increase[0])
    worksheet.write_column('B' + end_station_and1, data_increase[1])
    worksheet.write_column('C' + end_station_and1, data_increase[2])
    worksheet.write_column('D' + end_station_and1, data_increase[3])
    worksheet.write_column('E' + end_station_and1, data_increase[4])
    worksheet.write_column('F' + end_station_and1, data_increase[5])
    worksheet.write_column('G' + end_station_and1, data_increase[6])
    worksheet.write_column('H' + end_station_and1, data_increase[7])
    worksheet.write_column('I' + end_station_and1, data_increase[8])
    worksheet.write_column('J' + end_station_and1, data_increase[9])

    chart2 = workbook.add_chart({'type': 'line'})
    colors = ['red', 'gray', 'orange', 'cyan', 'green', 'yellow', 'purple', 'brown', 'magenta', 'red']
    # print 'endstation_and1:' + end_station_and1
    for j in range(1, len(headings)):
        chart2.add_series({
            'name': ['sheet_source', int(end_station) - 1, j],
            'categories': ['sheet_source', int(end_station), 0, int(end_station) + len(data_increase[1]) - 1, 0],
            'values': ['sheet_source', int(end_station), j, int(end_station) + len(data_increase[1]) - 1, j],
            'fill': {'color': colors[j]}
        })
        # Iterate all rows
        # for i in range(1, len(headings)):
        #     chart1.add_series({
        #         'name': ['sheet_source', 0, i],
        #         'categories': ['sheet_source', 1, 0, 13, 0],
        #         'values': ['sheet_source', 1, i, 13, i],
        #     })
    chart2.set_title({'name': u'点击增量趋势图'})
    worksheet2.insert_chart('A18', chart2, {'x_offset': 25, 'y_offset': 10})
    # print data_all

    workbook.close()
    # tag =1 时更新pickel文件
    if tag == 1:
        with open('func_click.pkl', 'wb') as f:
            pickle.dump(data_all, f)

    return tag


############################################
# test pickle
## account_info2 = {'100003': ['tom2222', 8000, 10000], '1000004': ['lucy2222', 9500, 12000]}
# with open('func_click.pkl', 'wb') as f:
#     pickle.dump(func_click_obj, f)

# load from pickle file
# with open('func_click.pkl', 'rb') as f:
#     get_func_click_obj = pickle.load(f)
#     pprint.pprint(get_func_click_obj)

#
# # update value
# account_info['100001'][1] = 8500
# with open('account.pkl', 'wb') as f:
#     pickle.dump(account_info, f)
#
# # load from pickle file
# with open('account.pkl', 'rb') as f:
#     account_info = pickle.load(f)
#     pprint.pprint(account_info)

if __name__ == '__main__':
    # make_all_func_clik()
    # init_data()
    pop()
    # add()
    # pass
