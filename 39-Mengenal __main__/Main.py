# kegunaan __main__ dalam pyhton

"""
dalam bahasa cpp gerbang untuk memulai program ditandai dengan 

int main(){
    
}

sedangkan pada bahasa java 

class main (){
    public static void main(){

    }
}

pada bahasa pyhton tidak ada, oleh karena itu diperkenalkan __main__
sebagai gerbang pada pyhton
"""

print(f"__name dalam main.py adalah = {__name__}")  # akan memunculkan hasil __main__

"""
programer biasanya menggunakan __name__ sebagai awal program
if __name__ == "__main__":
    x = 30
    print(f"nilai x = {x}")
"""

if __name__ == "__main__":
    x = 30
    print(f"nilai x = {x}")
