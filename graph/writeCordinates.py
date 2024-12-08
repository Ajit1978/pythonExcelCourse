import pandas as pd
import pandas as pyExcel

data = {
    "X": [1, 2, 3, 4, 5],
    "Y": [350, 450, 550, 650, 100]
}
df=pd.DataFrame(data)
df.to_excel("Graph.xlsx", index=False)
