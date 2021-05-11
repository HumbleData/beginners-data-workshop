dict_codes = {
    "BG": "Bulgaria",
    "CZ": "Czech Republic",
    "IT": "Italy",
    "GR": "Greece",
    "SI": "Slovenia",
    "UK": "United Kingdom",
}

country_in_codes = df["country"].isin(dict_codes.keys())
df.loc[country_in_codes, "country"] = df.loc[country_in_codes, "country"].map(dict_codes)