import pandas as pd

file_path = 'Desktop/workarea/summery/webtoon.csv'

df = pd.read_csv(file_path)
df = pd.DataFrame(df)
df = df[['title','outline']]
df = df.drop_duplicates(subset=['title'])
print(df)
