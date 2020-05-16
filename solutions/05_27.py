dict_codes = {'BG':'Bulgaria', 'CZ':'Czech Republic', 'IT':'Italy', 'GR':'Greece', 'SI':'Slovenia', 'UK':'United Kingdom'}

df.loc[df['country'].isin(dict_codes.keys()), 'country'] = df.loc[df['country'].isin(dict_codes.keys()), 'country'].map(dict_codes)