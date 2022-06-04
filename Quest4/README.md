# Quest. 4 #
Buatlah algoritma dengan input bilangan bulat $n$, dimana $n$ adalah banyaknya karakter dari kode yang harus ditebak. Kode merupakan kombinasi acak dari karakter-karakter yang berupa huruf kecil (abcde dst.), huruf kapital (ABCDE dst.), ataupun angka 0 sampai 9.

Jadi algoritma akan berjalan terus sampai kode bisa ditebak. Perhatikan bahwa karakter yang ditebak sensitif, jadi harus sesuai apakah merupakan huruf kapital atau tidak. Jika input sesuai, maka akan dilanjutkan untuk menebak karakter selanjutnya, tetapi jika tidak sesuai maka akan diulang terus menerus hingga sesuai, dan jika kita memasukan input “menyerah” maka akan langsung berakhir dan jawaban akan ditampilkan.

``` python
import string
import random

n=int(input("Panjang karakter : ")) #Input n (bilangan bulat) menentukan banyak karakter
c= ''.join(random.choice(string.digits+string.ascii_uppercase+string.ascii_lowercase) for i in range(n))
b=0 #b akan ditetapkan sebagai 0, b adalah counter untuk karakter yang berhasil ditebak
a=3 #Nilai a=3 adalah pilihan acak, karena nanti a akan diganti dengan 0 atau 1

while b<=n-1:
    print("Jika sudah tidak tahan lagi, ketik MENYERAH")
    t=input("Tebak karakter ke {} ".format(b+1))
    if t==c[b]: #Jika nilai t = karakter ke b, artinya benar
        print("Benar")
        a=1 #Nilai a akan diganti menjadi 1
        b=b+1 #Nilai b akan naik 
    elif t==("MENYERAH"): #Jika nilai t adalah menyerah maka a akan menjadi 0
        a=0
        break
    else: #Kalau a tetap tidak menjadi 1 atau 0, artinya salah
        print("Salah,coba lagi")

if b==n: #Jika nilai b sudah naik sampai ke n, artinya game selesai
    print("Selamat!, kodenya ",c)
else: #Jika b tidak naik sampai ke n artinya penebak menyerah ditengah jalan, game selesai
    print("Makasih sudah main, kodenya adalah",c)
```

Contoh output:
```
Panjang karakter : 3
Jika sudah tidak tahan lagi, ketik MENYERAH
Tebak karakter ke 1 A
Salah,coba lagi
Jika sudah tidak tahan lagi, ketik MENYERAH
Tebak karakter ke 1 MENYERAH
Makasih sudah main, kodenya adalah nlu
```
