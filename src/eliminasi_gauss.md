---
title: Eliminasi Gauss
date: 2026-03-02
---

## Pengertian

Dalam aljabar linier, eliminasi gauss merupakan metode untuk menyelesaikan Sistem Persamaan Linier (SPL) dengan cara merubah SPL menjadi matriks. Tujuan dari eliminasi gauss adalah bentuk eselon baris. Terdapat teknik-teknik tersendiri untuk mencapai bentuk eselon baris.

## Representasi Sistem Persamaan Linier dalam Matriks

Sebagai contoh, terdapat sistem persamaan linier sebagai berikut.

$$
\begin{aligned}
a_{1}x_{1} + b_{2}y_{1} + c_{3}z_{1} &= d_1 \\
a_{1}x_{2} + b_{2}y_{2} + c_{3}z_{2} &= d_2 \\
a_{1}x_{3} + b_{2}y_{3} + c_{3}z_{3} &= d_3
\end{aligned}
$$

Jika persamaan diatas diubah ke bentuk matriks teraugmentasi (diperbesar), maka hasilnya adalah sebagai berikut.

$$
\left[\begin{array}{ccc|c}
a_{1}x_{1} & b_{2}y_{1} & c_{3}z_{1} & d_1 \\
a_{1}x_{2} & b_{2}y_{2} & c_{3}z_{2} & d_2 \\
a_{1}x_{3} & b_{2}y_{3} & c_{3}z_{3} & d_3
\end{array}\right]
$$

### Tujuan Eliminasi Gauss

Tujuan utama dari metode eliminasi gauss adalah mengubah matriks menjadi bentuk **eselon baris**. Eselon baris memiliki beberapa ciri-ciri, antara lain:

- Pivot pada setiap baris berada lebih ke kanan dibanding baris sebelumnya.
- Semua elemen di bawah pivot bernilai nol.

Setelah matriks telah mencapai bentuk **eselon baris**, maka barulah solusi dapat diperoleh dengan metode substitusi balik.

## Operasi Baris Elementer

Terdapat tiga operasi dasar yang disebut operasi baris elementer untuk merubah matrix menjadi bentuk eselon baris, antara lain:

1. Menukar dua baris
2. Mengalikan satu baris dengan konstanta yang bukan nol
3. Menambahkan kelipatan suatu baris ke baris lain

## Contoh Penyelesaian SPLTV dengan Eliminasi Gauss

### Soal

Tentukan himpunan penyelesaian dari persamaan dibawah ini:

$$
x + y + z &= 6 \\
x + 2y - z &= 2 \\
2x - y + z &= 3
$$

### Langkah Penyelesaian

1. Buat matrix teraugmentasi

$$
\left[\begin{array}{ccc|c}
1 & 1 & 1 & 6 \\
1 & 2 & -1 & 2 \\
2 & -1 & 1 & 3
\end{array}\right]
$$

Kita anggap:
- $\text{b1}$ = Baris 1
- $\text{b2}$ = Baris 2
- $\text{b3}$ = Baris 3

2. Baris 2 = $-1 \times \text{b1} + \text{b2}$

$$
\left[\begin{array}{ccc|c}
1 & 1 & 1 & 6 \\
0 & 1 & -2 & -4 \\
2 & -1 & 1 & 3
\end{array}\right]
$$

3. Baris 3 = $-2 \times \text{b1} + \text{b3}$

$$
\left[\begin{array}{ccc|c}
1 & 1 & 1 & 6 \\
0 & 1 & -2 & -4 \\
0 & -3 & -1 & -9
\end{array}\right]
$$

4. Baris 3 = $3 \times \text{b1} + \text{b3}$

$$
\left[\begin{array}{ccc|c}
1 & 1 & 1 & 6 \\
0 & 1 & -2 & -4 \\
0 & 0 & -7 & -21
\end{array}\right]
$$

5. Baris 3 = $\text{b3} \times (-\frac{1}{7})$

$$
\left[\begin{array}{ccc|c}
1 & 1 & 1 & 6 \\
0 & 1 & -2 & -4 \\
0 & 0 & 1 & 3
\end{array}\right]
$$

6. Subsitusi Balik

