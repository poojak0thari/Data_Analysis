import numpy
from numpy import percentile
import csv
import pandas as pd
import math
import matplotlib.pyplot as plt
import scipy.stats as stats

df= pd.read_csv(r"product.csv")
#print(df["current_price"])
cp=df["current_price"]

print("Min:" + str(numpy.min(cp)))
minimum = numpy.min(df["current_price"])

print("Max:" + str( numpy.max(cp)))
maximum = numpy.max(cp)

print("Median:" + str(numpy.median(cp)))
median = numpy.median(cp)

quartiles = percentile(cp, [25,75])
print('Q1:' + str( quartiles[0]))
print('Q3: ' +str ( quartiles[1]))

#plt.boxplot(cp)
#plt.title("Current Price BoxPlot")
#plt.show(cp)



n = 16
observation = cp.random.binomial(n, 0.16, size=16)/n

z = (observation-cp.mean(observation))/cp.std(observation)

stats.probplot(z, dist="norm", plot=plt)
plt.title("Normal Q-Q plot")
plt.show()




