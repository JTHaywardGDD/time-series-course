power_5d = (
    power
    .resample('D')
    .agg([('tot_consumption','sum')])
    .droplevel(0, axis=1)
    .resample('5D')
    .agg([('change', lambda x: x.iloc[-1] - x.iloc[0])])
    .droplevel(0, axis=1)
)

display(power_5d.nlargest(10, 'change'))
