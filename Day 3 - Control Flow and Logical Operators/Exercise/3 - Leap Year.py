year = int(input("Masukkan tahun: "))

message = ""
# algoritma pertama
if year % 400 == 0:
    message = "Tahun Kabisat"
else:
    if year % 100 == 0:
        message = "Bukan Tahun Kabisat"    
    else:
        if year % 4 == 0:
            message = "Tahun kabisat"
        else:
            message = "Bukan Tahun kabisat"
            
# algoritma kedua
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            message = "Tahun Kabisat"
        else:
            message = "Bukan Tahun Kabisat"
    else:
        message = "Bukan Tahun Kabisat"
else:
    message = "Bukan Tahun Kabisat"
            
    
print(f'Tahun {year}, {message}')