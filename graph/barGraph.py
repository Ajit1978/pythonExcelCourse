import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

filepath = "Graph.xlsx"
data=pd.read_excel(filepath)

plt.style.use('_mpl-gallery')

# plot
if 'X' in data.columns and 'Y' in data.columns:
    fig, ax = plt.subplots()

    ax.bar(data['X'],data ['Y'], width=1, edgecolor="white", linewidth=0.7)

    ax.set(xlim=(0, 12), xticks=np.arange(1, 12),
       ylim=(0, 12), yticks=np.arange(1, 12))

    plt.show()
else:
    print("excel file unable to create graph")