Dari OBE sebelumnya, didapatkan:

$$
x + y + z &= 6 \\
y - 2z &= -4 \\
z &= 3
$$

> Variabel $z$

$$
z &= 3
$$

> Variabel $y$

$$
y - 2z &= -4 \\
y - 2(3) &= -4 \\
y - 6 &= -4 \\
y &= -4 + 6 \\
y &= 2
$$

> Variabel $z$

$$
x + y + z &= 6 \\
x + 2 + 3 &= 6 \\
x + 5 &= 6 \\
x &= 6 - 5 \\
x &= 1
$$

7. Himpunan Penyelesaian

> Solusi:

$$
x &= 1 \\
y &= 2 \\
z &= 3
$$

> Maka, himpunan penyelesaiannya adalah $\{1, 2, 3\}$

## Contoh Penyelesaian SPL Lima Variabel dengan Eliminasi Gauss

### Soal

Tentukan himpunan penyelesaian dari sistem persamaan linear berikut:

$$
a + b + c + d + e &= 5 \\
a + 2b + 2c + 2d + 2e &= 9 \\
a + 2b + 3c + 3d + 3e &= 12 \\
a + 2b + 3c + 4d + 4e &= 14 \\
a + 2b + 3c + 4d + 5e &= 15
$$

### Langkah Penyelesaian

1. Buat matriks teraugmentasi

$$
\left[\begin{array}{ccccc|c}
1 & 1 & 1 & 1 & 1 & 5 \\
1 & 2 & 2 & 2 & 2 & 9 \\
1 & 2 & 3 & 3 & 3 & 12 \\
1 & 2 & 3 & 4 & 4 & 14 \\
1 & 2 & 3 & 4 & 5 & 15
\end{array}\right]
$$

Kita anggap:
- $\text{b1}$ = baris 1
- $\text{b1}$ = baris 2
- $\text{b1}$ = baris 3
- $\text{b1}$ = baris 4
- $\text{b1}$ = baris 5

2. Baris 2 (Nolkan $\text{a}_{21}$)

> Operasi: $-1 \times \text{b1} + \text{b2}$

$$
\left[\begin{array}{ccccc|c}
1 & 1 & 1 & 1 & 1 & 5 \\
0 & 1 & 1 & 1 & 1 & 4 \\
1 & 2 & 3 & 3 & 3 & 12 \\
1 & 2 & 3 & 4 & 4 & 14 \\
1 & 2 & 3 & 4 & 5 & 15
\end{array}\right]
$$

3. Baris 3 (Nolkan $\text{a}_{31}$ dan $\text{a}_{32}$)

> Operasi 1: $-1 \times \text{b1} + \text{b3}$

$$
\left[\begin{array}{ccccc|c}
1 & 1 & 1 & 1 & 1 & 5 \\
0 & 1 & 1 & 1 & 1 & 4 \\
0 & 1 & 2 & 2 & 2 & 7 \\
1 & 2 & 3 & 4 & 4 & 14 \\
1 & 2 & 3 & 4 & 5 & 15
\end{array}\right]
$$

> Operasi 2: $-1 \times \text{b2} + \text{b3}$

$$
\left[\begin{array}{ccccc|c}
1 & 1 & 1 & 1 & 1 & 5 \\
0 & 1 & 1 & 1 & 1 & 4 \\
0 & 0 & 1 & 1 & 1 & 3 \\
1 & 2 & 3 & 4 & 4 & 14 \\
1 & 2 & 3 & 4 & 5 & 15
\end{array}\right]
$$

4. Baris 4 (Nolkan $\text{a}_{41}$, $\text{a}_{42}$, dan $\text{a}_{43}$)

> Operasi 1: $-1 \times \text{b1} + \text{b4}$

$$
\left[\begin{array}{ccccc|c}
1 & 1 & 1 & 1 & 1 & 5 \\
0 & 1 & 1 & 1 & 1 & 4 \\
0 & 0 & 1 & 1 & 1 & 3 \\
0 & 1 & 2 & 3 & 3 & 9 \\
1 & 2 & 3 & 4 & 5 & 15
\end{array}\right]
$$

> Operasi 2: $-1 \times \text{b2} + \text{b4}$

