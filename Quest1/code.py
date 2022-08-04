import numpy as np

#Fungsi untuk menyusun array
def sorting(x):
    for i in range(len(x)-1):
        for j in range(len(x)-1-i):
            if x[j]>x[j+1]:
                a=x[j]
                x[j]=x[j+1]
                x[j+1]=a

#Fungsi untuk mencari 2 komponen pada array yang akan menghasilkan n saat dikalikan
def perkalian(x,n):
    for i in range(len(x)-1):
        for j in range(i+1,len(x)):
            if x[i]*x[j]==n:
                return 1
    return 0

n=int(input("Bilangan bulat: ")) #input n (bilangan bulat)
x=np.array(eval(input("Array: ")),dtype=int) #input x(array)

sorting(x) #susun arraynya
print("Bilangan terurut",x) #print array yang sudah tersusun
if perkalian(x,n)==0: #jika fungsi mengeluarkan 0, print "tidak ada"
    print("Tidak ada bilangan pada array yang jika dikalikan =",n)
else: #Print "ada" jika hasilnya 1
    print("Ada 2 bilangan pada array yang jika dikalikan akan menghasilkan",n)
