# Quest. 3 #
Pada sebuah daerah terdapat $n$ warga, misal $W_{1}, W_{2}, W_{3}, ..., W_{n}$ dimana diketahui bahwa probabilitas warga ke-i $(W_{i})$ tidak terinfeksi COVID-19 saat berada di pusat perbelanjaan adalah $\frac{1}{3i-2}$.

Buatlah algoritma yang dapat mengaproksimasi probabilitas bahwa lebih dari 90% warga yang berada di pusat perbelanjaan terinfeksi COVID-19 di saat terdapat $n$ warga di pusat perbelanjaan menggunakan simulasi 10000 kejadian terdapat $n$ warga di pusat perbelanjaan. (Gunakan 4 angka di belakang koma)

``` python
import random

#Fungsi weighted random, dengan inputnya [a,b], maka p(x=0)=a dan p(x=1)=b
def pilih(weights):
    totals = []
    running_total = 0

    for w in weights:
        running_total += w
        totals.append(running_total)

    rnd = random.random() * running_total
    for i, total in enumerate(totals):
        if rnd < total:
        	return i

print('Simulasi Covid')
print(' ')

y=0
while y==0:
	#Mulai simulasi
	n=int(input('Populasi: '))
	px=[0]*n #Array untuk probabilitas W_i tidak covid
	m=10000 #Jumlah simulasi

	for i in range(n):
		px[i]=1/(3*i-2) #Probabiitas W_i tidak covid

	h=0 #Counter sukses 90% positif covid
	for j in range(m):
		s=0 #Counter jumlah orang positif covid
		for i in range(n):
			k=pilih([px[i],1-px[i]])
			s=s+k
		if s>=9*n/10:
			h=h+1 #Apakah jumlah positif diatas 90%
		
	print('Simulasi lebih dari 90% covid: {0}'.format(h/m))
	print(' ')
	z=input('Coba lagi? yes/no ') #Mengulangi simulasi
	if z=='no':
		y=1 #Simulasi selesai
	print(' ')
  ```
  
Contoh output:
```
Simulasi Covid
 
Populasi: 20
Simulasi lebih dari 90% covid: 0.7246
 
Coba lagi? yes/no no  
```
