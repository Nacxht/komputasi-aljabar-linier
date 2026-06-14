---
title: Tugas 4 - SPL 4 Variabel
---

## Penyelesaian Sistem Persamaan Linear 4 Variabel dengan Eliminasi Gauss

Dokumen ini menyajikan langkah-langkah penyelesaian Sistem Persamaan Linear (SPL) yang terdiri dari 4 variabel dan 4 persamaan menggunakan metode **Eliminasi Gauss**. Solusi akhir dari sistem persamaan ini adalah: 
$$x_1 = 1,\; x_2 = 2,\; x_3 = 3,\; x_4 = 4$$

---

### 1. Sistem Persamaan Linear

Sistem persamaan linear yang akan diselesaikan didefinisikan sebagai berikut:

$$
\begin{aligned}
x_1 + x_2 + x_3 + x_4 &= 10 \quad &\text{(Persamaan I)} \\
2x_1 + 3x_2 + x_3 + x_4 &= 15 \quad &\text{(Persamaan II)} \\
x_1 + 2x_2 + 3x_3 + x_4 &= 18 \quad &\text{(Persamaan III)} \\
x_1 + x_2 + x_3 + 2x_4 &= 14 \quad &\text{(Persamaan IV)}
\end{aligned}
$$

---

### 2. Representasi Matriks Diperbesar (Augmented Matrix)

Langkah awal penyelesaian dilakukan dengan menyusun koefisien variabel beserta konstanta hasil ke dalam bentuk matriks diperbesar (*augmented matrix*). Representasi ini bertujuan untuk mempermudah manipulasi aljabar selama proses eliminasi:

$$
\left[
\begin{array}{cccc|c}
1 & 1 & 1 & 1 & 10 \\
2 & 3 & 1 & 1 & 15 \\
1 & 2 & 3 & 1 & 18 \\
1 & 1 & 1 & 2 & 14
\end{array}
\right]
$$

---

### 3. Proses Operasi Baris Elementer (OBE)

Tujuan utama dari Operasi Baris Elementer (OBE) pada Eliminasi Gauss adalah mentransformasikan matriks diperbesar menjadi bentuk **Eselon Baris (Segitiga Atas)**. Bentuk ini ditandai dengan semua elemen di bawah diagonal utama bernilai nol ($0$).

#### **Langkah A: Eliminasi Elemen Kolom Pertama di Bawah Diagonal Utama**
Baris pertama ($R_1$) digunakan sebagai baris acuan atau baris pivot. Elemen utama baris pertama ($a_{11} = 1$) digunakan untuk menolkan elemen pada kolom pertama untuk baris $R_2$, $R_3$, dan $R_4$.

* **Transformasi Baris Kedua ($R_2 \leftarrow R_2 - 2R_1$):**
  Untuk menghasilkan nilai $0$ pada elemen baris kedua kolom pertama, dilakukan pengurangan elemen-elemen baris kedua dengan dua kali elemen baris pertama yang bersesuaian.
  $$
  \begin{aligned}
  R_2 &= [2, 3, 1, 1 \mid 15] - 2 \times [1, 1, 1, 1 \mid 10] \\
      &= [2-2, \; 3-2, \; 1-2, \; 1-2 \mid 15-20] \\
      &= [0, 1, -1, -1 \mid -5]
  \end{aligned}
  $$

* **Transformasi Baris Ketiga ($R_3 \leftarrow R_3 - R_1$):**
  Untuk menghasilkan nilai $0$ pada elemen baris ketiga kolom pertama, dilakukan pengurangan elemen-elemen baris ketiga langsung dengan elemen baris pertama yang bersesuaian.
  $$
  \begin{aligned}
  R_3 &= [1, 2, 3, 1 \mid 18] - [1, 1, 1, 1 \mid 10] \\
      &= [1-1, \; 2-1, \; 3-1, \; 1-1 \mid 18-10] \\
      &= [0, 1, 2, 0 \mid 8]
  \end{aligned}
  $$

* **Transformasi Baris Keempat ($R_4 \leftarrow R_4 - R_1$):**
  Untuk menghasilkan nilai $0$ pada elemen baris keempat kolom pertama, dilakukan pengurangan elemen-elemen baris keempat langsung dengan elemen baris pertama yang bersesuaian.
  $$
  \begin{aligned}
  R_4 &= [1, 1, 1, 2 \mid 14] - [1, 1, 1, 1 \mid 10] \\
      &= [1-1, \; 1-1, \; 1-1, \; 2-1 \mid 14-10] \\
      &= [0, 0, 0, 1 \mid 4]
  \end{aligned}
  $$

