import pandas as pd

a=pd.read_excel('exp3.xlsx')
df=a['likes_count']

max = str(int(df.max()))
#print(max)
#df["decimal_scaling"] = df/(10**len(max))
#print(df["decimal_scaling"])

digit=len(str(max))
div=pow(10,digit)
s= df/div
print(s)
