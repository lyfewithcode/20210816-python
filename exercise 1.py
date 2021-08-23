arr_multi = [ [1, 2], [3, 4], [5, 6], [7, 8] ]

#bagaimana?
#1 2
#3 4
#5 6
#7 8

# nl = '\n'

# print(f'{arr_multi[0][0]} {arr_multi[0][1]}{nl}{arr_multi[1][0]} {arr_multi[1][1]}{nl}{arr_multi[2][0]} {arr_multi[2][1]}{nl}{arr_multi[3][0]} {arr_multi[3][1]}')

#menampilkan array
for i in range(len(arr_multi)):
   for j in range(len(arr_multi[i])):
      if j == 1:
         print (arr_multi[i][j])
      else:
        print (arr_multi[i][j], end =" ") #end =" " agar print tidak melakukan enter