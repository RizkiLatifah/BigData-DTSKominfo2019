# -*- coding: utf-8 -*-
"""
Created on Tue Jul 23 13:38:18 2019

@author: Mulmed
"""
from sqlalchemy import create_engine
import pandas as pd

## JAWABAN NO 1 ##
with pd.ExcelFile('G:\\Digitalent\karyawan.xls') as xls:
    df1 = pd.read_excel(xls, 'personalia2')
    df2 = pd.read_excel(xls, 'personalia1')

## JAWABAN NO 2 ##
print("***Result Sheet 1***")
print(df1)
print("")
print("***Result Sheet 2***")
print(df2)

engine = create_engine('sqlite:///:memory:')

df1.to_sql('data1', engine)
df2.to_sql('data2', engine)

## JAWABAN NO 3 ##
belum_menikah = pd.read_sql_query('SELECT * FROM data2 WHERE Status="BELUM MENIKAH"',engine)
print(belum_menikah)

## JAWABAN NO 4 ##
res4 = pd.read_sql_query('SELECT Pendidikan,Gender,avg("Gaji Akhir") FROM data2 group by Pendidikan,Gender',engine)
print(res4)

## JAWABAN NO 5 ##
res5 = pd.read_sql_query('SELECT * FROM data1 INNER JOIN data2 ON data1.id = data2.id WHERE data2.Gender="PRIA"', engine)
print(res5)