# Algorithms Programming #

> **Disclaimer :**
> 
> This project is for educational purposes only.

## Quest. 1 ##
Buatlah kode yang akan meminta input berupa array berisikan angka tidak berurut dan sebuah angka (n). Setelah itu, kode akan mengerluarkan output berupa array dengan angka yang sudah diurutkan serta mencari apakah terdapat 2 angka didalam array yang bila dikalikan akan menghasilkan (n).

Bila ada, akan mengerluarkan tulisan “Iya, ada 2 bilangan di dalam array yang bila dikalikan akan menghasilkan n”. Namun bila tidak ada, akan mengerluarkan “Tidak, tidak ada 2 bilangan di dalam array yang bila dikalikan menghasilkan n”.

``` Python
import numpy as np
def sorting(x): #ini adalah fungsi untuk menyusun arraynya
    for i in range(len(x)-1):
        for j in range(len(x)-1-i):
            if x[j]>x[j+1]:
                a=x[j]
                x[j]=x[j+1]
                x[j+1]=a
def perkalian(x,n): #ini adalah fungsi untuk mencari 2 komponen pada array yang akan menghasilkan n saat dikalikan
    for i in range(len(x)-1):
        for j in range(i+1,len(x)):
            if x[i]*x[j]==n:
                return 1
    return 0

n=int(input("Bilangan bulat: ")) #input n (bilangan bulat)
x=np.array(eval(input("Array: ")),dtype=int) #input x(array)

sorting(x) #susun arraynya
print("Bilangan terurut",x) #print array yang sudah tersusun
if perkalian(x,n)==0: #jika fungsi mengeluarkan 0 print "tidak ada-"
    print("Tidak ada bilangan pada array yang jika dikalikan =",n)
else: #Print "ada-" jika hasilnya 1
    print("Ada 2 bilangan pada array yang jika dikalikan akan menghasilkan",n)
```


