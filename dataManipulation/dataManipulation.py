import pandas as pd
import pandas as pyExcel

# df=pd.read_excel('BloodData.xlsx','Sheet2')
# print(df)

df=pd.read_excel('Crime Prediction.xlsx','Chicago Crime Prediction')
print(df)

sd=pd.describe_excel('Crime Prediction.xlsx','Chicago Crime Prediction')