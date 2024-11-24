import pandas as pd
import pandas as pyExcel

# df = pd.read_excel ("inventory.xlsx", "Sheet1")
# print(df)


# df = pd.read_excel ("inventory.xlsx", "Sheet1")
# print(df)

all_sheets = pd.read_excel ("inventory.xlsx" , sheet_name=None)

for sheet_name, sheet_data in all_sheets.items():
    print(sheet_name)
    print(sheet_data.head())