import numpy as np 
import math 
import pandas as pd

a= pd.read_excel('exp3.xlsx')
dataa = a['current_price']

for i in dataa.isnull():     
    dataa.fillna(dataa.mean(),inplace=True)
print(dataa)

data=np.sort(dataa)

b1=np.zeros((4,4)) 

for i in range (0,16,4): 
  k=int(i/4) 
  for j in range (4): 
    if (data[i+j]-data[i]) < (data[i+2]-data[i+j]): 
      b1[k,j]=data[i] 
    else: 
      b1[k,j]=data[i+2]   

print(b1)  


       


