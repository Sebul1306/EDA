# -*- coding: utf-8 -*-
"""Tugas Titanic

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1mZHlbyGM75NAomcjD16Sl5hzZAtJ5a2B

## Investigasi sampel data titanic berikut dengan cara :
1. Cek secara head, tail, sample, info lalu observasi apa yang bisa anda peroleh ?
2. Lakukan Statistical Summary dengan mengekstrak informasi yang didapat dari observasi anda ?
3. Cek apakah ada duplikat dan bagaimana handlenya ?
4. Cek apakah ada missing value, berapa persentasenya jika ada, dan bagaimana cara handlenya ?

## Import Libraries
"""

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
pd.set_option("display.max_columns", None)
pd.set_option("display.max_rows", None)

# import data
df = pd.read_excel('titanic.xlsx')
df.head()

# Melihat 5 baris pertama
print(df.head())

# Melihat 5 baris terakhir
print(df.tail())

# Melihat sampel acak dari dataset
print(df.sample(5))

# Melihat informasi umum dataset
print(df.info())

# Statistik deskriptif untuk kolom numerik
print(df.describe())

# Statistik deskriptif untuk semua kolom termasuk non-numerik
print(df.describe(include='all'))

# Memeriksa apakah ada duplikasi
print(df.duplicated().sum())

# Menghapus baris duplikasi
df = df.drop_duplicates()

# Memastikan duplikasi telah dihapus
print(df.duplicated().sum())

# Menghitung jumlah nilai yang hilang di setiap kolom
print(df.isnull().sum())

# Menghitung persentase nilai yang hilang
print((df.isnull().sum() / len(df)) * 100)

#  Mengisi nilai yang hilang dengan rata-rata

df['age'] = df['age'].fillna(df['age'].mean())

# -Menghapus baris dengan nilai yang hilang
df = df.dropna()

# - Menghapus kolom dengan nilai yang hilang
df = df.dropna(axis=1)

# Menyimpan data ke file CSV
df.to_csv('hasil_analisis_titanic.csv', index=False)

# Menyimpan data ke file Excel
df.to_excel('hasil_analisis_titanic.xlsx', index=False)