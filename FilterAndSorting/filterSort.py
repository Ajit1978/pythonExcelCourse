import pandas as pd
import pandas as pyExcel

df=pd.read_excel('salesData.xlsx','salesData')
# print(df)

filterData=df.loc[(df["Gender"]=="Female") & (df["Customer type"]=="Normal")]

sortData=filterData.sort_values(by="Quantity", ascending=False)

specific_column=sortData[["Gender", "Customer type", "Quantity"]]
print (specific_column)

sortData.to_excel("FilterSalesFemale.xlsx", index=False)
