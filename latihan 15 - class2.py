#cara import seluruh method pada class Kendaraan 
from Kendaraan import * 

#cara import beberapa method pada class Kendaraan
#from Kendaraan import getJenis, getMerek

k = Kendaraan('Motor', 'Honda', 'Beat', 2, 125)
k.getJenis()
k.getMerek()
k.getSeri()
k.getRoda()
k.getCC()