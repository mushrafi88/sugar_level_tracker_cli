import pandas as pd

df = pd.read_csv('sugar_chart.csv')
df.to_latex('sugar_chart_table.tex',index=False)
