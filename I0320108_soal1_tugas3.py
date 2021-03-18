#Membuat List Teman
teman = ['Aji', 'Alica', 'Alvin', 'Diva', 'Rana', 'Raysa', 'Rio', 'Sasa', 'Sekar', 'Stefany']

#Menampilkan Nama Teman Urutan 4,6,7
print("Nama teman indeks 4,6,7: ", teman[4], ",", teman[6], ",", teman[-3])

#Mengganti Nama Teman Urutan 3,5,9
teman[2] = 'Yola'
teman[4] = 'Yuku'
teman[-2] = 'Zafira'

#Menambahkan 2 Nama Teman
teman.append('Tsania')
teman.append('Zedi')

#Menampilkan Nama Teman dengan Perulangan
print(teman*2)

#Menampilkan Panjang List
print(len(teman))
