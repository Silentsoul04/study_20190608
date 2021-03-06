#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author:    xurongzhong#126.com wechat:pythontesting qq:37391319
# CreateDate: 2018-1-19 pandas_add_header_row.py
import pandas as pd

# 给没有header的数据添加header，即定义了一个列表,然后赋值给names参数
input_file = r"supplier_data_no_header_row.csv"
output_file = r"output_files/11output.csv"
header_list = ['Supplier Name', 'Invoice Number', 'Part Number', 'Cost', 'Purchase Date']
data_frame = pd.read_csv(input_file, header=None, names=header_list)  # 从一个csv文件读取数据，同时添加了header信息
print(data_frame)
data_frame.to_csv(output_file, index=False)      # 把data_frame写到一个cvs文件里面