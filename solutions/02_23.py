print(f'number of rows of df_2: {df_2.shape[0]}')

# We haven't lost any rows here, because .dropna(how='all') drops rows
# where ALL the values are missing. This dataset has no rows where every
# value is missing:

print(df.isnull().sum())