import pandas as pd

file_path = '/Users/choedohyeon/desktop/workarea/summery/webtoon.csv'

df = pd.read_csv(file_path)
df = pd.DataFrame(df)
df = df[['title', 'outline']]
df = df.drop_duplicates(subset=['title'])
df = df.dropna()
df = df.reset_index(drop=True)

print(df.head())
