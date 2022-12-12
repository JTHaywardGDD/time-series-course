(
    logins['full']
    .resample('d')
    .mean()
    .sort_values(ascending=False)
    .head()
)