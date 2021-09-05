arr_siswa = [ ["Bagas", 4],
               ["Indah", 34],
               ["Sri", 43],
               ["Indra", 24] ]

#tampilkan data
print("------------------------")
print(" No.     Nama       Usia")
print("------------------------")

#loop 
for i in range(len(arr_siswa)):
   print(f'| {i+1} | {arr_siswa[i][0]} \t | {arr_siswa[i][1]} |') #\t -> tab
   
print("------------------------")