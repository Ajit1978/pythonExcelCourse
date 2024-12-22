import pandas as pd
import pandas as pyExcel

df=pd.read_excel("BloodData.xlsx","Sheet2")
# print(df)

column1=df["Population"]
column2=df["O Plus"]
print(column1)
print(column2)

column3=[]

size=len(df)
for i in range(0, size):
    # column3.append(float(column1[i]*column2[i]))
    df.loc[i,"O Plus Peoples"]=column1[i]*column2[i]

# print(column3)

# df.loc[len(df),"O Plus Peoples"]=columnSum

df.to_excel("BloodData.xlsx","Sheet2", index=False)