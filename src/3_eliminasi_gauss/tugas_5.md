---
title: Tugas 5 - SPL 5 Variabel
---

## Penyelesaian Sistem Persamaan Linear 5 Variabel dengan Eliminasi Gauss

Dokumen ini menyajikan langkah-langkah penyelesaian Sistem Persamaan Linear (SPL) yang terdiri dari 5 variabel dan 5 persamaan menggunakan metode **Eliminasi Gauss**. Solusi akhir dari sistem persamaan ini adalah: 
$$x_1 = 1, \; x_2 = 2, \; x_3 = 3, \; x_4 = 4, \; x_5 = 5$$

---

### 1. Sistem Persamaan Linear

Sistem persamaan linear yang akan diselesaikan didefinisikan sebagai berikut:

$$
\begin{aligned}
x_1 + x_2 + x_3 + x_4 + x_5 &= 15 \quad &\text{(Persamaan I)} \\
2x_1 + 3x_2 + 2x_3 + 2x_4 + 2x_5 &= 32 \quad &\text{(Persamaan II)} \\
x_1 + 2x_2 + 3x_3 + 2x_4 + 2x_5 &= 32 \quad &\text{(Persamaan III)} \\
x_1 + x_2 + 2x_3 + 3x_4 + 2x_5 &= 31 \quad &\text{(Persamaan IV)} \\
x_1 + x_2 + x_3 + 2x_4 + 3x_5 &= 29 \quad &\text{(Persamaan V)}
\end{aligned}
$$

---

### 2. Representasi Matriks Diperbesar (Augmented Matrix)

Persamaan linear di atas disusun ke dalam matriks diperbesar (*augmented matrix*) untuk mempermudah manipulasi baris:

$$
\left[
\begin{array}{ccccc|c}
1 & 1 & 1 & 1 & 1 & 15 \\
2 & 3 & 2 & 2 & 2 & 32 \\
1 & 2 & 3 & 2 & 2 & 32 \\
1 & 1 & 2 & 3 & 2 & 31 \\
1 & 1 & 1 & 2 & 3 & 29
\end{array}
\right]
$$

---

### 3. Proses Operasi Baris Elementer (OBE)

Tujuan utama operasi baris elementer adalah mentransformasikan matriks diperbesar tersebut menjadi bentuk **Eselon Baris (Segitiga Atas)**.

#### **Langkah A: Eliminasi Elemen Kolom Pertama di Bawah Diagonal Utama**
Baris pertama ($R_1$) bertindak sebagai baris pivot. Elemen pivot ($a_{11} = 1$) digunakan untuk menghilangkan elemen kolom pertama pada baris $R_2$, $R_3$, $R_4$, dan $R_5$.

* **Transformasi Baris Kedua ($R_2 \leftarrow R_2 - 2R_1$):**
  Untuk mengubah angka $2$ di kolom pertama menjadi $0$, kurangi elemen baris kedua dengan dua kali elemen baris pertama yang bersesuaian.
  $$
  \begin{aligned}
  R_2 &= [2, 3, 2, 2, 2 \mid 32] - 2 \times [1, 1, 1, 1, 1 \mid 15] \\
      &= [2-2, \; 3-2, \; 2-2, \; 2-2, \; 2-2 \mid 32-30] \\
      &= [0, 1, 0, 0, 0 \mid 2]
  \end{aligned}
  $$

* **Transformasi Baris Ketiga ($R_3 \leftarrow R_3 - R_1$):**
  Kurangi elemen baris ketiga dengan elemen baris pertama yang bersesuaian.
  $$
  \begin{aligned}
  R_3 &= [1, 2, 3, 2, 2 \mid 32] - [1, 1, 1, 1, 1 \mid 15] \\
      &= [1-1, \; 2-1, \; 3-1, \; 2-1, \; 2-1 \mid 32-15] \\
      &= [0, 1, 2, 1, 1 \mid 17]
  \end{aligned}
  $$

* **Transformasi Baris Keempat ($R_4 \leftarrow R_4 - R_1$):**
  Kurangi elemen baris keempat dengan elemen baris pertama yang bersesuaian.
  $$
  \begin{aligned}
  R_4 &= [1, 1, 2, 3, 2 \mid 31] - [1, 1, 1, 1, 1 \mid 15] \\
      &= [1-1, \; 1-1, \; 2-1, \; 3-1, \; 2-1 \mid 31-15] \\
      &= [0, 0, 1, 2, 1 \mid 16]
  \end{aligned}
  $$

