from sklearn.preprocessing import PolynomialFeatures

#identifying months and preprocessing them
schiphol['month'] = schiphol.index.month
X_month = schiphol[['period_num','after2009','month']]

feature_transformer = ColumnTransformer(
     [('categorical', OneHotEncoder(sparse=False, drop='first'), ['month'])],
    remainder='passthrough'
)

#creating the model
model_monthly = Pipeline([
    ('preprocess', feature_transformer),
    ('poly', PolynomialFeatures(degree=2)),
    ('model', LinearRegression())
])

#model fitting, predictions and plotting
lm_poly = model_monthly.fit(X_month, y)
print(f"R^2 is {round(lm_poly.score(X_month, y),3)}")

schiphol['pass_poly_pred'] = lm_poly.predict(X_month)

schiphol[['total_passengers','pass_poly_pred']].plot(figsize=(16,4));
