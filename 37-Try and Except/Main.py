# mengatasi eror pada program pyhton
"""
try digunakan pada program apakah akan ada eror atau tidak
except digunakan untuk menangani program yang eror
finally digunakan untuk menjalankan kode tanpa memperdulikan try dan except
"""

try:
    f = open("demofile.txt", "r")
    try:
        print(f.read())
        f.write("Lorum Ipsum")  # akan eror
        f.write("\nLorum")  # akan eror
    except:  # pesan dalam eror dan tidak berhentikan program
        print("Something went wrong when writing to the file")
    finally:
        f.close()
except:
    print("Something went wrong when opening the file")