* **Transformasi Baris Kelima ($R_5 \leftarrow R_5 - R_1$):**
  Kurangi elemen baris kelima dengan elemen baris pertama yang bersesuaian.
  $$
  \begin{aligned}
  R_5 &= [1, 1, 1, 2, 3 \mid 29] - [1, 1, 1, 1, 1 \mid 15] \\
      &= [1-1, \; 1-1, \; 1-1, \; 2-1, \; 3-1 \mid 29-15] \\
      &= [0, 0, 0, 1, 2 \mid 14]
  \end{aligned}
  $$

Setelah transformasi kolom pertama selesai, diperoleh matriks baru sebagai berikut:
$$
\left[
\begin{array}{ccccc|c}
1 & 1 & 1 & 1 & 1 & 15 \\
0 & 1 & 0 & 0 & 0 & 2 \\
0 & 1 & 2 & 1 & 1 & 17 \\
0 & 0 & 1 & 2 & 1 & 16 \\
0 & 0 & 0 & 1 & 2 & 14
\end{array}
\right]
$$

---

#### **Langkah B: Eliminasi Elemen Kolom Kedua di Bawah Diagonal Utama**
Baris kedua ($R_2$) digunakan sebagai baris pivot baru. Elemen pivot ($a_{22} = 1$) digunakan untuk menolkan kolom kedua pada baris di bawahnya. 
*(Catatan: Kolom kedua pada baris keempat dan kelima sudah bernilai $0$, sehingga operasi OBE hanya diterapkan pada baris ketiga).*

* **Transformasi Baris Ketiga ($R_3 \leftarrow R_3 - R_2$):**
  Kurangi elemen baris ketiga dengan elemen baris kedua yang bersesuaian.
  $$
  \begin{aligned}
  R_3 &= [0, 1, 2, 1, 1 \mid 17] - [0, 1, 0, 0, 0 \mid 2] \\
      &= [0-0, \; 1-1, \; 2-0, \; 1-0, \; 1-0 \mid 17-2] \\
      &= [0, 0, 2, 1, 1 \mid 15]
  \end{aligned}
  $$

Setelah transformasi kolom kedua selesai, diperoleh matriks baru sebagai berikut:
$$
\left[
\begin{array}{ccccc|c}
1 & 1 & 1 & 1 & 1 & 15 \\
0 & 1 & 0 & 0 & 0 & 2 \\
0 & 0 & 2 & 1 & 1 & 15 \\
0 & 0 & 1 & 2 & 1 & 16 \\
0 & 0 & 0 & 1 & 2 & 14
\end{array}
\right]
$$

---

#### **Langkah C: Eliminasi Elemen Kolom Ketiga di Bawah Diagonal Utama**
Baris ketiga ($R_3$) direncanakan sebagai baris pivot. Namun, nilai elemen $a_{33}$ adalah $2$, sedangkan elemen di bawahnya ($a_{43}$) pada baris keempat bernilai $1$. Untuk menghindari perhitungan pecahan pada operasi baris berikutnya, dilakukan **pertukaran baris** antara baris ketiga dan baris keempat.

* **Pertukaran Baris 3 dan Baris 4 ($R_3 \leftrightarrow R_4$):**
  Matriks setelah pertukaran baris:
  $$
  \left[
  \begin{array}{ccccc|c}
  1 & 1 & 1 & 1 & 1 & 15 \\
  0 & 1 & 0 & 0 & 0 & 2 \\
  0 & 0 & 1 & 2 & 1 & 16 \\
  0 & 0 & 2 & 1 & 1 & 15 \\
  0 & 0 & 0 & 1 & 2 & 14
  \end{array}
  \right]
  $$

* **Transformasi Baris Keempat ($R_4 \leftarrow R_4 - 2R_3$):**
  Gunakan baris ketiga baru sebagai pivot untuk menolkan elemen kolom ketiga pada baris keempat.
  $$
  \begin{aligned}
  R_4 &= [0, 0, 2, 1, 1 \mid 15] - 2 \times [0, 0, 1, 2, 1 \mid 16] \\
      &= [0-0, \; 0-0, \; 2-2, \; 1-4, \; 1-2 \mid 15-32] \\
      &= [0, 0, 0, -3, -1 \mid -17]
  \end{aligned}
  $$

Setelah transformasi kolom ketiga selesai, diperoleh matriks baru sebagai berikut:
$$
\left[
\begin{array}{ccccc|c}
1 & 1 & 1 & 1 & 1 & 15 \\
0 & 1 & 0 & 0 & 0 & 2 \\
0 & 0 & 1 & 2 & 1 & 16 \\
0 & 0 & 0 & -3 & -1 & -17 \\
0 & 0 & 0 & 1 & 2 & 14
\end{array}
\right]
$$

---

