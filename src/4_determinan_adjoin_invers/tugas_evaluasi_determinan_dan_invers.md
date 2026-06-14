---
title: Tugas Evaluasi Determinan dan Invers
---

## Soal Latihan

### Bagian A: Hitunglah determinan matriks berikut menggunakan metode ekspansi baris:

$$
\det(A) = \sum_{k=1}^n (-1)^{i+k} a_{ik} M_{ik}
$$

Di mana $M_{ij}$ adalah minor dari matriks $A$, yaitu:

$$
M_{ij} = \det(A_{ij})
$$

dan $A_{ij}$ adalah submatriks yang diperoleh dengan menghapus baris ke-$i$ dan kolom ke-$j$ dari matriks $A$ berordo $n \times n$.

1. $$A = \begin{bmatrix} -7 & -5 \\ 1 & 4 \end{bmatrix}$$
2. $$A = \begin{bmatrix} 0 & 2 & -3 \\ 1 & -2 & -1 \\ 0 & 0 & 1 \end{bmatrix}$$
3. $$A = \begin{bmatrix} 1 & -3 & 1 & 1 \\ -3 & 1 & 1 & 1 \\ 1 & 1 & -3 & 1 \\ 1 & 1 & 1 & -3 \end{bmatrix}$$

---

### Bagian B: Gunakan rumus matriks adjoin untuk menghitung invers dari matriks berikut:

Rumus elemen adjoin:

$$(\operatorname{adj} A)_{ij} = (-1)^{i+j} M_{ji}$$

Rumus invers matriks:

$$A^{-1} = \frac{1}{\det(A)} \operatorname{adj}(A)$$

4. $$A = \begin{bmatrix} -7 & -5 \\ 1 & 4 \end{bmatrix}$$
5. $$A = \begin{bmatrix} 0 & 2 & -3 \\ 1 & -2 & -1 \\ 0 & 0 & 1 \end{bmatrix}$$
6. $$A = \begin{bmatrix} 1 & -3 & 1 & 1 \\ -3 & 1 & 1 & 1 \\ 1 & 1 & -3 & 1 \\ 1 & 1 & 1 & -3 \end{bmatrix}$$

---

## Solusi Lengkap dan Pembahasan

### **1. Penyelesaian Soal 1 (Determinan Ordo 2 × 2)**

Diberikan matriks:
$$A = \begin{bmatrix} -7 & -5 \\ 1 & 4 \end{bmatrix}$$

#### **Penjelasan Proses:**
Determinan matriks berordo $2 \times 2$ dihitung menggunakan aturan perkalian silang diagonal utama dikurangi diagonal samping:
$$\det(A) = ad - bc$$

#### **Perhitungan Aritmatika:**
* Perkalian Diagonal Utama ($ad$): $-7 \times 4 = -28$
* Perkalian Diagonal Samping ($bc$): $-5 \times 1 = -5$
* Pengurangan:
  $$\det(A) = (-28) - (-5) = -28 + 5 = -23$$

**Jawaban:** Determinan matriks $A$ adalah **$-23$**.

---

### **2. Penyelesaian Soal 2 (Determinan Ordo 3 × 3)**

Diberikan matriks:
$$A = \begin{bmatrix} 0 & 2 & -3 \\ 1 & -2 & -1 \\ 0 & 0 & 1 \end{bmatrix}$$

#### **Penjelasan Proses:**
Untuk meminimalkan jumlah perhitungan, ekspansi kofaktor dilakukan di sepanjang **baris ke-3** karena baris tersebut memiliki elemen nol terbanyak ($a_{31} = 0$, $a_{32} = 0$, $a_{33} = 1$). 

Formula ekspansi baris ke-3 adalah:
$$\det(A) = (-1)^{3+1} a_{31} M_{31} + (-1)^{3+2} a_{32} M_{32} + (-1)^{3+3} a_{33} M_{33}$$

