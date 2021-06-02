import numpy as np
import pandas as pd

excel_file = 'marks.xlsx'

scores_df = pd.read_excel(excel_file)

# creating new column

scores_df['Average'] = scores_df.mean(axis=1)
conditions = [
    (scores_df['Average'] % 2 == 0) & (scores_df['Average'] % 5 == 0),
    (scores_df['Average'] % 3 == 0) & (scores_df['Average'] % 7 == 0),
    (scores_df['Average'] % 4 == 0) & (scores_df['Average'] % 2 == 0),
    (scores_df['Average'] % 2 == 0),
    (scores_df['Average'] % 2 != 0)

]
results = [' 2&5', '3&7', '4&2', 'Even', 'Odd']

scores_df['Results'] = np.select(conditions, results)
print(scores_df)
