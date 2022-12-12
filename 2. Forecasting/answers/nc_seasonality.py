# +
#selecting 12 rbf features
rbf_features =  X_rbf[:,1:].copy()

#multiplying by time variable
rbf_time  = rbf_features*time_var
# -

#concatenating RBF features, RBF*time features and After 2009 feature
X_rbf2 = np.c_[ X_rbf, rbf_time, schiphol_rbf['after2009']]

#fitting the model
lm_rbf2 = LinearRegression().fit(X_rbf2, y)
print(f"R^2 is {round(lm_rbf2.score(X_rbf2, y),3)}")

schiphol_rbf['pass_rbf2_pred'] = lm_rbf2.predict(X_rbf2)

#plotting
schiphol_rbf[['total_passengers','pass_rbf2_pred']].plot(figsize=(16,4));
