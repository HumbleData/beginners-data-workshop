mask__PW_PL = (df['PetalWidthCm'] >2) & (df['PetalLengthCm'] < 5.5)
df[mask__PW_PL]