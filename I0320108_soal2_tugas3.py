#Membuat Dictionary
dict = {'Nama': 'Maurich',
        'Hobi': ['mendengarkan lagu', 'makan'],
        'Sosial Media': ['Line','Instagram','Twitter','linkedIn'],
        'Lagu Kesukaan': ['Higher', 'Mariposa', 'Supercuts'],
        'Makanan Favorit': ['ayam goreng', 'mie ayam', 'batagor']}

#Mengubah Salah Satu Hobi dan Sosial Media
dict['Hobi'][1]=('bernyanyi')
dict['Sosial Media'][3]=('WhatsApp')

#Menghapus Dua Makanan Favorit
del dict['Makanan Favorit'][0:2]

#Menambahkan Satu Hobi
dict['Hobi'].append('tidur')

print(dict)
