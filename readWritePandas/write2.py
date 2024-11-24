import pandas as pd
import pandas as pyExcel

data = {
    "Name" : ["Amer","Akbar","Atul"],
    "English" : [50,40,10],
    "Marathi" : [35,30,15,88]
}

df = pd.DataFrame(data)

df.to_excel("inventory.xlsx", index=False)
