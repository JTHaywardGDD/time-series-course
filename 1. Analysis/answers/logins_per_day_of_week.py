(
    logins_daily
    .assign(weekday = logins_daily.index.day_of_week,
            day = logins_daily.index.day_name())
    .groupby('day')
    .mean()[['full']]
)
