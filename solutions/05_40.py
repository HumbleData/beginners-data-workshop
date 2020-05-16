df['DateFrom'] = pd.to_datetime(df['DateFrom'], format='%Y-%m-%d')
df['DateTo'] = pd.to_datetime(df['DateTo'], format='%Y-%m-%d')