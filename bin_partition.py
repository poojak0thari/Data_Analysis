import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


a= pd.read_excel(r"exp3.xlsx")
min=(a['raw_price']).min()
max=(a['raw_price']).max()
list= a['raw_price']
list1= sorted(list, reverse=True)
#print(min, max)


bins = np.linspace(min,max,5, dtype=float)
#print(bins)
labels = ['bin4', 'bin3', 'bin2', 'bin1']


a['bins'] = pd.cut(list1, bins=bins, labels=labels, include_lowest=True)
print(a['bins'])
plt.hist(a['bins'], bins=4)
plt.show()








