import pandas as pd


'''
ADDING A COLUMN....
dataframe["new_col_name]=default value
dataframe["new_col_name]=expression/condition

REMOVING COLUMN...
dataframe.drop(columns="co;_name)
dataframe.drop(columns="co;_name, inplace=true)

df.duplicated()     #it would give boolean valve does ir repeated before or not...
df.drop_duplicates(inplace=true)    #delete the duplicates..

'''

d = pd.read_excel("C:\\Users\\korad\\Desktop\\python examples\\modules\\pandas\\Academic.xlsx")
#creating DataFrame
df = pd.DataFrame(d).head(21)

df["total"]=0
df["total"]=df["1-1 Semester"]+df["1-2 Semester"]

df.drop(columns= "Average")     #it won`t modefify permently
df.drop(columns= "Average", inplace=True)     #it modefify permently
print(df)
print(df.duplicated())      #it would give boolean valve does ir repeated before or not...



