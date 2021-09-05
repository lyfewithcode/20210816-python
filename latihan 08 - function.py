#---------- deklarasi function

#tanpa parameter
def halo():
   print("Halo, teman-teman!")

#tanpa parameter
def tambah():
   return 3 + 4

#dengan parameter
def kali(n_1, n_2):
   return n_1 * n_2

#dengan parameter
def sebutdatadiri(nm, tl, us):
   print("Namaku "+ nm)
   print("Telepon "+ tl)
   print("Usia "+ us +" Tahun")

#-------- program utama

halo()

tambah()

print("Hasil penjumlahan", tambah())

print("Hasil perkalian", kali(3, 4))

sebutdatadiri("Maria", "08138767876", "17")