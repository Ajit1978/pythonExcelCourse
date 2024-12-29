import pandas as pd
import pandas as pyExcel

# df=pd.read_excel('BloodData.xlsx','Sheet2')
# print(df)

data=pd.read_excel('Crime Prediction.xlsx','Chicago Crime Prediction')
# print(data)
# print(data.head())
data.head().to_excel("Write Head.xlsx",sheet_name="Sheet1")
# print('--------------------------------------------------')
# print(data.info())
data.info().to_excel("Write Info.xlsx",sheet_name="Sheet1")
# print('--------------------------------------------------')
# print(data.describe())
data.describe().to_excel("Write Describe.xlsx",sheet_name="Sheet1")
