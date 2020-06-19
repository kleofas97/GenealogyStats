import pandas as pd
import matplotlib.pyplot as plt
file = pd.read_csv("jany_csv.csv", sep = ';', engine='python')
print(file.head())

# Histogram of years

year = file['rok']
lastyear = year.max()
firstyear = year.min()
plt.hist(year, bins=int((lastyear-firstyear)/2),color='green')
plt.show()
month = file['miesiac']
plt.hist(month,bins=12)
plt.show()