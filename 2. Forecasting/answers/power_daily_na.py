power_daily_na = (
    power
    .assign(missing=lambda df: df['consumption'].isna())
    .resample('D')
    .agg({'consumption': sum, 'missing': all})
    .assign(consumption=lambda df: np.where(df['missing'], np.nan, df['consumption']))
    .drop(columns='missing')
)
power_daily_na.loc[lambda df: df['consumption'].isna()]
