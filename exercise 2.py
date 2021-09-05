"""
Latihan

>= 88 kriteria A
77 >= dan < 88 kriteria B
60 >= dan < 77 kriteria C 
45 >= dan < 60 kriteria D
selain itu E 
"""

nilai = 95

if nilai >= 88:
   print('A')
elif nilai >= 77 and nilai < 88:
   print('B')
elif nilai >= 60 and nilai < 77:
   print('C')
elif nilai >= 45 and nilai < 60:
   print('D')
else:
   print('E')

"""
Buatlah program untuk menampilkan bilangan 
yang memiliki kelipatan 3, jika sudah ditemukan sebanyak 
variable "sampai", maka berhenti.
Gunakan while atau for dan break 
"""

mulai = input('Mulai dari: ') #10
sampai = input('Sampai: ') #50
temuan = input('Jumlah temuan? ') #7

mulai = int(mulai)
sampai = int(sampai)
temuan = int(temuan)
  
for i in range(mulai, sampai, 3):
    print(i)
    if i is temuan:
        print('angka ditemukan', i)
        break