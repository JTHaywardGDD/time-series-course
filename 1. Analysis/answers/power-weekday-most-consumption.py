(
    power_daily
    .assign(weekday = lambda df: df.index.day_name(),
            weekday_num = lambda df: df.index.day_of_week)
    .groupby('weekday')
    .mean()
    .sort_values('weekday_num')
    .plot(kind='bar', legend=False, title='total consumption per day of the week')
)
