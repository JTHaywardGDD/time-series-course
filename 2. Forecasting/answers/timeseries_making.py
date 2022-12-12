data_df = pd.DataFrame(data = data, 
                index = pd.date_range(pd.Timestamp('2021-07-01') , periods=10, freq='W-THU'), 
                columns = ['A','B','C'])
