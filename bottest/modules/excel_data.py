"""
Create by 吹着风的包子 on 2019-06-11
"""
from bottest.modules.helper import file_path

__author__ = "吹着风的包子"

import os
import xlrd


class ExcelData:
    def __init__(self, book):
        self.get_sheet_names = book.sheet_names()
        self.table = book.sheet_by_name(self.get_sheet_names[0])
        self.row_num = self.table.nrows
        self.col_num = self.table.ncols
        self.cur_row_no = 4

    def conf_get_data(self):
        conf_list = self.table.row_values(2)
        return conf_list

    def get_case_data(self):
        r = []
        while self.has_next():
            col = self.table.row_values(self.cur_row_no)
            split_col_1 = "".join(col[1].split())
            split_col_2 = "".join(col[2].split())

            if "||" in col[0]:
                spl_data = col[0].strip("||").split("||")
                for i in spl_data:
                    r.append([self.cur_row_no, i, split_col_1, split_col_2])
            else:
                r.append([self.cur_row_no, col[0], split_col_1, split_col_2])
            self.cur_row_no += 1
        return r

    def has_next(self):
        if self.row_num == 0 or self.row_num <= self.cur_row_no:
            return False
        else:
            return True
