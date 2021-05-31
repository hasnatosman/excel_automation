# import the libraries........................

import numpy as np
import pandas as pd


# excel file to work............................

excel_file = 'marks.xlsx'
df = pd.read_excel(excel_file)

# creating new column ...........................

df['Average'] = df.mean(axis=1)


# even or odd column...............

df['Even/Odd'] = np.where(df['Average'] % 2 == 0, 'Even', 'Odd')


print(df)


