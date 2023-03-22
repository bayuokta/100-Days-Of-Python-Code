data = {
    'name': 'Bayu Okta Krisdianto',
    'age': '24',
    'hobby': 'Play Game'
}

data1 = {
    'name': 'Pearly',
    'age': '24',
    'hobby': 'Play Game'
}

data2 = {
    'name': 'Bayu Okta Krisdianto',
    'age': '24',
    'hobby': 'Play Game'
}

all_data = [data, data1, data2]

for i in range(len(all_data)):
    for key in all_data[i]:
        print(all_data[i].get(key))

data3 = {
    'name': 'Wulan',
    'age': '24',
    'hobby': 'Play Game',
    'travel_log': [
        {
            'indonesia': ['Jakarta', 'Karawang', 'Bandung'],
            'total_visited': 12
        },
        {
            'germanry': ['Berlin', 'Hamburg', 'Stuttgart'],
            'total_visited': 32
        }
    ]
}
