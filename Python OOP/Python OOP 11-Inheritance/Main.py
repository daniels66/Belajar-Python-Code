# inheritance (pewarisan)


class Person:  # merupakan class utama
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)


class Student(Person):  # merupakan kelas turunan dengan mengambil properti dan method
    pass  # digunakan ketika tidak ingin menambahkan properti atau method baru pada class


class Friend(Person):
    def __init__(self):
        """
        __init__ dalam kelas turunan akan menimpa kelas utama
        apabila kelas turunan diinisialisasi
        """
        print(f"hallo ini dari init kelas turunan Friend")


class Fwb(Person):
    def __init__(self, fname, lname, status):
        super().__init__(fname, lname)
        """
        keyword super() digunakan untuk copy semua method dan properti dalam kelas utama
        kedalam kelas turunan, super() mengacu pada class utama (Person)
        """
        self.reliation = status

    def sapadia(self):
        print(
            f"hello {self.firstname} {self.lastname} cantik, sudah {self.reliation} belum ??"
        )


x = Person("Bili", "Candra")
x.printname()

y = Student("Daniel", "Saputra")
y.printname()

z = Friend()

# menambahkan properti dalam kelas turunan
fwb = Fwb("Okthi", "Shafira", "maried")
print(fwb.reliation)

# menambahkan properti dan method dalam kelas turunan
fwb.sapadia()
