(
    power
    .resample('5D')
    .sum()
    .loc[lambda df: df['consumption'] == df['consumption'].max()]
)
