mses = []

#finding the best parameters for different n_splits
for n in range (2, 11, 2):
    
    tscv = TimeSeriesSplit(n_splits = n)

    gsearch = GridSearchCV(estimator = model, cv = tscv,
                           
                        param_grid = parameters, scoring='neg_root_mean_squared_error').fit(X, y)
    
    power_daily['grid_pred_new'] = gsearch.predict(power_daily[['period_num','day_of_year']])
    
    y_pred = power_daily['grid_pred_new'].loc['2010 May':]

    mses.append(np.sqrt(mean_squared_error(y_test_wra, y_pred)))

#plotting the resulting RMSEs
plt.plot(range (2, 11, 2), mses)
plt.title("RMSE vs number of CV splits");
