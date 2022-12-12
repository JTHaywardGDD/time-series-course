logins =  pd.read_csv('data/logins.csv', 
                    parse_dates=['login_date'], index_col='login_date')
logins.head()