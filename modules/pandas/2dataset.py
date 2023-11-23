#a sataset is the collection of date..

#we get the free dataset from https://www.kaggle.com/

import pandas as pd
import __future__
# In a nutshell, __future__ allows you to use newer Python features even in older versions of Python, making your code more compatible and future-proof.

#read the existing dataset... 
#pd.read_excel for excel file
d = pd.read_csv("C:\\Users\\korad\\Desktop\\python examples\\modules\\pandas\\BILLIONAIRES.csv")
#creating DataFrame
df = pd.DataFrame(d)
print(df)
print()
d1 = pd.read_excel("C:\\Users\\korad\\Desktop\\python examples\\modules\\pandas\\Academic.xlsx")
df1=pd.DataFrame(d1)
print(df1)
