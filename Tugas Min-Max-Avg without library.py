# -*- coding: utf-8 -*-
"""
Created on Fri Jul 19 13:57:16 2019

@author: Latifah
"""
dict_nilai = {'Siswa A': 75,
              'Siswa B': 80,
              'Siswa C': 65 }

nilai = [int(v) for v in dict_nilai.values()]

def maksimum(nilai):
    maks = nilai[0]
    i = 0
    while i < len(nilai):
        if nilai[i] > maks :
            maks = nilai[i]
        i+=1
    return(maks)

def minimum(nilai):
    minim = nilai[0]
    i = 0
    while i < len(nilai):
        if nilai[i] < minim :
            minim = nilai[i]
        i+=1
    return(minim)    

def average(nilai):
    jumlah = 0
    for num in nilai:    
        jumlah = jumlah + num
    average = jumlah /(len(nilai))
    return(average)

for x,y in dict_nilai.items():
    nilai_maks = maksimum(nilai)
    nilai_min = minimum(nilai)
    if y==nilai_maks:        
       print("Nilai tertinggi adalah: ", y)
       print("Diperoleh oleh: ", x)
    elif y==nilai_min:
        print("Nilai terendah adalah: ", y)
        print("Diperoleh oleh: ", x)
print("Nilai Rata-rata dari", len(nilai), "orang siswa adalah: ", average(nilai))