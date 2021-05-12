null_country = df["country"].isnull()
df.loc[null_country, "country"] = df.loc[null_country, "city"].map(dict_cities)