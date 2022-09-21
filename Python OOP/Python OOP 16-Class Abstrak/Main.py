# class abstrack

"""
perbedaan class biasa dan class abstrack
class biasa adalah blueprint dari objek, sedangkan
class abstrack adalah blue print dari class biasa yang 
dipaksa untuk menginplementasikan method class class abstrack
"""

# untuk menggunakan class abstrack import dari abc
# abc = abstrack base class
from abc import ABC, abstractmethod


class Button(ABC):
    def __init__(self, set_link):
        self.link = set_link  # termasuk setter
        """
        implementasi self.link terdapat pada class abstrack
        apabila ingin implementasi self.link pada class biasa
        menggunakan getter dan setter
        """

    @abstractmethod  # membuat class abstrack
    def click(self):
        pass

    @property
    @abstractmethod
    def link(self):  # membuat link implementasi
        pass


class PushButton(Button):
    def click(self):
        print("Go To: {}".format(self.link))  # self.link termasuk getter

    # implementasi link dari class abstrack Button
    @Button.link.setter
    def link(self, input):  # akan setter menjadi self.link = set_link
        self.__link = input

    @link.getter  # akan getter setter diatas dan dimakukkan dalam self.link class PushButton
    def link(self):
        return self.__link


tombol1 = PushButton("https://daniels66.github.io/portfolio/")
"""
super class dari PushButton adalah Button
class Button memiliki satu input yaitu set link
"""
tombol1.click()

"""
penggunaan abstrack method jarang sekali dipakai,
apabila dipakai hanya dalam kondisi tertentu
"""
