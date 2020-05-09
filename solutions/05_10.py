df = df.reset_index().index
# We could also have done the following when concatenating: df = pd.concat(frames, ignore_index=True)