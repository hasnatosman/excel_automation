import numpy as np
import pandas as pd

excel = 'marks.xlsx'

df = pd.read_excel(excel)

df['Average'] = df.mean(axis=1)
df['Sum'] = df.sum(axis=1)

df['Even/Odd'] = np.where(df['Sum'] % 2 == 0, 'EVEN', 'ODD')
print(df)
