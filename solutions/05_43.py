df["month"] = df["DateFrom"].dt.month
df["month"].hist()