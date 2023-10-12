import os
import argparse
from time import time
import pandas as pd
import numpy as np
import unittest
import math
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
# class Animal:
#    def __init__(self,name,age,species):
#       self.name = name
#       self.age = age
#       self.species = species
# class Cat(Animal):
#    def deskripsi(self):
#       return (f"{self.name} adalah kucing berjenis {self.species} yang sudah berumur {self.age} tahun")
#    def suara(self):
#       return ("meow!")
# myCat = Cat("Nekoo",3,"Persian")
# Suara = myCat.suara()  
# print(myCat.deskripsi(),Suara)
# total = 4000000000
# margin = total / 12
# margin_bulan = margin / 30
# print(margin,margin_bulan)
# def LuasPersegiPanjang(panjang: int = 2, lebar: int = None):
#     luas = panjang*lebar
#     return luas

# luas_satu = LuasPersegiPanjang(lebar=2)
# print(luas_satu)
# print(math.sqrt(25))
# from scipy import stats
# jumlah_kucing = np.array([3, 2, 1, 1, 2, 3, 2, 1, 0, 1,2,3])
# modus = stats.mode(jumlah_kucing)[0]
# print(jumlah_kucing.mean(),",",np.median(jumlah_kucing),",",modus)
import matplotlib.pyplot as plt
 
cities = ('Bogor', 'Bandung', 'Jakarta', 'Semarang', 'Yogyakarta', 
          'Surakarta','Surabaya', 'Medan', 'Makassar')
 
populations = (45076704, 11626410, 212162757, 19109629, 50819826, 17579085,
               3481, 287750, 785409)
 
plt.bar(x=cities, height=populations)
plt.show()