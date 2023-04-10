import pandas

data = pandas.read_csv("weather_data.csv")
print(data['temp'])

data_dict = data.to_dict()
print(data_dict)

temp_list = data['temp'].to_list()
avg_temp = data['temp'].mean()
max_temp = data['temp'].max()
min_temp = data['temp'].min()
print(temp_list)
print(f"Average\t = {avg_temp}")
print(f"Max\t\t = {max_temp}")
print(f"Min\t\t = {min_temp}")

# Get Data
print(data[data['day'] == 'Monday'])

print(data[data['temp'] == data['temp'].max()])

monday = data[data.day == "Monday"]

print(data)
data['temp'] = data['temp'].apply(lambda x: ((x * 1.8) + 32))
print(data)


data_dict = {
    "student": ["Any", "James", "Angela"],
    "scores": [76, 77, 90]
}

df = pandas.DataFrame(data_dict)
df.to_csv('new_data.csv')
print(df)
