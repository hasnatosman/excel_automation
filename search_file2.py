import numpy as np
import pandas as pd


excel_file = 'automate2.xlsx'
df = pd.read_excel(excel_file)

print(df)


print()

x = df['Name'].where(df['Occupation'] == 'Programmer')
print(x.dropna())