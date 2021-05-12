df = df.drop("Country", axis=1)

# N.B. You can only run this cell once! If you try run it again, it will throw an error!
#      Why? Because if you drop the Country column, it will be removed...so you can't
#      drop it a second time as the column isn't there to drop!