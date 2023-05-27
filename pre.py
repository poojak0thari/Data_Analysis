import csv
import sys
import pandas as pd
import numpy as np
from matplotlib.patches import Patch
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt


df= pd.read_csv(r'Book.csv')
print(df)
#to print upto 4 columns
print(df.head(4))



#to display delected files
pd.read_csv('Book.csv',header=0)
data = pd.DataFrame(df, columns=['Unit_cost', 'Quantity'])
print(data)


#to add new column by multiplying data from given columns in csv file
Total =  np.around (df["Unit_cost"]*df["Quantity"])
#print(Total)
df.insert(4, column = "TOTAL", value = Total)  
print(df)


#to plot line chart
df.plot()
plt.show()


#to plot bar chart
df["TOTAL"].plot(kind = 'hist')
plt.show()
#Two  lines to make our compiler able to draw:
plt.savefig(sys.stdout.buffer)
sys.stdout.flush()


#pie chart
TOTAL = df["TOTAL"]
Quantity = df["Quantity"]
colors = ["#1f77b4", "#ff7f0e", "#2ca02c"]
explode = (0.1, 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0)  
plt.pie(TOTAL, labels=Quantity, explode=explode, colors=colors,
autopct='%1.1f%%', shadow=True, startangle=140)
plt.title("TOTAL BY QUANTITY")
plt.show()



#surface chart-3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
x = df["ID"].values
y = df["TOTAL"].values
z = df["Quantity"].values
ax.scatter(x, y, z, c='r', marker='o')
plt.show()
