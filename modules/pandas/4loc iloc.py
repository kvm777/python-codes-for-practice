import pandas as pd
'''
loc and iloc

using loc[] (stop index included..)
dataframe.loc[row_num]
dataframe.loc[row_num, [column_name,...] ]
dataframe.loc[start:stop]
dataframe.loc[start:stop, column_name]
dataframe.loc[start:stop, [column_name,...] ]
dataframe.loc[start:stop, "column_1": "column_n"]


using iloc[] (stop index excluding..)
dataframe.iloc[row_num,column_num]
dataframe.iloc[row_stat:row_stop, column_start:solmn_stop]
dataframe.iloc[row_stat:row_stop, "column_num"]
dataframe.iloc[[row_1, row_2,...]]
dataframe.iloc[:, [col_1,col_2,..]]
dataframe.iloc[start:stop, [col_1,col_2,..]]
'''

d = pd.read_csv("C:\\Users\\korad\\Desktop\\python examples\\modules\\pandas\\BILLIONAIRES.csv")
#creating DataFrame
df = pd.DataFrame(d)

print(df.loc[1])
print()

print(df.loc[10,["NAME","AGE", "SOURCE"]])
print()

print(df.loc[0:5])      #stop index including...
print()

print(df.iloc[0:5])     #stop index excluding...
print()

print(df.loc[1:5, "NAME"])
print()

print(df.loc[1:5, ['NAME', 'AGE', 'SOURCE']])
print()

print(df.loc[1:5, 'NAME' : 'SOURCE'])
print()


#iloc[]......

print(df.iloc[0,4])
print()

print(df.iloc[0:4, 1:3])
print()

print(df.iloc[0:4, 1])      
print()

print(df.iloc[[1,3,7]])     #row nums...
print()

print(df.iloc[2:6, [1,3,4]])
print()

print(df.loc[5,"NAME"])