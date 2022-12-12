(
    logins['full']
    .resample('d')
    .max()
    .sort_values(ascending=False)
    .head()
)