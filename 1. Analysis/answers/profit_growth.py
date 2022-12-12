random_growth_df.resample('5d').apply(lambda df: pd.Series({
    'net_growth': df['profit'].iat[-1] - df['profit'].iat[0],
    'all_growth': (df['profit'].diff().dropna() > 0).all()
})).sort_values('net_growth', ascending=False)
