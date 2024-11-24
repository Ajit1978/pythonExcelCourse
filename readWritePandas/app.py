import pandas as pd
import pandas as pyExcel

df = pd.read_excel('inventory.xlsx','Sheet1')
print(df)

# df = pd.to_excel('inventroy.xlsx','Sheet1',index=False)
# print(df)