plotr = (
    power_daily_na
    .loc['2010-08']
    .assign(
        smooth=lambda df: df['consumption'].ewm(alpha=0.01).mean().fillna(method='ffill'),
        interpolate_smooth=lambda df: np.where(df['consumption'].isnull(), df['smooth'], np.NaN)
    )
)

fig, (ax_upper, ax_middle, ax_lower) = plt.subplots(3, figsize=(10, 8), sharex=True)

plotr.plot(y='consumption', style='.b', ax=ax_upper, legend=False)
for missing_day in power_daily_na.loc[lambda df: df['consumption'].isna()].index.values:
    ax_upper.axvline(missing_day, c='r')
ax_upper.set_title('the red lines are missing')

plotr.plot(y='consumption', style='.b', ax=ax_middle, legend=False)
plotr.plot(y='smooth', style='.g', ax=ax_middle, legend=False)
ax_middle.set_title('the green values are from smoothing')

plotr.plot(y='consumption', style='.b', ax=ax_lower, legend=False)
plotr.plot(y='interpolate_smooth', style='.g', ax=ax_lower, legend=False)
ax_lower.set_title('the final plot shows the true values and the smoothed interpolated values')

for ax in (ax_upper, ax_middle, ax_lower):
    ax.set_ylim([0, 25_000])
    ax.set_yticks(range(0, 30_000, 5_000))

fig.tight_layout()
