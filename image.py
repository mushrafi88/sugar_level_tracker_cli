import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('sugar_chart.csv')
df=df.replace('-',np.nan)

Time = ['Fasting','2HAB','2HAL','2HAD']

mean = []
for i in Time:
    df[i] = df[i].astype(np.float32)
    mean.append(df[i].mean().round(1))

#time of the day in 24h when the sugar is measured
time = [8,11,17,23.75]

df = {
    'Time' : time,
    'Sugar level (mmol/L)' : mean
}

sns.set()
p = sns.lineplot(x='Time', y='Sugar level (mmol/L)',data=df)
p.set_xlabel("Time(24H)", fontsize = 15)
p.set_ylabel("Sugar level (mmol/l)", fontsize = 15)
p.set_title("Average Sugar level", fontsize = 15)
plt.savefig('sugar_level.png')
