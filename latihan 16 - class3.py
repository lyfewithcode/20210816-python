#cara mengambil beberapa class yang terpisah dalam subfolder
#1. membuat file kosong  __init__.py
from KumpulanClass.Benda import *
from KumpulanClass.Hewan import *

b = Benda('Guci', 'Keramik')
b.getJenis()
b.getBahan()

h = Hewan('Kucing', 'Meong')
h.getJenis()
h.getSuara()