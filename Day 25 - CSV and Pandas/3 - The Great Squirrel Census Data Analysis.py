import pandas as pd

data = pd.read_csv("2018_Central_Park_Squirrel_Census_Squirrel_Data.csv")
counts = data['Primary Fur Color'].value_counts()
print(counts)
counts.to_csv('test.csv ')