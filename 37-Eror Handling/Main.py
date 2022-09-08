# mengatasi eror pada program pyhton
"""
try digunakan pada program apakah akan ada eror atau tidak
except digunakan untuk menangani program yang eror
finally digunakan untuk menjalankan kode tanpa memperdulikan try dan except
"""

# kasus 1
"""
try:
    f = open("demofile.txt", "r")
    try:
        print(f.read())
        f.write("Hai Cantikk") # akan eror
        f.write("\nApa Kabar?") # akan eror
    except:  # pesan dalam eror dan tidak berhentikan program
        print("Something went wrong when writing to the file")
    finally:
        f.close()
except:
    print("Something went wrong when opening the file")
"""

# kasus 2
"""
try:
    f = open("demofile.txt", "w")
    try:
        print(f.read())  # akan eror
        f.write("Hai Cantikk")
        f.write("\nApa Kabar?")
    except:  # pesan dalam eror dan tidak berhentikan program
        print("Something went wrong when writing to the file")
    finally:
        f.close()
except:
    print("Something went wrong when opening the file")
"""

# kasus 3
# """
try:
    f = open("demofile.txt", "x")
    try:
        f.write("Hai Cantikk")
        f.write("\nApa Kabar?")
        f.close()
        f = open("demofile.txt", "r")
        print(f.read())  # apabila file belum ada maka file dapat dibaca
        f.close()
    except:
        print("Something went wrong when writing to the file")
    finally:
        f.close()
except:  # akan eror apabila file tersebut sudah ada dan try turunan tidak akan berjalan
    print("Something went wrong when opening the file")
# """