#### **Perhitungan Langkah demi Langkah:**

1. **Suku Pertama ($a_{31}$):**
   Karena elemen $a_{31} = 0$, perkaliannya dengan nilai minor $M_{31}$ menghasilkan nol.
   $$\text{Suku 1} = (+1) \cdot 0 \cdot M_{31} = 0$$

2. **Suku Kedua ($a_{32}$):**
   Karena elemen $a_{32} = 0$, perkaliannya dengan nilai minor $M_{32}$ menghasilkan nol.
   $$\text{Suku 2} = (-1) \cdot 0 \cdot M_{32} = 0$$

3. **Suku Ketiga ($a_{33}$):**
   Elemen $a_{33} = 1$ bertanda positif karena $(-1)^{3+3} = +1$.
   Minor $M_{33}$ diperoleh dengan menghapus baris ke-3 dan kolom ke-3 dari matriks $A$:
   $$M_{33} = \det \begin{bmatrix} 0 & 2 \\ 1 & -2 \end{bmatrix}$$
   Hitung determinan matriks $2 \times 2$ ini:
   $$M_{33} = (0 \times -2) - (2 \times 1) = 0 - 2 = -2$$
   $$\text{Suku 3} = (+1) \cdot 1 \cdot (-2) = -2$$

4. **Penjumlahan Total Suku:**
   $$\det(A) = 0 + 0 + (-2) = -2$$

**Jawaban:** Determinan matriks $A$ adalah **$-2$**.

---

### **3. Penyelesaian Soal 3 (Determinan Ordo 4 × 4)**

Diberikan matriks:
$$A = \begin{bmatrix} 1 & -3 & 1 & 1 \\ -3 & 1 & 1 & 1 \\ 1 & 1 & -3 & 1 \\ 1 & 1 & 1 & -3 \end{bmatrix}$$

#### **Penjelasan Proses:**
Ekpansi kofaktor dilakukan di sepanjang **baris ke-1**.
Formula determinal matriks $4 \times 4$ sepanjang baris ke-1 adalah:
$$\det(A) = a_{11} C_{11} + a_{12} C_{12} + a_{13} C_{13} + a_{14} C_{14}$$
Di mana $C_{1j} = (-1)^{1+j} M_{1j}$.

#### **Perhitungan Minor Matriks 3 × 3:**

##### **1. Minor $M_{11}$ (Hapus Baris 1, Kolom 1):**
$$M_{11} = \det \begin{bmatrix} 1 & 1 & 1 \\ 1 & -3 & 1 \\ 1 & 1 & -3 \end{bmatrix}$$
Hitung menggunakan ekspansi baris ke-1 dari submatriks tersebut:
$$
\begin{aligned}
M_{11} &= 1 \cdot \det\begin{bmatrix} -3 & 1 \\ 1 & -3 \end{bmatrix} - 1 \cdot \det\begin{bmatrix} 1 & 1 \\ 1 & -3 \end{bmatrix} + 1 \cdot \det\begin{bmatrix} 1 & -3 \\ 1 & 1 \end{bmatrix} \\
       &= 1 \cdot (9 - 1) - 1 \cdot (-3 - 1) + 1 \cdot (1 - (-3)) \\
       &= 8 - (-4) + 4 = 8 + 4 + 4 = 16
\end{aligned}
$$
* **Suku ke-1 Utama:** $a_{11} C_{11} = (1) \cdot (-1)^{1+1} \cdot M_{11} = 1 \cdot (+1) \cdot 16 = \mathbf{16}$

