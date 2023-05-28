import numpy as np 
import math 
import pandas as pd

a= pd.read_excel('exp3.xlsx')
dataa = a['current_price']
data=np.sort(dataa)
#print(data)

b1=np.zeros((4,4)) 

for i in range (0,16,4): 
 k=int(i/4) 
 mean=(data[i] + data[i+1] + data[i+2]  + data[i+3] )/4
 for j in range(4): 
    b1[k,j]=mean 


for i in dataa.isnull():     
    dataa.fillna(dataa.mean(),inplace=True)
    
print(dataa)
print(b1)  


       


