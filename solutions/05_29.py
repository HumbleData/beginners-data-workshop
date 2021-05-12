dict_capitals = {
    "Denmark": "copenhague",
    "France": "paris",
    "Italy": "rome",
    "Spain": "madrid",
    "United Kingdom": "london",
}

unknown_city = df["city"] == "unknown"
df.loc[unknown_city, "city"] = df.loc[unknown_city, "country"].map(dict_capitals)