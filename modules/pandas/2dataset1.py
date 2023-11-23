import pandas as pd

#dataframe using dictionary...
print("dataframe using dictionary...")
d={"roll_num":[10,11,12,13], "marks":[54,25,75,37], "Percent":[23.4,65.3,53,77.99]}
df=pd.DataFrame(d)
print(df)

print()
#dataframe using tupples..
print("dataframe using tupples..")
d1=[(10,11,12,13), (54,25,75,37), (23.4,65.3,53,77.99)]
df1=pd.DataFrame(d1)
print(df1)
