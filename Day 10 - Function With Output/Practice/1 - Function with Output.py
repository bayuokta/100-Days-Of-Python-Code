def format_name(first_name:str, last_name:str):
    """
    sebuah fungsi untuk menggabungkan nama depan dan belakang
    selanjutnya akan membuat huruf kapital di awal nama
    :param first_name:
    :param last_name:
    :return:
    """
    if first_name == "" or last_name == "":
        return 'Tidak boleh kosong'
    return f'{first_name.title()}, {last_name.title()}'


print(format_name('', ''))
