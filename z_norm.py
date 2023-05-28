import pandas as pd
from scipy.stats import zscore


d= pd.read_excel('exp3.xlsx')
mean = d["likes_count"].mean()     
std_dev = d["likes_count"].std()
d["z_score"] = (d['likes_count'] - mean)/std_dev
print(d[['z_score',"likes_count" ]])


#d["likes_count"] = zscore(d["likes_count"])
#print(d["likes_count"])