import pandas as pd
import pandas as pyExcel

df=pd.read_excel('salesData.xlsx','salesData')
# print(df)

filterData=df.loc[(df["Gender"]=="Male")]
print (filterData)

filterData.to_excel("FilterSalesMale.xlsx", index=False)