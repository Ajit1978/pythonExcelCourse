import pandas as pd
import pandas as pyExcel

df=pd.read_excel('salesData.xlsx','salesData')
# print(df)

sortData=df.sort_values(by="Unit price")
print (sortData)

sortData.to_excel("SortUnitprice.xlsx", index=False)