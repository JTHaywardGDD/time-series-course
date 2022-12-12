(
    logins['full']
    .resample('d')
    .max()
    .plot()
)