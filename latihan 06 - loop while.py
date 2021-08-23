count = 0

while count < 5:
    print(count)
    count += 1 #sama dengan "count = count + 1"

#while - break [jika count >= 5 maka hentikan looping]
while True:
    print(count)
    count += 1 #increment
    if (count >= 5):
        break

#studi kasus : cetak nomor ganjil
for x in range(10):
    #cek ganjilnya
    if x % 2 == 0: #modulus
        continue
    print(x)

