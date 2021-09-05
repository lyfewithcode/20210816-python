class Teman:
   #_init_ merupakan function yang jalan / aktif terlebih dahulu saat class Teman diinisiasi

   #self merupakan inisiasi kedalam propertinya sendiri

   def __init__(self, nama, usia):
      self.nama = nama
      self.usia = usia

   def panggil(self):
      print("Namaku "+ self.nama + " usiaku " + self.usia)      


t = Teman("Andi", "20")
t.panggil()