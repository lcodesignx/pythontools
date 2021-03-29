#!/usr/bin/env python3

import pandas as pd
import numpy as np

df_new = pd.read_csv('file.csv')

excel_file = pd.ExcelWriter('file.xlsx')

df_new.to_excel(excel_file, index=False)

excel_file.save()
