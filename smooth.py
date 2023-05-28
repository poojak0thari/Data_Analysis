import array
import pandas as pd
import numpy as np
import math
import matplotlib.pyplot as plt


a= pd.read_excel(r"exp3.xlsx")
min=(a['current_price']).min()
max=(a['current_price']).max()
#print(min, max)

bins = np.linspace(min,max,4, dtype=float)
#print(bins)
labels = ['bin1', 'bin2', 'bin3', 'bin4']


a['bin_qcut'] = pd.qcut(a['current_price'], q=4, precision=1, labels=labels)
#print(a)
s=a.sort_values(by=['current_price','bin_qcut'])[['current_price','bin_qcut']]
#print(s)
new=(s['current_price'])



   


    




#plt.hist(a['bins'], bins=3)
#plt.show()






