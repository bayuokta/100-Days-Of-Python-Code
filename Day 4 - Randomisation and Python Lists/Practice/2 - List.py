province_in_indonesian = ['Jakarta', 'Jawa Barat', 'Jawa Tenga']
# update isi list
print(province_in_indonesian)
province_in_indonesian[2] = "Jawa Tengah"
print(province_in_indonesian)
province_in_indonesian_1 = ['Jawa Timur', 'Bali', 'Madura']
print(province_in_indonesian_1)
# meambahkan data baru
province_in_indonesian.append('Jawa Timur')
# menambahkan list baru kedalam list yang sudah ada
province_in_indonesian.extend(province_in_indonesian_1)
# memanggil index jakarta
print(province_in_indonesian[0])
print(province_in_indonesian)
