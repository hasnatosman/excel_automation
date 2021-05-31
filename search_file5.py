import numpy as np
import pandas as pd

excel_file = 'stocl_analysis.xlsx'

analysed_data = pd.read_excel(excel_file)
ps = analysed_data['Packaging Station'].where(analysed_data['Packaging Station'] == 'Mirpur-13')

print(ps.dropna())
