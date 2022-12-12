(
    logins_daily
    .assign(weekday = logins_daily.index.day_of_week,
            day = logins_daily.index.day_name())
    .loc[lambda df: df['weekday']< 5]
    [['full']]
    .resample('w')
    .mean()
     .plot()
)
