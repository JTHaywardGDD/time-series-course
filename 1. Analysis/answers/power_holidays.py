(
    power_daily
    .assign(
        low_cons=lambda df: df['consumption'] < 5000,     # flag
        switchpoint=lambda df: df['low_cons'] != df['low_cons'].shift(),
        session=lambda df: df['switchpoint'].cumsum()
    )
    .reset_index()
    .groupby('session')
    .agg(
        holiday=('low_cons', 'all'), 
        session_length=('session', 'count'),
        start=('ts', 'min'), 
        end=('ts', 'max'), 
    )
    .loc[lambda df: df.holiday==1]
    .loc[lambda df: df.session_length>=5]
)
