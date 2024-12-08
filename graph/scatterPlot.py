import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

filepath = "Graph.xlsx"
data=pd.read_excel(filepath)

plt.style.use('_mpl-gallery')

# make the data
#np.random.seed(3)
#x = 4 + np.random.normal(0, 2, 24)
#y = 4 + np.random.normal(0, 2, len(x))

# size and color:
sizes = np.random.uniform(15, 80, len(data['X']))
colors = np.random.uniform(15, 80, len(data['X']))

# plot
if 'X' in data.columns and 'Y' in data.columns:
    fig, ax = plt.subplots()

    ax.scatter(data['X'],data ['Y'], s=sizes, c=colors, vmin=0, vmax=100)

    ax.set(xlim=(0, 12), xticks=np.arange(1, 12),
       ylim=(0, 12), yticks=np.arange(1, 12))

    plt.show()
else:
    print("excel file unable to create graph")