Setelah transformasi kolom pertama selesai, diperoleh matriks baru sebagai berikut:
$$
\left[
\begin{array}{cccc|c}
1 & 1 & 1 & 1 & 10 \\
0 & 1 & -1 & -1 & -5 \\
0 & 1 & 2 & 0 & 8 \\
0 & 0 & 0 & 1 & 4
\end{array}
\right]
$$

---

#### **Langkah B: Eliminasi Elemen Kolom Kedua di Bawah Diagonal Utama**
Baris kedua ($R_2$) digunakan sebagai baris pivot baru. Elemen pivot ($a_{22} = 1$) digunakan untuk menolkan elemen di bawahnya pada kolom kedua. 
*(Catatan: Kolom kedua pada baris keempat ($R_4$) sudah bernilai $0$, sehingga operasi OBE hanya diterapkan pada baris ketiga ($R_3$)).*

* **Transformasi Baris Ketiga ($R_3 \leftarrow R_3 - R_2$):**
  Untuk menghasilkan nilai $0$ pada kolom kedua baris ketiga, elemen baris ketiga dikurangi dengan elemen baris kedua yang bersesuaian.
  $$
  \begin{aligned}
  R_3 &= [0, 1, 2, 0 \mid 8] - [0, 1, -1, -1 \mid -5] \\
      &= [0-0, \; 1-1, \; 2-(-1), \; 0-(-1) \mid 8-(-5)] \\
      &= [0, 0, 3, 1 \mid 13]
  \end{aligned}
  $$

Setelah transformasi kolom kedua selesai, diperoleh matriks baru sebagai berikut:
$$
\left[
\begin{array}{cccc|c}
1 & 1 & 1 & 1 & 10 \\
0 & 1 & -1 & -1 & -5 \\
0 & 0 & 3 & 1 & 13 \\
0 & 0 & 0 & 1 & 4
\end{array}
\right]
$$

---

#### **Langkah C: Evaluasi Akhir Matriks Eselon Baris**
Berdasarkan hasil matriks terakhir, kolom ketiga pada baris keempat ($R_4$) sudah bernilai $0$. Karena seluruh elemen di bawah diagonal utama telah bernilai nol, matriks diperbesar tersebut telah memenuhi kriteria **Matriks Eselon Baris (Segitiga Atas)**. Dengan demikian, tahapan OBE dinyatakan selesai.

---

### 4. Substitusi Balik (Back Substitution)

Setelah bentuk eselon baris diperoleh, langkah berikutnya adalah menerjemahkan kembali matriks tersebut ke dalam sistem persamaan linear baru:

$$
\begin{cases}
x_1 + x_2 + x_3 + x_4 = 10 \quad &\text{(Persamaan 1)} \\
x_2 - x_3 - x_4 = -5 \quad &\text{(Persamaan 2)} \\
3x_3 + x_4 = 13 \quad &\text{(Persamaan 3)} \\
x_4 = 4 \quad &\text{(Persamaan 4)}
\end{cases}
$$

Penyelesaian nilai variabel dihitung secara berurutan dari persamaan terbawah menuju persamaan teratas:

1. **Menentukan nilai $x_4$ (dari Persamaan 4):**
   $$x_4 = 4$$

2. **Menentukan nilai $x_3$ (dari Persamaan 3):**
   Substitusikan nilai $x_4 = 4$ ke dalam Persamaan 3:
   $$
   \begin{aligned}
   3x_3 + 4 &= 13 \\
   3x_3 &= 13 - 4 \\
   3x_3 &= 9 \\
   x_3 &= \frac{9}{3} \\
   x_3 &= 3
   \end{aligned}
   $$

3. **Menentukan nilai $x_2$ (dari Persamaan 2):**
   Substitusikan nilai $x_3 = 3$ dan $x_4 = 4$ ke dalam Persamaan 2:
   $$
   \begin{aligned}
   x_2 - 3 - 4 &= -5 \\
   x_2 - 7 &= -5 \\
   x_2 &= -5 + 7 \\
   x_2 &= 2
   \end{aligned}
   $$

4. **Menentukan nilai $x_1$ (dari Persamaan 1):**
   Substitusikan nilai $x_2 = 2$, $x_3 = 3$, dan $x_4 = 4$ ke dalam Persamaan 1:
   $$
   \begin{aligned}
   x_1 + 2 + 3 + 4 &= 10 \\
   x_1 + 9 &= 10 \\
   x_1 &= 10 - 9 \\
   x_1 &= 1
   \end{aligned}
   $$

---

### 5. Kesimpulan

Dengan menerapkan metode Eliminasi Gauss, diperoleh himpunan penyelesaian untuk sistem persamaan linear tersebut sebagai berikut:
$$\mathbf{x_1 = 1, \; x_2 = 2, \; x_3 = 3, \; x_4 = 4}$$