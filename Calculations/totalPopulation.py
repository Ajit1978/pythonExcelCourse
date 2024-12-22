import pandas as pd
import pandas as pyExcel

df=pd.read_excel("BloodData.xlsx","Sheet1")
# print(df)

# summ=0
# for i in columnSum:
#     summ=summ+int(i)

# print(summ)


columnSum=df["Population"].sum()
print(columnSum)

df.loc[len(df),"Population"]=columnSum

df.to_excel("BloodData.xlsx","Sheet2", index=False)



