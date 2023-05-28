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
labels = ['bin1', 'bin2', 'bin3', 'bin4']



a['bin_qcut'] = pd.qcut(list1, q=4, precision=1, labels=labels)
#print(a['bin_qcut'])
plt.hist(a['bin_qcut'], bins=4)
plt.show()










