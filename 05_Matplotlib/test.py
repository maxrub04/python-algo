
import numpy as np
import matplotlib.pyplot as plt
#Plotting a simple line graph
days=[1,2,3,4,5]
prices=[3500,3600,3200,3000,3900]
plt.figure(figsize=(10,6))
plt.plot(days,prices,marker="o",linestyle="-",color="b")
plt.title("Price change over 5 days")
plt.xlabel("Days")
plt.ylabel("USD")
plt.grid(True)
plt.show()

#Plotting a bar charts
Assets=["USD/JPY","EUR/USD","GBP/USD"]
Volume=[1000,1200,1100]
plt.figure(figsize=(10,6))
plt.bar(Assets,Volume,color=["gold","silver","#CD7F32"])
plt.title("Assets Volume")
plt.xlabel("Asset")
plt.ylabel("Volume")
plt.show()


#Plotting histograms
price_sample=np.random.normal(3000,1000,10000)

plt.figure(figsize=(10,6))
plt.hist(price_sample,bins=100,color="skyblue",edgecolor="black")
plt.title("Price sample")
plt.xlabel("USD")
plt.ylabel("Frequency")
plt.show()