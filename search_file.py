import numpy as np
import pandas as pn


excel_file = 'automate.xlsx'

pd = pn.read_excel(excel_file)
#print(pd)


#print(pd['Country'].where(pd['Phone'] == 115566))

country_name = pd['Country'].where(pd['Name'] == 'Hasnat')

#print(country_name.dropna())

excel_files = ['automate.xlsx', 'automate2.xlsx']
for i in excel_files:
    files = pn.read_excel(i)
    print(files)