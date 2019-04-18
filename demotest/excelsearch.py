#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/4/15 10:43
# @Author  : bgzhou

import xlrd
import os


class ExcelSearch:

    def search_in_dir(self, dirs, value):
        for path, dir_list, file_list in os.walk(dirs):
            for file_name in file_list:
                path1 = path.replace("\\", "/")
                file_path = path1 + "/" + file_name
                if self._search_in_excel(value, file_path):
                    yield file_path

    def _search_in_excel(self, value, file):
        wb = xlrd.open_workbook(filename=file)
        for k in range(2):
            sheet1 = wb.sheet_by_index(k)
            for i in range(sheet1.nrows):
                for j in range(sheet1.ncols):
                    if str(sheet1.cell_value(i, j)).find(value) != -1:
                        return True