import numpy as np
import pandas as pd

excel_file = 'marks.xlsx'

df = pd.read_excel(excel_file)

df['Test 3'] = df.sum(axis=1)

df['Average'] = df.mean(axis=1).round()

conditions = [
    df['Average'] = np.where(df[])
]
print(df)