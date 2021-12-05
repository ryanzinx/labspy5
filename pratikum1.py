listNama=[]
listNim=[]
listTugas=[]
listUts=[]
listUas=[]
listAkhir=[]

a=0
while a==0:
    listNama.append(input("Nama: "))
    listNim.append(input("Nim: "))
    listTugas.append(input("Nilai Tugas: "))
    listUts.append(input("Nilai UTS: "))
    listUas.append(input("Nilai UAS: "))
    a=(input("Tambah Data (y/t)? "))
    if a=="y":
        a=0
    elif a=="t":
        listAkhir.append((int(tugas) * .30) + (int(uts) * .35) + (int(uas) * .35))

print("\nNama:",nama)
print("\nNIM:",nim)
print("Nilai UTS:",uts)
print("Nilai UAS:",uas)
print("Nilai Tugas:",tugas)
print("Nilai Akhir:",akhir)
