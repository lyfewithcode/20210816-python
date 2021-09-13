from prettytable import PrettyTable
tbl = PrettyTable()

#membuat tabel
tbl.field_names = ["Nama", "Usia"]

#masukkan data
tbl.add_row(["Miska", "23"])
tbl.add_row(["Andi", "22"])
tbl.add_row(["Bambang", "23"])
tbl.add_row(["Agus", "20"])
tbl.add_row(["Arif", "21"])

#menampilkan data
tbl.align["Nama"] = "l"
print(tbl)