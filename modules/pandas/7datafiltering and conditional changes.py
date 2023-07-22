import pandas as pd

'''
dataframe.loc[condition]
dataframe.loc[condition].str.startswith(str)
dataframe.loc[condition].str.endswith(str)
dataframe.loc[condition].str.contains(str)

'''


d = pd.read_excel("C:\\Users\\korad\\Desktop\\python examples\\modules\\pandas\\Academic.xlsx")
#creating DataFrame
df = pd.DataFrame(d).head(20)


print(df.loc[(df["1-1 Semester"]>7.5) & (df["1-1 Semester"]<8.0)])