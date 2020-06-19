import pandas as pd
import matplotlib.pyplot as plt
file = pd.read_csv("jany_birth_csv.csv", sep = ';', engine='python')
print(file.head())

# Histogram of years

year = file['rok']
lastyear = year.max()
firstyear = year.min()
plt.hist(year, bins=int((lastyear-firstyear)/2),color='green')
plt.xlabel('Years')
plt.ylabel('Number of births')
plt.savefig('Years')
plt.show()
month = file['miesiac']
plt.hist(month,bins=12,color='green')
plt.xlabel('Months')
plt.ylabel('Number of births')
plt.savefig('Months')
plt.show()