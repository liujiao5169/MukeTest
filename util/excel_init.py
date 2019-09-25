# coding=utf-8
import xlrd
from xlutils.copy import copy


class ExcelInit(object):
    def __init__(self, excel_path=None, index=None):
        if excel_path == None:
            self.excel_path = "C:/Users/TSDLJ/PycharmProjects/UITest_muke/config/casedata.xls"
        else:
            self.excel_path = excel_path
        if index == None:
            index = 0
        # 获取data
        self.data = xlrd.open_workbook(self.excel_path)
        # 获取sheet
        self.table = self.data.sheets()[index]

    # 获取行数
    def get_lines(self):
        lines = self.table.nrows
        if lines >= 1:
            return lines
        return None

    # 获取列数
    def get_col(self):
        col = self.table.ncols
        if col >= 1:
            return col
        return None

    # 获取表格具体数据
    def get_col_value(self, row, col):
        if self.get_lines() > row and self.get_col() > col:
            data = self.table.cell(row, col).value
            return data
        return None

    # 以list格式返回data
    def get_data(self):
        data = []
        rows = self.get_lines()
        if rows >= 1:
            for i in range(rows):
                # 获取每行list
                col = self.table.row_values(i)
                data.append(col)
            return data
        return None

    # 写入数据
    def write_value(self, row, vlaue):
        read_data = xlrd.open_workbook(self.excel_path)
        write_data = copy(read_data)
        # 实际结果列写入数据
        write_data.get_sheet(0).write(row, 9, vlaue)
        write_data.save(self.excel_path)


if __name__ == "__main__":
    ex = ExcelInit("C:/Users/TSDLJ/PycharmProjects/UITest_muke/config/keyword.xls")
    data = ex.get_col_value(5, 8)
    print(data)
    print(ex.get_lines())
    print(ex.get_col())
    # ex.write_value(7, "test")
