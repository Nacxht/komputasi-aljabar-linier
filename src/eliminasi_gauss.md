---
title: Eliminasi Gauss
date: 2026-03-02
---

## Pengertian

Dalam aljabar linier, eliminasi gauss merupakan metode untuk menyelesaikan sistem persamaan linier. Metode ini bekerja dengan cara merubah persamaan menjadi matriks, dan menggunakan operasi pada matriks tersebut. Metode ini sangat berguna untuk menyelesaikan persamaan dengan banyak variabel.

Konsep dari eliminasi gauss cukup sederhana, yaitu dengan cara menghilangkan/mengeliminasi variabel secara bertahap, hingga sistem persamaan berubah menjadi bentuk yang mudah diselesaikan, dan proses ini biasanya dilakukan dengan representasi matriks.

## Representasi Sistem Persamaan Linier dalam Matriks

Sebagai contoh, terdapat sistem persamaan linier sebagai berikut.

$$
\begin{aligned}
a_{11}x_1 + a_{12}x_2 + a_{13}x_3 &= b_1 \\
a_{14}x_1 + a_{15}x_2 + a_{16}x_3 &= b_2 \\
a_{17}x_1 + a_{18}x_2 + a_{19}x_3 &= b_3
\end{aligned}
$$

Jika persamaan diatas diubah ke bentuk matriks augmentasi, maka hasilnya adalah sebagai berikut.

$$
\begin{bmatrix}
a_{11} & a_{12} & a_{13} & b_1 \\
a_{14} & a_{15} & a_{16} & b_2 \\
a_{17} & a_{18} & a_{19} & b_3
\end{bmatrix}
$$

## Operasi Baris Elementer

Eliminasi gauss menggunakan tiga operasi dasar yang disebut operasi baris elementer.

1. Menukar dua baris
2. Mengalikan satu baris dengan konstanta yang bukan nol
3. Menambahkan kelipatan suatu baris ke baris lain

### Tujuan Eliminasi Gauss

Tujuan utama dari metode eliminasi gauss adalah mengubah matriks menjadi bentuk **eselon baris**. Eselon baris memiliki beberapa ciri-ciri, antara lain:

- Pivot pada setiap baris berada lebih ke kanan dibanding baris sebelumnya.
- Semua elemen di bawah pivot bernilai nol.

Setelah matriks telah mencapai bentuk **eselon baris**, maka barulah solusi dapat diperoleh dengan metode substitusi balik.

## Contoh Penyelesaian Sistem Persamaan dengan 5 Variabel

Sebagai contoh, terdapat persamaan seebagai berikut.

$$
\begin{aligned}
x_1 + x_2 + x_3 + x_4 + x_5 &= 5 \\
2x_1 + 3x_2 + x_3 + x_4 + x_5 &= 8 \\
x_1 + 2x_2 + 3x_3 + x_4 + x_5 &= 9 \\
x_1 + x_2 + 2x_3 + 3x_4 + x_5 &= 10 \\
x_1 + x_2 + x_3 + 2x_4 + 3x_5 &= 11
\end{aligned}
$$

### Membentuk Matrix Augmentasi

Maka, langkah pertama adalah membuat matriks augmentasi dari persamaan diatas.

$$
\begin{bmatrix}
1 & 1 & 1 & 1 & 1 & 5 \\
2 & 3 & 1 & 1 & 1 & 8 \\
1 & 2 & 3 & 1 & 1 & 9 \\
1 & 1 & 2 & 3 & 1 & 10 \\
1 & 1 & 1 & 2 & 3 & 11
\end{bmatrix}
$$

### Mengeliminasi Kolom Pivot Pertama

$$
\begin{bmatrix}
1 & 1 & 1 & 1 & 1 & 5 \\
0 & 1 & -1 & -1 & -1 & -2 \\
0 & 1 & 2 & 0 & 0 & 4 \\
0 & 0 & 1 & 2 & 0 & 5 \\
0 & 0 & 0 & 1 & 2 & 6
\end{bmatrix}
$$

Detail langkah:
1. $\text{Baris 2} - 2 \times \text{Baris 1}$
2. $\text{Baris 3} - \text{Baris 1}$
3. $\text{Baris 4} - \text{Baris 1}$
4. $\text{Baris 5} - \text{Baris 1}$

### Mengeliminasi Kolom Pivot Kedua

$$
\begin{bmatrix}
1 & 1 & 1 & 1 & 1 & 5 \\
0 & 1 & -1 & -1 & -1 & -2 \\
0 & 0 & 3 & 1 & 1 & 6 \\
0 & 0 & 1 & 2 & 0 & 5 \\
0 & 0 & 0 & 1 & 2 & 6
\end{bmatrix}
$$

Detail langkah:
1. $\text{Baris 3} - \text{Baris 2}$

### Mengeliminasi Kolom Pivot Ketiga

