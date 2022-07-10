mask_PW_PL = (df["body_mass_g"] > 4000) & (df["flipper_length_mm"] < 185)
df[mask_PW_PL]