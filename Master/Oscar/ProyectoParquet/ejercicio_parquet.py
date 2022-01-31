import pandas as pd

# Load pandas dataframe with data from matches.csv

df = pd.read_csv("matches.csv", low_memory=False)


# Warning is displayed, it's inferencing datatype

# Get new dataset containing only selected columns ['home','away','date','home_score','away_score']
df2 = pd.DataFrame(columns=['home','away','date','home_score','away_score'])

df2['home'] = df['home']
df2['away'] = df['away']
df2['date'] = df['date']
df2['home_score'] = df['home_score']
df2['away_score'] = df['away_score']



# Save as csv file

df2.to_csv('out.csv', index=False)
# Save as parquet file without compression
df2.to_parquet('out.parquet', compression=None)
# Save as parquet file with compression
df2.to_parquet('outCompressed.zip', compression= 'gzip')

# Load new pandas dataframe with data from parquet file and display dataframe info

df3 = pd.read_parquet('outCompressed.zip')
df3.info()