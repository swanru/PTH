import os
import argparse
from time import time
import pandas as pd
import numpy 

# matrik = numpy.array([[1, 2, 3],
#         [4, 5, 6],
#         [7, 8, 9]])
# print(matrik[1][1])
# def minimal(a,b):
#     if a>b :
#         return b
#     elif a<b:
#         return a
#     else:
#         return a
# print(minimal(1,4))
# """
# TODO:
# 1. Buatlah class bernama Animal dengan ketentuan:
#     - Memiliki properti:
#       - name: string
#       - age: int
#       - species: string
#     - Memiliki constructor untuk menginisialisasi properti:
#       - name
#       - age
#       - species
# 2. Buatlah class bernama Cat dengan ketentuan:
#     - Merupakan turunan dari class Animal
#     - Memiliki method:
#       - bernama "deskripsi" yang mengembalikan nilai string berikut ini.
#         "{self.name} adalah kucing berjenis {self.species} yang sudah berumur {self.age} tahun"
#       - bernama "suara" yang akan mengembalikan nilai string "meow!"
#  3. Buatlah instance dari kelas Cat bernama "myCat" dengan ketentuan:
#     - Atribut name bernilai: "Neko"
#     - Atribut age bernilai: 3
#     - Atribut species bernilai: "Persian".
# """
class Animal:
   def __init__(self,name,age,species):
      self.name = name
      self.age = age
      self.species = species
class Cat(Animal):
   def deskripsi(self):
      return (f"{self.name} adalah kucing berjenis {self.species} yang sudah berumur {self.age} tahun")
   def suara(self):
      return ("meow!")
myCat = Cat("Neko",3,"Persian")
Suara = myCat.suara()  
print(myCat.deskripsi(),Suara)
