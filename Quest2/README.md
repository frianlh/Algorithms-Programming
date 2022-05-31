## Quest. 2 ##

Berikut adalah tabel kasus COVID-19 di Indonesia pada bulan Mei. Angka yang disajikan di dalam kotak menandakan penambahan kasus per harinya (Bila kotak kosong berarti itu bukan merupakan hari di bulan Mei (mengikuti kalender)).
| Hari | Senin | Selasa | Rabu | Kamis | Jum'at | Sabtu | Minggu
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
| **Minggu 1** | | | | | 433 | 292 | 349 |
| **Minggu 2** | 395 | 484 | 367 | 338 | 336 | 533 | 387 |
| **Minggu 3** | 233 | 4484 | 689 | 568 | 490 | 529 | 489 |
| **Minggu 4** | 496 | 486 | 693 | 973 | 634 | 949 | 526 |
| **Minggu 5** | 479 | 415 | 686 | 687 | 478 | 557 | 700 |

Berdasarkan data pada tabel di atas, buatlah grafik kenaikan kasus COVID-19 di Indonesia sekreatif mungkin. Lalu berikanlah elemen-elemen apa saja agar grafik tersebut terlihat menarik bagi pembaca, seperti memberikan warna pada garis atau lainnya.


``` Python
import numpy as np #Bertujuan untuk memanipulasi array
from matplotlib import pyplot as plt #Bertujuan untuk membuat plot di python
from scipy.interpolate import make_interp_spline, BSpline #Bertujuan untuk membuat plot yang melengkung

#Tanggal
day = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31])

#Data berdasarkan soal
tambahan = np.array([433,292,349,395,484,367,338,336,533,387,233,4484,689,568,490,529,489,496,486,693,973,634,949,526,479,415,686,687,678,557,700])

#Data ketika dijumlahkan
total_hari = np.array([433, 725, 1074, 1469, 1953, 2320, 2658, 2994, 3527, 3914, 4147, 8631, 9320, 9888, 10378, 10907, 11396, 11892, 12378, 13071, 14044, 14678, 15627, 16153, 16632, 17047, 17733, 18420, 19098, 19655, 20355])

# 500 represents number of points to make between T.min and T.max
dayy = np.linspace(day.min(), day.max(), 500) #Untuk mengatur titik pada sumbu x 
spl = make_interp_spline(day, tambahan, k=3)  #Untuk mengatur titik pada sumbu y (plot1)
spl2 = make_interp_spline(day,total_hari,k=3) #Untuk mengatur titik pada sumbu y (plot2)
smooth = spl(dayy) 
smooth2 = spl2(dayy)
plt.figure(figsize=(10,5)) #Membuat grafik berukuran 10x5
plt.plot(dayy,smooth) #Membuat plot1 dengan dayy sebagai x dan smooth sebagai y 
plt.plot(dayy,smooth2) #Membuat plot2 dengan dayy sebagai x dan smooth2 sebagai y
plt.title("Curve of COVID-19 Infection Rate",fontweight="bold",fontsize=20,color="k") #Judul plot
plt.grid(color="k",linewidth=0.5,linestyle="--",alpha=0.5) #Memberikan grid pada plot
plt.xlabel("Day",fontsize=15,color="k") #Label sumbu x dengan nama day 
plt.ylabel("Patients",fontsize=15,color="k") #Label sumbu y dengan nama patients 
plt.legend(["Number of infection per-day","Total infected"],facecolor="w") #Legend plot
plt.show() #Menampilkan plot
```
Output:
<p align="center">
  <img src="https://github.com/frianlh/Algorithms-Programming/blob/9cd04f69f585a2f37247932d465dbba6b8434d45/Quest2/Curve%20of%20COVID-19%20Infection%20Rate.png"
</p>
