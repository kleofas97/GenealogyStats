import pandas as pd

file = pd.read_csv("jany_csv.csv", sep = ';', engine='python')
print(file.head())