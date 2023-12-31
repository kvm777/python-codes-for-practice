import pandas as pd

'''
df.fillna(value)    --replace the missing data with value..
df.dropna()         --drop the rows with missing data temperory
df.dropna(inplace=True)  
'''
d = pd.read_excel("C:\\Users\\korad\\Desktop\\python examples\\modules\\pandas\\Academic.xlsx", sheet_name="marks_Missing")
#we are adding sheet_name="" if there is any other sheet in file
#creating DataFrame
df = pd.DataFrame(d)

print(df)
print()

#fething horizental rows data with no missing  
#by dafault axis=0
# axis = 0 is horizentally
print(df.dropna(axis=0))
print()

#fething vertical columns data with no missing
# axis = 1 is for vertically
print(df.dropna(axis=1))
print()

print("mean of 2-2 semester", df["2-2 Semester"].mean())
print()

print(df["2-2 Semester"].fillna(df["2-2 Semester"].mean()))
print()

# fill the data missing with thw given value.
print(df.fillna(80))
df.dropna()     #drop the rows with missing data

df.dropna(inplace=True)

print(df)


