import numpy as np
import pandas as pd


excel_file = 'automate2.xlsx'
collected_data = pd.read_excel(excel_file)

print(collected_data)
print(collected_data['Country'].where(collected_data['Name'] == 'Messi').dropna())