$$
\left[\begin{array}{ccccc|c}
1 & 1 & 1 & 1 & 1 & 5 \\
0 & 1 & 1 & 1 & 1 & 4 \\
0 & 0 & 1 & 1 & 1 & 3 \\
0 & 0 & 1 & 2 & 2 & 5 \\
1 & 2 & 3 & 4 & 5 & 15
\end{array}\right]
$$

> Operasi 3: $-1 \times \text{b3} + \text{b4}$

$$
\left[\begin{array}{ccccc|c}
1 & 1 & 1 & 1 & 1 & 5 \\
0 & 1 & 1 & 1 & 1 & 4 \\
0 & 0 & 1 & 1 & 1 & 3 \\
0 & 0 & 0 & 1 & 1 & 2 \\
1 & 2 & 3 & 4 & 5 & 15
\end{array}\right]
$$

5. Baris 5 (Nolkan $\text{a}_{51}$, $\text{a}_{52}$, ... , $\text{a}_{54}$)

> Operasi 1: $-1 \times \text{b1} + \text{b5}$

$$
\left[\begin{array}{ccccc|c}
1 & 1 & 1 & 1 & 1 & 5 \\
0 & 1 & 1 & 1 & 1 & 4 \\
0 & 0 & 1 & 1 & 1 & 3 \\
0 & 0 & 0 & 1 & 1 & 2 \\
0 & 1 & 2 & 3 & 4 & 10
\end{array}\right]
$$

> Operasi 2: $-1 \times \text{b2} + \text{b5}$

$$
\left[\begin{array}{ccccc|c}
1 & 1 & 1 & 1 & 1 & 5 \\
0 & 1 & 1 & 1 & 1 & 4 \\
0 & 0 & 1 & 1 & 1 & 3 \\
0 & 0 & 0 & 1 & 1 & 2 \\
0 & 0 & 1 & 2 & 3 & 6
\end{array}\right]
$$

> Operasi 3: $-1 \times \text{b3} + \text{b5}$

$$
\left[\begin{array}{ccccc|c}
1 & 1 & 1 & 1 & 1 & 5 \\
0 & 1 & 1 & 1 & 1 & 4 \\
0 & 0 & 1 & 1 & 1 & 3 \\
0 & 0 & 0 & 1 & 1 & 2 \\
0 & 0 & 0 & 1 & 2 & 3
\end{array}\right]
$$

> Operasi 4: $-1 \times \text{b4} + \text{b5}$

$$
\left[\begin{array}{ccccc|c}
1 & 1 & 1 & 1 & 1 & 5 \\
0 & 1 & 1 & 1 & 1 & 4 \\
0 & 0 & 1 & 1 & 1 & 3 \\
0 & 0 & 0 & 1 & 1 & 2 \\
0 & 0 & 0 & 0 & 1 & 1
\end{array}\right]
$$

5. Substitusi Balik

Dari OBE sebelumnya, didapatkan:

$$
a + b + c + d + e &= 5 \\
b + c + d + e &= 4 \\
c + d + e &= 3 \\
d + e &= 2 \\
e &= 1
$$

> Variabel $e$

$$
e &= 1
$$

> Variabel $d$

$$
d + e &= 2 \\
d + 1 &= 2 \\
d &= 2 - 1 \\
d &= 1
$$

> Variabel $c$

$$
c + d + e &= 3 \\
c + 1 + 1 &= 3 \\
c + 2 &= 3 \\
c &= 3 - 2 \\
c &= 1
$$

> Variabel $b$

$$
b + c + d + e &= 4 \\
b + 1 + 1 + 1 &= 4 \\
b + 3 &= 4 \\
b &= 4 - 3 \\
b &= 1
$$

> Variabel $a$

$$
a + b + c + d + e &= 5 \\
a + 1 + 1 + 1 + 1 &= 5 \\
a + 4 &= 5 \\
a &= 5 - 4 \\
a &= 1 \\
$$

6. Himpunan Penyelesaian

> Solusi:

$$
a &= 1 \\
b &= 1 \\
c &= 1 \\
d &= 1 \\
e &= 1
$$

> Maka, himpunan penyelesaiannya adalah ${1, 1, 1, 1, 1}$