import pandas as pd
import matplotlib.pyplot as plt

filepath = "Graph.xlsx"
data=pd.read_excel(filepath)

if 'X' in data.columns and 'Y' in data.columns:
    plt.figure(figsize=(16,24))
    plt.plot(data['X'],data ['Y'],marker='o', linestyle = '-',color='b', label='Coordinates')
    plt.title('Graph')
    plt.xlabel("x Coordinates")
    plt.ylabel("y Coordinates")
    plt.legend()
    plt.grid(True)
    plt.show()
else:
    print("excel file unable to create graph")