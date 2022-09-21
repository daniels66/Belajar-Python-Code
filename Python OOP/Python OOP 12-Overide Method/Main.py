# overide method dalam kelas turunan


class Person:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
        self.sapa()

    def sapa(self):
        print(f"Hello {self.fname} {self.lname}")


class laki(Person):
    def __init__(self, fname, lname, emoji):
        self.emoji = emoji
        super().__init__(fname, lname)

    # overide method
    def sapa(self):
        print(f"Hello {self.fname} {self.lname} Ganteng {self.emoji}")

    """
    untuk membuat overide method gunakan nama method yang sama, 
    akan tetapi ubah isi dalam method tersebut,
    method sapa pada class turunan akan menimpa method sapa pada class utama
    """


class perempuan(Person):
    def __init__(self, fname, lname):
        super().__init__(fname, lname)

    # overide method
    def sapa(self):
        print(f"Hello {self.fname} {self.lname} Cantik ")


laki1 = Person("Daniel", "Saputra")
perempuan1 = Person("Okthi", "Safira")
laki2 = laki("Daniel", "Saputra", ":)")
perempuan2 = perempuan("Okthi", "Safira")
