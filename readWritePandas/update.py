import pandas as pd
from openpyxl import load_workbook

file_path = "test.xlsx"

existing_data = pd.read_excel (file_path, engine='openpyxl')

print(existing_data)

new_data = pd.DataFrame({
    "Name" : ["Amer","Akbar","Atul"],
    "English" : [90,40,10],
    "Marathi" : [35,60,15]
})

updated_data = pd.concat([existing_data,new_data],ignore_index=True)

updated_data.to_excel(file_path, engine='openpyxl')

print ("data updated successfully")