#### **Langkah D: Eliminasi Elemen Kolom Keempat di Bawah Diagonal Utama**
Baris keempat ($R_4$) direncanakan sebagai baris pivot. Namun, nilai elemen $a_{44}$ adalah $-3$, sedangkan elemen di bawahnya ($a_{54}$) pada baris kelima bernilai $1$. Untuk menghindari perhitungan pecahan pada operasi baris berikutnya, dilakukan **pertukaran baris** antara baris keempat dan baris kelima.

* **Pertukaran Baris 4 dan Baris 5 ($R_4 \leftrightarrow R_5$):**
  Matriks setelah pertukaran baris:
  $$
  \left[
  \begin{array}{ccccc|c}
  1 & 1 & 1 & 1 & 1 & 15 \\
  0 & 1 & 0 & 0 & 0 & 2 \\
  0 & 0 & 1 & 2 & 1 & 16 \\
  0 & 0 & 0 & 1 & 2 & 14 \\
  0 & 0 & 0 & -3 & -1 & -17
  \end{array}
  \right]
  $$

* **Transformasi Baris Kelima ($R_5 \leftarrow R_5 + 3R_4$):**
  Gunakan baris keempat baru sebagai pivot untuk menolkan elemen kolom keempat pada baris kelima.
  $$
  \begin{aligned}
  R_5 &= [0, 0, 0, -3, -1 \mid -17] + 3 \times [0, 0, 0, 1, 2 \mid 14] \\
      &= [0, \; 0, \; 0, \; -3+3, \; -1+6 \mid -17+42] \\
      &= [0, 0, 0, 0, 5 \mid 25]
  \end{aligned}
  $$

Setelah transformasi kolom keempat selesai, diperoleh matriks eselon baris akhir:
$$
\left[
\begin{array}{ccccc|c}
1 & 1 & 1 & 1 & 1 & 15 \\
0 & 1 & 0 & 0 & 0 & 2 \\
0 & 0 & 1 & 2 & 1 & 16 \\
0 & 0 & 0 & 1 & 2 & 14 \\
0 & 0 & 0 & 0 & 5 & 25
\end{array}
\right]
$$

---

### 4. Substitusi Balik (Back Substitution)

Matriks eselon baris yang diperoleh diterjemahkan kembali menjadi sistem persamaan linear baru:

$$
\begin{cases}
x_1 + x_2 + x_3 + x_4 + x_5 = 15 \quad &\text{(Persamaan 1)} \\
x_2 = 2 \quad &\text{(Persamaan 2)} \\
x_3 + 2x_4 + x_5 = 16 \quad &\text{(Persamaan 3)} \\
x_4 + 2x_5 = 14 \quad &\text{(Persamaan 4)} \\
5x_5 = 25 \quad &\text{(Persamaan 5)}
\end{cases}
$$

Nilai variabel dihitung secara bertahap dari persamaan terbawah menuju teratas:

1. **Menentukan nilai $x_5$ (dari Persamaan 5):**
   $$5x_5 = 25 \implies x_5 = \frac{25}{5} \implies x_5 = 5$$

2. **Menentukan nilai $x_4$ (dari Persamaan 4):**
   Substitusikan nilai $x_5 = 5$ ke dalam Persamaan 4:
   $$
   \begin{aligned}
   x_4 + 2(5) &= 14 \\
   x_4 + 10 &= 14 \\
   x_4 &= 14 - 10 \\
   x_4 &= 4
   \end{aligned}
   $$

3. **Menentukan nilai $x_3$ (dari Persamaan 3):**
   Substitusikan nilai $x_4 = 4$ dan $x_5 = 5$ ke dalam Persamaan 3:
   $$
   \begin{aligned}
   x_3 + 2(4) + 5 &= 16 \\
   x_3 + 8 + 5 &= 16 \\
   x_3 + 13 &= 16 \\
   x_3 &= 16 - 13 \\
   x_3 &= 3
   \end{aligned}
   $$

4. **Menentukan nilai $x_2$ (dari Persamaan 2):**
   Nilai $x_2$ secara langsung diperoleh dari Persamaan 2:
   $$x_2 = 2$$

5. **Menentukan nilai $x_1$ (dari Persamaan 1):**
   Substitusikan nilai $x_2 = 2$, $x_3 = 3$, $x_4 = 4$, dan $x_5 = 5$ ke dalam Persamaan 1:
   $$
   \begin{aligned}
   x_1 + 2 + 3 + 4 + 5 &= 15 \\
   x_1 + 14 &= 15 \\
   x_1 &= 15 - 14 \\
   x_1 &= 1
   \end{aligned}
   $$

---

### 5. Kesimpulan

Dengan menerapkan metode Eliminasi Gauss, diperoleh himpunan penyelesaian untuk sistem persamaan linear tersebut sebagai berikut:
$$\mathbf{x_1 = 1, \; x_2 = 2, \; x_3 = 3, \; x_4 = 4, \; x_5 = 5}$$