##### **2. Minor $M_{12}$ (Hapus Baris 1, Kolom 2):**
$$M_{12} = \det \begin{bmatrix} -3 & 1 & 1 \\ 1 & -3 & 1 \\ 1 & 1 & -3 \end{bmatrix}$$
Hitung menggunakan ekspansi baris ke-1:
$$
\begin{aligned}
M_{12} &= -3 \cdot \det\begin{bmatrix} -3 & 1 \\ 1 & -3 \end{bmatrix} - 1 \cdot \det\begin{bmatrix} 1 & 1 \\ 1 & -3 \end{bmatrix} + 1 \cdot \det\begin{bmatrix} 1 & -3 \\ 1 & 1 \end{bmatrix} \\
       &= -3 \cdot (9 - 1) - 1 \cdot (-3 - 1) + 1 \cdot (1 - (-3)) \\
       &= -3 \cdot (8) - 1 \cdot (-4) + 1 \cdot (4) = -24 + 4 + 4 = -16
\end{aligned}
$$
* **Suku ke-2 Utama:** $a_{12} C_{12} = (-3) \cdot (-1)^{1+2} \cdot M_{12} = (-3) \cdot (-1) \cdot (-16) = \mathbf{-48}$

##### **3. Minor $M_{13}$ (Hapus Baris 1, Kolom 3):**
$$M_{13} = \det \begin{bmatrix} -3 & 1 & 1 \\ 1 & 1 & 1 \\ 1 & 1 & -3 \end{bmatrix}$$
Hitung menggunakan ekspansi baris ke-1:
$$
\begin{aligned}
M_{13} &= -3 \cdot \det\begin{bmatrix} 1 & 1 \\ 1 & -3 \end{bmatrix} - 1 \cdot \det\begin{bmatrix} 1 & 1 \\ 1 & -3 \end{bmatrix} + 1 \cdot \det\begin{bmatrix} 1 & 1 \\ 1 & 1 \end{bmatrix} \\
       &= -3 \cdot (-3 - 1) - 1 \cdot (-3 - 1) + 1 \cdot (1 - 1) \\
       &= -3 \cdot (-4) - 1 \cdot (-4) + 0 = 12 + 4 = 16
\end{aligned}
$$
* **Suku ke-3 Utama:** $a_{13} C_{13} = (1) \cdot (-1)^{1+3} \cdot M_{13} = 1 \cdot (+1) \cdot 16 = \mathbf{16}$

##### **4. Minor $M_{14}$ (Hapus Baris 1, Kolom 4):**
$$M_{14} = \det \begin{bmatrix} -3 & 1 & 1 \\ 1 & 1 & -3 \\ 1 & 1 & 1 \end{bmatrix}$$
Hitung menggunakan ekspansi baris ke-1:
$$
\begin{aligned}
M_{14} &= -3 \cdot \det\begin{bmatrix} 1 & -3 \\ 1 & 1 \end{bmatrix} - 1 \cdot \det\begin{bmatrix} 1 & -3 \\ 1 & 1 \end{bmatrix} + 1 \cdot \det\begin{bmatrix} 1 & 1 \\ 1 & 1 \end{bmatrix} \\
       &= -3 \cdot (1 - (-3)) - 1 \cdot (1 - (-3)) + 1 \cdot (1 - 1) \\
       &= -3 \cdot (4) - 1 \cdot (4) + 0 = -12 - 4 = -16
\end{aligned}
$$
* **Suku ke-4 Utama:** $a_{14} C_{14} = (1) \cdot (-1)^{1+4} \cdot M_{14} = 1 \cdot (-1) \cdot (-16) = \mathbf{16}$

#### **Penjumlahan Total Suku:**
$$\det(A) = 16 + (-48) + 16 + 16 = 0$$

**Jawaban:** Determinan matriks $A$ adalah **$0$**.

---

### **4. Penyelesaian Soal 4 (Invers Ordo 2 × 2)**

Diberikan matriks:
$$A = \begin{bmatrix} -7 & -5 \\ 1 & 4 \end{bmatrix}$$

#### **Langkah 1: Menghitung Determinan ($\det A$)**
Dari perhitungan di Soal 1, kita ketahui determinannya adalah:
$$\det(A) = -23$$

