arr_siswa = [
        ["John", 90, 80, 60, 85],
        ["Monica", 80, 70, 60, 90],
        ["Prince", 90, 85, 60, 90],
        ["Bob", 85, 70, 60, 90]
    ]


for i in range(0, len(arr_siswa)):
    # print(i)
    n_tugas = arr_siswa[i][1]
    n_kuis = arr_siswa[i][2]
    n_uts = arr_siswa[i][3]
    n_uas = arr_siswa[i][4]
    n_akhir = (0.35 * n_uas + 0.35 * n_uts + 0.20 * n_tugas + 0.10 * n_kuis)

    def grade():
        if n_akhir >= 85:
            print('A')
        elif n_akhir >= 80 and n_akhir < 84:
            print('A-')
        elif n_akhir >= 75 and n_akhir < 79:
            print('B+')
        elif n_akhir >= 70 and n_akhir < 74:
            print('B')
        elif n_akhir >= 65 and n_akhir < 69:
            print('B-')
        elif n_akhir >= 60 and n_akhir < 64:
            print('C+')
        elif n_akhir >= 55 and n_akhir < 59:
            print('C')
        elif n_akhir >= 50 and n_akhir < 54:
            print('C-')
        elif n_akhir >= 40 and n_akhir < 50:
            print('D')
        else:
            print('E')
    
    print("------------------------------------------------------------")
    print(" No. Nama        N.Tugas N.Kuis N.UTS N.UAS NilaiAkhir Grade")
    print("------------------------------------------------------------")


    print(f'| {i+1} | {arr_siswa[i][0]} \t | {arr_siswa[i][1]}   | {arr_siswa[i][2]}   | {arr_siswa[i][3]}  | {arr_siswa[i][4]}  | {n_akhir}')
    grade()
    
print("------------------------------------------------------------")