# control flow dalam python
'''
1. pass
2. continue
3. break
'''

angka = 0
while angka < 10:
    angka += 1
    print(f"angka ke-{angka}")
    if angka == 5:
        # pass # tidak berpengaruh apa - apa
        # continue # kembali ke awal loop
        break # keluar dari looping
    print("hello")
print("selesai")