#### **Langkah 2: Menentukan Kofaktor dan Membuat Matriks Adjoin**
Matriks kofaktor $C$ diperoleh dengan menghitung kofaktor setiap elemen:
* $C_{11} = (-1)^{1+1} \cdot \det[4] = 4$
* $C_{12} = (-1)^{1+2} \cdot \det[1] = -1$
* $C_{21} = (-1)^{2+1} \cdot \det[-5] = 5$
* $C_{22} = (-1)^{2+2} \cdot \det[-7] = -7$

Susun elemen kofaktor menjadi matriks kofaktor $C$:
$$C = \begin{bmatrix} 4 & -1 \\ 5 & -7 \end{bmatrix}$$
Lakukan transpose terhadap $C$ untuk memperoleh matriks adjoin ($\operatorname{adj} A = C^T$):
$$\operatorname{adj}(A) = \begin{bmatrix} 4 & 5 \\ -1 & -7 \end{bmatrix}$$

#### **Langkah 3: Menghitung Invers Matriks ($A^{-1}$)**
Kalikan skalar $\frac{1}{\det(A)}$ dengan matriks adjoin:
$$
A^{-1} = \frac{1}{-23} \begin{bmatrix} 4 & 5 \\ -1 & -7 \end{bmatrix} = \begin{bmatrix} -\frac{4}{23} & -\frac{5}{23} \\ \frac{1}{23} & \frac{7}{23} \end{bmatrix}
$$

**Jawaban:** Invers matriks $A$ adalah **$\begin{bmatrix} -4/23 & -5/23 \\ 1/23 & 7/23 \end{bmatrix}$**.

---

### **5. Penyelesaian Soal 5 (Invers Ordo 3 × 3)**

Diberikan matriks:
$$A = \begin{bmatrix} 0 & 2 & -3 \\ 1 & -2 & -1 \\ 0 & 0 & 1 \end{bmatrix}$$

#### **Langkah 1: Menghitung Determinan ($\det A$)**
Dari perhitungan di Soal 2, kita ketahui determinannya adalah:
$$\det(A) = -2$$

#### **Langkah 2: Menghitung Matriks Kofaktor $C$ (Sembilan Elemen)**
Hitung masing-masing kofaktor $C_{ij} = (-1)^{i+j} M_{ij}$:

* **$C_{11}$**: Hapus baris 1, kolom 1:
  $$C_{11} = (-1)^{1+1} \det \begin{bmatrix} -2 & -1 \\ 0 & 1 \end{bmatrix} = +1 \cdot ((-2 \times 1) - (-1 \times 0)) = -2$$
* **$C_{12}$**: Hapus baris 1, kolom 2:
  $$C_{12} = (-1)^{1+2} \det \begin{bmatrix} 1 & -1 \\ 0 & 1 \end{bmatrix} = -1 \cdot ((1 \times 1) - (-1 \times 0)) = -1$$
* **$C_{13}$**: Hapus baris 1, kolom 3:
  $$C_{13} = (-1)^{1+3} \det \begin{bmatrix} 1 & -2 \\ 0 & 0 \end{bmatrix} = +1 \cdot ((1 \times 0) - (-2 \times 0)) = 0$$
* **$C_{21}$**: Hapus baris 2, kolom 1:
  $$C_{21} = (-1)^{2+1} \det \begin{bmatrix} 2 & -3 \\ 0 & 1 \end{bmatrix} = -1 \cdot ((2 \times 1) - (-3 \times 0)) = -2$$
* **$C_{22}$**: Hapus baris 2, kolom 2:
  $$C_{22} = (-1)^{2+2} \det \begin{bmatrix} 0 & -3 \\ 0 & 1 \end{bmatrix} = +1 \cdot ((0 \times 1) - (-3 \times 0)) = 0$$
* **$C_{23}$**: Hapus baris 2, kolom 3:
  $$C_{23} = (-1)^{2+3} \det \begin{bmatrix} 0 & 2 \\ 0 & 0 \end{bmatrix} = -1 \cdot ((0 \times 0) - (2 \times 0)) = 0$$
