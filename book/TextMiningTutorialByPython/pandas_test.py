import pandas as pd
indata = [('Toronto', 175, 68, 25), ('Detroit', 183, 70, 23), ('Boise', 190, 72, 26)]
df = pd.DataFrame(data=indata, columns=['出身地','身長','体重','年齢'], index=['Bill', 'John', 'Fred'])
print(df)
print(df['体重'])
print(df[['体重','身長']])
print(df['体重']['John':'Fred'])
# または
print(df['体重'][1:3])
print(df.ix[1,3])
print(df['体重'].sum())
print(df['体重'].mean())
print(df['体重'].median())
print(df['体重'].max())
from matplotlib import pyplot as plt
df['身長'].plot.bar()
plt.show()
import pandas as pd
df = pd.read_excel('file_name', 'Sheet1')
df = pd.read_csv('file_name', encoding='utf-8')
df.to_excel('file_name', 'sheet_name')
