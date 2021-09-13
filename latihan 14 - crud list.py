import os
from prettytable import PrettyTable


list_buah = []

def tampilkanData():
   #tampilkan data, gunakan pretty table 
   tbl = PrettyTable()
   tbl.field_names = ["No", "Nama", "Harga"] #membentuk kolom
   tbl.align["Nama"] = "l" #left
   tbl.align["Harga"] = "r" #right

   for i in range(len(list_buah)):
      tbl.add_row( [ i+1, list_buah[i][0],  list_buah[i][1] ] ) 

   print(tbl)
   #print("---------------------------------------")
   #print(" No.     Nama       harga")
   #print("---------------------------------------")

   #loop 
   #for i in range(len(list_buah)):
   #   print(f'| {i+1} | {list_buah[i][0]} \t | {list_buah[i][1]} |') #\t -> tab

   #print("---------------------------------------")


pilih = None   
while(pilih != "0"):
   os.system("cls||clear")      
   print("Data tersimpan: ", list_buah)
   pilih = input("\n===== M E N U =====\n1.Masukkan data\n2.Ubah data\n3.Hapus data\n4.Tampilkan data\n0.Keluar\nPilihan: ")

   if(pilih == "1"):
      os.system("cls||clear")
      nama = input("Nama buah: ")
      harga = input("Harga: ")

      list_buah.append([nama, harga])
   elif(pilih == "2"):
      os.system("cls||clear")

      tampilkanData()

      idx = input("Nomer buah: ")

      #ubah idx menjadi integer dan -1
      idx = int(idx) - 1

      print("--- Ubah Data ---")
      nama = input("Nama buah: ")
      harga = input("Harga: ")

      list_buah[idx] = [nama, harga]

      input("Berhasil diubah...")
   elif(pilih == "3"):
      os.system("cls||clear")

      tampilkanData()

      idx = input("Nomer buah: ")

      #ubah idx menjadi integer dan -1
      idx = int(idx) - 1

      list_buah.pop(idx)
      input("Berhasil dihapus...")

   elif(pilih == "4"):
      os.system("cls||clear")

      tampilkanData()

      input("Tekan enter untuk melanjutkan...")