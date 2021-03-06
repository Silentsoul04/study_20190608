#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author:    xurongzhong#126.com wechat:pythontesting qq:37391319
# CreateDate: 2018-1-19 pandas_column_by_index.py
import pandas as pd

input_file = r"supplier_data.csv"
output_file = r"output_files\6output.csv"

data_frame = pd.read_csv(input_file)  # 从csv文件里读取内容到data_frame
data_frame_column_by_index = data_frame.iloc[:, [0, 1, 3]]    # select all rows, select 0,1 and 3 column
data_frame_column_by_index.to_csv(output_file, index=False)