import pandas as pd

'''
dataframe.to_excel("file path")     --path location must be defined with doubke slshes(\\)
dataframe.to_csv("file path",index=False)   --it may hekps to print without index nums...
dataframe.to_excel("file path")
dataframe.to_excel("file path",index=False)
'''

d = pd.read_excel("C:\\Users\\korad\\Desktop\\python examples\\modules\\pandas\\Academic.xlsx")
#creating DataFrame
df = pd.DataFrame(d).head(21)

df["1st yeartotal"]=(df["1-1 Semester"]+df["1-2 Semester"])/2

print(df)

#df.to_csv("C:\\Users\\korad\\Desktop\\python examples\\pandas\\Academics1.csv")
