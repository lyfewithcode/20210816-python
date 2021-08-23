lulusan = 'LP3I'

if lulusan == 'LP3I':
    print('Politeknik')
else:
    print('Universitas')

#operator : ==, >, <, >=, <=, !=, and, dan or
"""
studi kasus : penggolongan usia berdasarkan kemenkes RI
https://yhantiaritra.wordpress.com/2015/06/03/kategori-umur-menurut-depkes/
Masa balita         = 0 – 5 tahun,
Masa kanak-kanak    = 5 – 11 tahun.
Masa remaja Awal    = 12 – 1 6 tahun.
Masa remaja Akhir   = 17 – 25 tahun.
Masa dewasa Awal    = 26- 35 tahun.
Masa dewasa Akhir   = 36- 45 tahun.
Masa Lansia Awal    = 46- 55 tahun.
Masa Lansia Akhir   = 56 – 65 tahun.
Masa Manula         = 65 – sampai atas
"""

usia = 43
   
if usia >= 65:
   print('Manula')
elif usia >= 56 and usia < 65:
   print('Lansia akhir')
elif usia >= 46 and usia < 55:
   print('Lansia awal')
elif usia >= 36 and usia < 45:
   print('Dewasa akhir')
elif usia >= 26 and usia < 35:
   print('Lansia awal')
elif usia >= 17 and usia < 26:
   print('Remaja akhir')
elif usia >= 12 and usia < 17:
   print('Remaja awal')
elif usia >= 5 and usia < 12:
   print('Kanak-kanak')
else:
   print('Balita')