import pandas as pd

'''
dataframe.sort_values["column_name"]
dataframe.sort_value("column_name")
dataframe.sort_value("column_name" asscending=False)  ...descending order
dataframe.sort_value(["column_name1", "col_2"])

'''

d = pd.read_csv("C:\\Users\\korad\\Desktop\\python examples\\modules\\pandas\\BILLIONAIRES.csv")
#creating DataFrame
df = pd.DataFrame(d)

print(df.sort_values("AGE" ,ascending=False))