* **$C_{31}$**: Hapus baris 3, kolom 1:
  $$C_{31} = (-1)^{3+1} \det \begin{bmatrix} 2 & -3 \\ -2 & -1 \end{bmatrix} = +1 \cdot ((2 \times -1) - (-3 \times -2)) = -2 - 6 = -8$$
* **$C_{32}$**: Hapus baris 3, kolom 2:
  $$C_{32} = (-1)^{3+2} \det \begin{bmatrix} 0 & -3 \\ 1 & -1 \end{bmatrix} = -1 \cdot ((0 \times -1) - (-3 \times 1)) = -(0 + 3) = -3$$
* **$C_{33}$**: Hapus baris 3, kolom 3:
  $$C_{33} = (-1)^{3+3} \det \begin{bmatrix} 0 & 2 \\ 1 & -2 \end{bmatrix} = +1 \cdot ((0 \times -2) - (2 \times 1)) = -2$$

Susun hasil kofaktor ke matriks kofaktor $C$:
$$C = \begin{bmatrix} -2 & -1 & 0 \\ -2 & 0 & 0 \\ -8 & -3 & -2 \end{bmatrix}$$

#### **Langkah 3: Membentuk Matriks Adjoin ($\operatorname{adj} A$)**
Transpose matriks kofaktor $C$ (tukar baris menjadi kolom):
$$\operatorname{adj}(A) = C^T = \begin{bmatrix} -2 & -2 & -8 \\ -1 & 0 & -3 \\ 0 & 0 & -2 \end{bmatrix}$$

#### **Langkah 4: Menghitung Invers Matriks ($A^{-1}$)**
Kalikan skalar pengali $\frac{1}{\det(A)} = \frac{1}{-2}$ ke setiap elemen matriks adjoin:
$$
\begin{aligned}
A^{-1} &= \frac{1}{-2} \begin{bmatrix} -2 & -2 & -8 \\ -1 & 0 & -3 \\ 0 & 0 & -2 \end{bmatrix} \\
       &= \begin{bmatrix} \frac{-2}{-2} & \frac{-2}{-2} & \frac{-8}{-2} \\ \frac{-1}{-2} & \frac{0}{-2} & \frac{-3}{-2} \\ \frac{0}{-2} & \frac{0}{-2} & \frac{-2}{-2} \end{bmatrix} \\
       &= \begin{bmatrix} 1 & 1 & 4 \\ \frac{1}{2} & 0 & \frac{3}{2} \\ 0 & 0 & 1 \end{bmatrix}
\end{aligned}
$$

**Jawaban:** Invers matriks $A$ adalah **$\begin{bmatrix} 1 & 1 & 4 \\ 1/2 & 0 & 3/2 \\ 0 & 0 & 1 \end{bmatrix}$**.

---

### **6. Penyelesaian Soal 6 (Invers Ordo 4 × 4)**

Diberikan matriks:
$$A = \begin{bmatrix} 1 & -3 & 1 & 1 \\ -3 & 1 & 1 & 1 \\ 1 & 1 & -3 & 1 \\ 1 & 1 & 1 & -3 \end{bmatrix}$$

#### **Penjelasan Proses & Hasil:**
* Dari perhitungan determinan pada **Soal 3**, nilai determinan matriks $A$ adalah **$0$** ($\det(A) = 0$).
* Sesuai dengan teorema keujudan invers, sebuah matriks persegi hanya memiliki invers jika nilainya non-singular ($\det \neq 0$).
* Karena determinan bernilai nol, operasi pembagian dengan nilai determinan pada rumus invers $\left(A^{-1} = \frac{1}{\det A} \operatorname{adj} A\right)$ tidak terdefinisi (pembagian dengan nol).

**Jawaban:** Matriks $A$ tidak memiliki invers (**singular**).