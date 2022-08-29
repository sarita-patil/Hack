import pandas as pd
df=pd.read_csv("C:\\Users\\SaritaPatil\\Desktop\\Hack\\employees.csv")
print(df)
#count no. of duplicate rows
#print(df.duplicated())
print(df.duplicated(keep=False).sum())

#count no.of columns
print(df.shape[1])
