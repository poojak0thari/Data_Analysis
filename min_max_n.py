import pandas as pd 

a= pd.read_excel('exp3.xlsx')
n=a['likes_count']

max= n.max()
min = n.min()
new_max = 1
new_min = 0
n["min_max"]=((n - min)/(max - min))*(new_max-new_min) + new_min
print(n["min_max"])




