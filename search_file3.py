import numpy as np
import pandas as pd


excel_files = ['automate.xlsx', 'automate2.xlsx']

for each_file in excel_files:
    df = pd.read_excel(each_file)

    programmer = df['Name'].where(df['Occupation'] == 'Programmer').dropna()
    print('File Name: ' + each_file)
    print(programmer)