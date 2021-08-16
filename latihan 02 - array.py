#----array => tipe data yang memiliki banyak nilai

arr = [10, 20, 30, 40]
print(arr)

#---membaca data array
print(arr[0])
print(arr[1])
print(arr[2])
print(arr[3])
print('berapakah jumlah nilai array', len(arr)) #length

#---menambahkan nilai ke dalam array
arr.append(50) #satu nilai
print('sudah ditambahkan 50', arr)

arr = arr + [60, 70, 80, 90] #beberapa nilai
print('sudah ditambahkan 60, 70, 80, dan 90', arr)

#----menghapus array?
arr.remove(50) #menghapus berdasarkan nilai --- remove()
print('hapus nilai 50', arr)

arr.pop(3) #menghapus berdasarkan index --- pop()
print('hapus index ke-3', arr)

arr = arr * 5 #memasukan nilai sendiri 5 kali --- LOOPING
print('mengulang dirinya sendiri', arr)

#---memilih nilai array
print('index antara 0 hingga 3', arr[0:3])
print('index di bawah 3', arr[:3])
print('index ke 3 dari belakang', arr[-3:])

#---array multidimensi ( 2 dimensi )
arr_multi = [ [1, 2], [3, 4], [5, 6], [7, 8] ]
print(arr_multi)

#bagaimana?
#1 2
#3 4
#5 6
#7 8

nl = '\n'

print(f'{arr_multi[0][0]} {arr_multi[0][1]}{nl}{arr_multi[1][0]} {arr_multi[1][1]}{nl}{arr_multi[2][0]} {arr_multi[2][1]}{nl}{arr_multi[3][0]} {arr_multi[3][1]}')