import pandas as pd
import pandas as pyExcel

df=pd.read_excel('salesData.xlsx','salesData')
# print(df)

filterData=df.loc[(df["Payment"]=="Cash") & (df["Rating"]>=5)]

sortData=filterData.sort_values(by="City")

specific_column=sortData[["Payment", "Rating", "City"]]
print (specific_column)

sortData.to_excel("FilterSalesPayment.xlsx", index=False)
