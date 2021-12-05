# Dictionary

# ==================== #
# Nama | Nomor Telepon #
# ==================== #
# Ari  | 081267888     #
# Dina | 087677776     #
# ==================== #

a = {"Ari":"081267888","Dina":"087677776"}

# Tampilkan Kontaknya Ari
print("Tampilkan kontaknya Ari adalah",a["Ari"])

# Tambah kontak baru dengan nama Riko, nomor 087654544
a['Riko'] = "087654544"
print("Tambah kontak baru dengan nama Riko adalah",a)

# Ubah kontak Dina dengan nomor baru 088999776
a['Dina'] = "088999776"
print("Ubah kontak Dina dengan nomor baru adalah",a)

# Tampilkan semua nama
print("Tampilkan semua nama adalah",a.keys())

# Tampilkan semua nomor
print("Tampilkan semua nomor adalah",a.values())

# Tampilkan daftar nama dan nomornya
print("Tampilkan daftar nama dan nomornya adalah",a.items())

# Hapus kontak Dina
del a ["Dina"]
print("Hapus kontak Dina adalah",a)
