import pandas as pd
import pandas as pyExcel

df=pd.read_excel("BloodData.xlsx","Sheet2")
# print(df)

column1=df["O Plus"]
print(column1)

sum=0
for i in column1:
    sum=sum+float(i)

avg=sum/len(df)
print(avg)

# df.loc[len(df),"Population"]=columnSum

# df.to_excel("BloodData.xlsx","Sheet2", index=False)



