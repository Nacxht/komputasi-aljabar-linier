---
title: Eliminasi Gauss
date: 2026-03-02
---

## Pengertian

Dalam aljabar linier, eliminasi gauss merupakan metode untuk menyelesaikan sistem persamaan linier. Metode ini bekerja dengan cara merubah persamaan menjadi matriks, dan menggunakan operasi pada matriks tersebut.

Metode ini sangat berguna untuk menyelesaikan persamaan dengan banyak variabel. Untuk persamaan yang memiliki dua variabel, metode menggunakan grafik atau substitusi masih memungkinkan dilakukan. Namun ketika persamaan memiliki jumlah variabel mencapai tiga atau lebih, maka anda dapat menggunakan metode eliminasi gauss untuk menyelesaika persamaan ini.

Konsep dari eliminasi gauss cukup sederhana, yaitu dengan cara menghilangkan/mengeliminasi variabel secara bertahap, hingga sistem persamaan berubah menjadi bentuk yang mudah diselesaikan, dan proses ini biasanya dilakukan dengan representasi matriks.

## Representasi Sistem Persamaan Linier dalam Matriks

Sebagai contoh, terdapat sistem persamaan linier sebagai berikut.

```{math}
\begin{aligned}
a_{11}x_1 + a_{12}x_2 + a_{13}x_3 &= b_1 \\
a_{21}x_1 + a_{22}x_2 + a_{23}x_3 &= b_2 \\
a_{31}x_1 + a_{32}x_2 + a_{33}x_3 &= b_3
\end{aligned}
```

Jika persamaan diatas diubah ke bentuk matriks augmentasi, maka hasilnya adalah sebagai berikut.

```{math}
\begin{bmatrix}
a_{11} & a_{12} & a_{13} & b_1 \\
a_{21} & a_{22} & a_{23} & b_2 \\
a_{31} & a_{32} & a_{33} & b_3
\end{bmatrix}
```

## Operasi Baris Elementer

Eliminasi gauss menggunakan tiga operasi dasar yang disebut operasi baris elementer.

1. Menukar dua baris

```{math}
R_i \leftrightarrow R_j 
```

2. Mengalikan satu baris dengan konstanta yang bukan nol

```{math}
R_i \rightarrow kR_i
```

3. Menambahkan kelipatan suatu baris ke baris lain

```{math}
R_i \rightarrow R_i + kR_j
```

Operasi-operasi diatas tidak mengubah solusi dari sistem persamaan, tetapi membantu untuk menyederhanakan bentuk matriks.

### Tujuan Eliminasi Gauss

Tujuan utama dari metode eliminasi gauss adalah mengubah matriks menjadi bentuk **eselon baris**. Eselon baris memiliki beberapa ciri-ciri, antara lain:

- Elemen utama pada setiap baris berada lebih ke kanan dibanding baris sebelumnya.
- Semua elemen di bawah pivot bernilai nol.
- Baris nol (jika ada berada di bagian bawah).

Setelah matriks telah mencapai bentuk **eselon baris**, maka barulah solusi dapat diperoleh dengan metode substitusi balik.

## Contoh Penyelesaian Sistem Persamaan dengan 5 Variabel

Sebagai contoh, terdapat persamaan seebagai berikut.

```{math}
\begin{aligned}
1x_1 + 2x_2 + 3x_3 + 4x_4 + 5x_5 &= 15 \\
2x_1 + 3x_2 + 4x_3 + 5x_4 + 6x_5 &= 20 \\
3x_1 + 4x_2 + 5x_3 + 6x_4 + 7x_5 &= 25 \\
4x_1 + 5x_2 + 6x_3 + 7x_4 + 8x_5 &= 30 \\
5x_1 + 6x_2 + 7x_3 + 8x_4 + 9x_5 &= 35
\end{aligned}
```

### Membentuk Matrix Augmentasi

Maka, langkah pertama adalah membuat matriks augmentasi dari persamaan diatas.

```{math}
\begin{bmatrix}
1 & 2 & 3 & 4 & 5 & 15 \\
2 & 3 & 4 & 5 & 6 & 20 \\
3 & 4 & 5 & 6 & 7 & 25 \\
4 & 5 & 6 & 7 & 8 & 30 \\
5 & 6 & 7 & 8 & 9 & 35
\end{bmatrix}
```

### Mengeliminasi Kolom Pertama

Setelah membuat matriks augmentasi, maka langkah selanjutnya adalah mengeliminasi kolom pertama. Caranya adalah dengan menggunakna baris pertama sebagai pivot untuk menghilangkan elemen dibawahnya.

```{math}
\begin{aligned}
R_2 &= R_2 - 2R_1 \\
R_3 &= R_3 - 3R_1 \\
R_4 &= R_4 - 4R_1 \\
R_5 &= R_5 - 5R_1 
\end{aligned}
```

Maka hasil akhir dari operasi diatas adalah sebagai berikut.

```{math}
\begin{bmatrix}
1 & 2 & 3 & 4 & 5 & 15 \\
0 & -1 & -2 & -3 & -4 & -10 \\
0 & -2 & -4 & -6 & -8 & -20 \\
0 & -3 & -6 & -9 & -12 & -30 \\
0 & -4 & -8 & -12 & -16 & -40
\end{bmatrix}
```

### Mengeliminasi Baris Kedua

Setelah selesai mengeliminasi kolom kedua. Gunakan baris kedua sebagai pivot.

```{math}
\begin{aligned}
R_3 &= R_3 - 2R_2 \\
R_4 &= R_4 - 3R_2 \\
R_5 &= R_5 - 4R_2
\end{aligned}
```

Maka hasil dari operasi diatas adalah sebagai berikut.

```{math}
\begin{bmatrix}
1 & 2 & 3 & 4 & 5 & 15 \\
0 & -1 & -2 & -3 & -4 & -10 \\
0 & 0 & 0 & 0 & 0 & 0 \\
0 & 0 & 0 & 0 & 0 & 0 \\
0 & 0 & 0 & 0 & 0 & 0
\end{bmatrix}
```

### Analisis Hasil

Baris-baris terakhir menjadi nol. Hal ini menunjukkan bahwa sistem persamaan ini memiliki "banyak solusi", atau "tak hingga".

Artinya, beberapa variabel dapat dipilih sebgai variabel bebas, lalu variabel lainnya dinyatakan dalam bentuk variabel tersebut.

```{math}
\begin{aligned}
x_5 &= t \\
x_4 &= s \\
x_3 &= r
\end{aligned}
```

## Kesimpulan

Eliminasi gauss adalah metode penting dalam aljabar linier dapat digunakan untuk menyelesaikan sistem persamaan linier yang memiliki banyak variabel. Metode ini bekerja dengan mengubah sistem persamaan menjadi bentuk matriks teraugmentasi, lalu menyederhanakannya menggunakan operasi baris elementer hingga diperoleh bentuk eselon baris.

Karena sifatnya yang terstruktur, metode ini banyak digunakan dalam berbagai bidang seperti komputasi ilmiah, grafika komputer, dan analisis data.