$$
\begin{bmatrix}
1 & 1 & 1 & 1 & 1 & 5 \\
0 & 1 & -1 & -1 & -1 & -2 \\
0 & 0 & 3 & 1 & 1 & 6 \\
0 & 0 & 0 & \frac{5}{3} & -\frac{1}{3} & \frac{7}{3} \\
0 & 0 & 0 & 1 & 2 & 6
\end{bmatrix}
$$

Detail langkah:
1. $\text{Baris 4} - \frac{1}{3} \times \text{Baris 3}$

### Mengeliminasi Kolom Pivot Keempat

$$
\begin{bmatrix}
1 & 1 & 1 & 1 & 1 & 5 \\
0 & 1 & -1 & -1 & -1 & -2 \\
0 & 0 & 3 & 1 & 1 & 6 \\
0 & 0 & 0 & 1 & -\frac{1}{5} & \frac{7}{5} \\
0 & 0 & 0 & 0 & \frac{11}{5} & \frac{13}{5}
\end{bmatrix}
$$

Detail langkah:
1. $\text{Baris 5} - \text{Baris 4}$

### Substitusi Balik

1. Dari variabel $x_5$:

$$
\begin{aligned}
\frac{11}{5}x_5 &= \frac{13}{5} \\
x_5 &= \frac{13}{5} \times \frac{5}{11} \\
x_5 &= \frac{13}{11}
\end{aligned}
$$

2. Dari variabel $x_4$:

$$
\begin{aligned}
x_4 - \frac{1}{5}x_5 &= \frac{7}{5} \\
x_4 &= \frac{7}{5} + \frac{1}{5} \times \frac{13}{11} \\
x_4 &= \frac{7}{5} + \frac{13}{55} \\
x_4 &= \frac{77}{55} + \frac{13}{55} \\
x_4 &= \frac{90}{55} \\
x_4 &= \frac{18}{11}
\end{aligned}
$$

3. Dari variabel $x_3$:

$$
\begin{aligned}
3x_3 + 1x_4 + 1x_5 &= 6 \\
3x_3 + \frac{18}{11} + \frac{13}{11} &= 6 \\
3x_3 + \frac{31}{11} &= 6 \\
3x_3 &= 6 - \frac{31}{11} \\
3x_3 &= \frac{66}{11} - \frac{31}{11} \\
3x_3 &= \frac{35}{11} \\
x_3 = \frac{35}{33}
\end{aligned}
$$

4. Dari variabel $x_2$:

$$
\begin{aligned}
x_2 - 1x_3 - 1x_4 - 1x_5 &= -2 \\
x_2 - \frac{35}{33} - \frac{18}{11} - \frac{13}{11} &= -2 \\
x_2 - \frac{35}{33} - \frac{54}{33} - \frac{39}{33} &= -2 \\
x_2 - \frac{128}{33} &= -2 \\
x_2 &= -2 + \frac{128}{33} \\
x_2 &= -\frac{66}{33} + \frac{128}{33} \\
x_2 = \frac{62}{33}
\end{aligned}
$$

5. Dari variabel $x_1$:

$$
\begin{aligned}
x_1 + 1x_2 + 1x_3 + 1x_4 + 1x_5 &= 5 \\
x_1 + \frac{62}{33} + \frac{35}{33} + \frac{18}{11} + \frac{13}{11} &= 5 \\
x_1 + \frac{62}{33} + \frac{35}{33} + \frac{54}{33} + \frac{39}{33} &= 5 \\
x_1 + \frac{190}{33} &= 5 \\
x_1 &= 5 - \frac{190}{33} \\
x_1 &= \frac{165}{33} - \frac{190}{33} \\
x_1 = -\frac{25}{33}
\end{aligned}
$$

### Solusi Akhir

$$
\begin{aligned}
x_1 &= -\frac{25}{33} \\
x_2 &= \frac{62}{33} \\
x_3 &= \frac{35}{33} \\
x_4 &= \frac{18}{11} \\
x_5 &= \frac{13}{11}
\end{aligned}
$$

Pembuktian:

$$
\begin{aligned}
x_1 + x_2 + x_3 + x_4 + x_5 &= -\frac{25}{33} + \frac{62}{33} + \frac{35}{33} + \frac{18}{11} + \frac{13}{11} \\
&= \frac{72}{33} + \frac{31}{11} \\
&= \frac{72}{33} + \frac{93}{33} \\
&= \frac{165}{33} \\
&= 5
\end{aligned}
$$ 

Pembuktian 2:

$$
\begin{aligned}
2x_1 + 3x_2 + x_3 + x_4 + x_5 &= 2 \times -\frac{25}{33} + 3 \times \frac{62}{33} + \frac{35}{33} + \frac{18}{11} + \frac{13}{11} \\
&= \frac{-50 + 186 + 35 + 54 + 39}{33} \\
&= \frac{264}{33} \\
&= 8
\end{aligned}
$$

### Kesimpulan Persamaan

Persamaan ini merupakan tipe persamaan linier yang memiliki satu solusi.