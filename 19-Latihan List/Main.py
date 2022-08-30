# latihan list input buku

list_buku = []

while True:
    print("Masukkan data buku".center(40,"-"))
    judul = input("Masukkan Judul Buku = ")
    penulis = input("Masukkan Penulis Buku = ") 
    
    buku = [judul,penulis] 
    list_buku.append(buku) 
    print(f"No | Judul | Penulis")
    for index,buku in enumerate(list_buku):
        print(f"{index+1} | {buku[0]} | {buku[1]}")
    
    print("\n",20*"-")

    while True:
        lanjut = input("Lanjut (y/n)?")
        lanjut.lower()
        if lanjut == 'n':
            break
        if lanjut == 'y':
            break
        else:
            print("Masukkan (y/n)!")
            True
    
    if lanjut == 'n':
        break

print("Selesai")