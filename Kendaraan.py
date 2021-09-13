class Kendaraan:

   def __init__(self, jns, mrk, sr, rd, cc):
      self.jenis = jns
      self.merek = mrk
      self.seri = sr
      self.roda = rd
      self.cc = cc

   def getJenis(self):
      print(self.jenis)      

   def getMerek(self):
      print(self.merek)      

   def getSeri(self):
      print(self.seri)      

   def getRoda(self):
      print(self.roda)      

   def getCC(self):
      print(self.cc)