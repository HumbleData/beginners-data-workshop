dict_capitals = {'Denmark':'copenhague', 'France':'paris', 'Italy':'rome', 'Spain':'madrid', 'United Kingdom':'london'}

df.loc[df['city']=='unknown', 'city'] = df.loc[df['city']=='unknown', 'country'].map(dict_capitals) 