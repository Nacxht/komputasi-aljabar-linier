---
title: Tugas Adjoin
---

## Adjoin Matriks, Determinan, dan Invers Matriks Ordo 5 × 5

Dokumen ini memaparkan formulasi teoritis untuk menghitung determinan, matriks adjoin, dan invers dari matriks persegi berordo $5 \times 5$ secara lengkap dan terstruktur.

Misalkan diberikan matriks persegi $A$ berordo $5 \times 5$:

$$
A = \begin{bmatrix}
a & b & c & d & e \\
f & g & h & i & j \\
k & l & m & n & o \\
p & q & r & s & t \\
u & v & w & x & y
\end{bmatrix}
$$

---

## 1. Determinan Matriks Ordo 5 × 5 ($\det A$)

Determinan dari matriks berordo $5 \times 5$ dihitung menggunakan metode ekspansi kofaktor sepanjang baris pertama:

$$
\det(A) = aC_{11} + bC_{12} + cC_{13} + dC_{14} + eC_{15}
$$

> [!NOTE]
> Nilai tanda positif/negatif pada setiap suku sudah secara otomatis terintegrasi di dalam masing-masing nilai kofaktor $C_{ij}$ melalui faktor pengali $(-1)^{i+j}$.

---

## 2. Definisi Kofaktor dan Minor

Kofaktor didefinisikan secara formal sebagai berikut:

$$
C_{ij} = (-1)^{i+j} \cdot M_{ij}
$$

Keterangan parameter:
* $C_{ij}$: Kofaktor dari elemen pada baris ke-$i$ dan kolom ke-$j$.
* $M_{ij}$: Minor, yaitu determinan dari submatriks berordo $4 \times 4$ yang diperoleh setelah menghapus baris ke-$i$ dan kolom ke-$j$ dari matriks asal $A$.
* $(-1)^{i+j}$: Tanda penentu (positif atau negatif) berdasarkan posisi indeks baris $i$ dan kolom $j$.

---

## 3. Proses Pembentukan Kofaktor Baris Pertama

Berikut adalah penjelasan dan pembentukan submatriks kofaktor secara rinci untuk seluruh elemen pada baris pertama ($C_{11}$ hingga $C_{15}$):

### **Kofaktor $C_{11}$ (Untuk Elemen $a$)**

**Operasi Penghapusan:** Hapus Baris ke-1 dan Kolom ke-1.

**Tanda Posisi:** $(-1)^{1+1} = (-1)^2 = +1$.

**Formulasi:**

$$
C_{11} = (+1) \times
\begin{vmatrix}
g & h & i & j \\
l & m & n & o \\
q & r & s & t \\
v & w & x & y
\end{vmatrix}
$$

---

### **Kofaktor $C_{12}$ (Untuk Elemen $b$)**

**Operasi Penghapusan:** Hapus Baris ke-1 dan Kolom ke-2 (elemen pada kolom ke-2 yaitu $g, l, q, v$ dihilangkan).

**Tanda Posisi:** $(-1)^{1+2} = (-1)^3 = -1$.

**Formulasi:**

$$
C_{12} = (-1) \times
\begin{vmatrix}
f & h & i & j \\
k & m & n & o \\
p & r & s & t \\
u & w & x & y
\end{vmatrix}
$$

---

### **Kofaktor $C_{13}$ (Untuk Elemen $c$)**

**Operasi Penghapusan:** Hapus Baris ke-1 dan Kolom ke-3 (elemen pada kolom ke-3 yaitu $h, m, r, w$ dihilangkan).

**Tanda Posisi:** $(-1)^{1+3} = (-1)^4 = +1$.

**Formulasi:**

$$
C_{13} = (+1) \times
\begin{vmatrix}
f & g & i & j \\
k & l & n & o \\
p & q & s & t \\
u & v & x & y
\end{vmatrix}
$$

---

### **Kofaktor $C_{14}$ (Untuk Elemen $d$)**

**Operasi Penghapusan:** Hapus Baris ke-1 dan Kolom ke-4 (elemen pada kolom ke-4 yaitu $i, n, s, x$ dihilangkan).

**Tanda Posisi:** $(-1)^{1+4} = (-1)^5 = -1$.

**Formulasi:**

$$
C_{14} = (-1) \times
\begin{vmatrix}
f & g & h & j \\
k & l & m & o \\
p & q & r & t \\
u & v & w & y
\end{vmatrix}
$$

---

### **Kofaktor $C_{15}$ (Untuk Elemen $e$)**

**Operasi Penghapusan:** Hapus Baris ke-1 dan Kolom ke-5 (elemen pada kolom ke-5 yaitu $j, o, t, y$ dihilangkan).

**Tanda Posisi:** $(-1)^{1+5} = (-1)^6 = +1$.

**Formulasi:**

$$
C_{15} = (+1) \times
\begin{vmatrix}
f & g & h & i \\
k & l & m & n \\
p & q & r & s \\
u & v & w & x
\end{vmatrix}
$$

---

## 4. Matriks Adjoin ($\operatorname{adj} A$)

Matriks adjoin ($\operatorname{adj} A$) diperoleh dengan melakukan operasi transpose pada matriks kofaktor $C$. Secara konsep, proses pembentukan adjoin untuk ordo $5 \times 5$ ini melibatkan tahapan berikut:

### **Penyusunan Matriks Kofaktor $C$**
Pertama-tama, hitung nilai kofaktor untuk seluruh $25$ elemen dari matriks asal $A$ ($C_{11}$ sampai $C_{55}$). Tempatkan setiap hasil perhitungan tersebut ke posisi baris dan kolom yang bersesuaian untuk membentuk matriks kofaktor $C$ berordo $5 \times 5$:

$$
C = \begin{bmatrix}
C_{11} & C_{12} & C_{13} & C_{14} & C_{15} \\
C_{21} & C_{22} & C_{23} & C_{24} & C_{25} \\
C_{31} & C_{32} & C_{33} & C_{34} & C_{35} \\
C_{41} & C_{42} & C_{43} & C_{44} & C_{45} \\
C_{51} & C_{52} & C_{53} & C_{54} & C_{55}
\end{bmatrix}
$$

### **Operasi Transpose untuk Mendapatkan Adjoin**
Transpose matriks kofaktor $C$ (ditulis sebagai $C^T$) dilakukan dengan cara menukar susunan baris menjadi kolom. Secara spesifik:
* Elemen-elemen **Baris 1** dari $C$ ($[C_{11}, C_{12}, C_{13}, C_{14}, C_{15}]$) diposisikan menjadi **Kolom 1** pada matriks adjoin.
* Elemen-elemen **Baris 2** dari $C$ ($[C_{21}, C_{22}, C_{23}, C_{24}, C_{25}]$) diposisikan menjadi **Kolom 2** pada matriks adjoin.
* Elemen-elemen **Baris 3** dari $C$ ($[C_{31}, C_{32}, C_{33}, C_{34}, C_{35}]$) diposisikan menjadi **Kolom 3** pada matriks adjoin.
* Elemen-elemen **Baris 4** dari $C$ ($[C_{41}, C_{42}, C_{43}, C_{44}, C_{45}]$) diposisikan menjadi **Kolom 4** pada matriks adjoin.
* Elemen-elemen **Baris 5** dari $C$ ($[C_{51}, C_{52}, C_{53}, C_{54}, C_{55}]$) diposisikan menjadi **Kolom 5** pada matriks adjoin.

Sehingga, struktur matriks Adjoin $\operatorname{adj}(A)$ adalah:

$$
\operatorname{adj}(A) = C^T = \begin{bmatrix}
C_{11} & C_{21} & C_{31} & C_{41} & C_{51} \\
C_{12} & C_{22} & C_{32} & C_{42} & C_{52} \\
C_{13} & C_{23} & C_{33} & C_{43} & C_{53} \\
C_{14} & C_{24} & C_{34} & C_{44} & C_{54} \\
C_{15} & C_{25} & C_{35} & C_{45} & C_{55}
\end{bmatrix}
$$

---

## 5. Invers Matriks Ordo 5 × 5 ($A^{-1}$)

Setelah nilai determinan $\det(A)$ dan matriks adjoin $\operatorname{adj}(A)$ diperoleh, langkah terakhir adalah menghitung invers matriks $A^{-1}$.

### **Operasi Perkalian Skalar**
Invers matriks diperoleh dengan cara mengalikan konstanta skalar $\frac{1}{\det(A)}$ ke setiap elemen dari matriks adjoin $\operatorname{adj}(A)$ secara individual:

$$
A^{-1} = \frac{1}{\det(A)} \cdot \operatorname{adj}(A)
$$

Secara rinci, setiap elemen matriks adjoin dibagi dengan nilai determinan matriks $A$:

$$
A^{-1} = \begin{bmatrix}
\frac{C_{11}}{\det(A)} & \frac{C_{21}}{\det(A)} & \frac{C_{31}}{\det(A)} & \frac{C_{41}}{\det(A)} & \frac{C_{51}}{\det(A)} \\
\frac{C_{12}}{\det(A)} & \frac{C_{22}}{\det(A)} & \frac{C_{32}}{\det(A)} & \frac{C_{42}}{\det(A)} & \frac{C_{52}}{\det(A)} \\
\frac{C_{13}}{\det(A)} & \frac{C_{23}}{\det(A)} & \frac{C_{33}}{\det(A)} & \frac{C_{43}}{\det(A)} & \frac{C_{53}}{\det(A)} \\
\frac{C_{14}}{\det(A)} & \frac{C_{24}}{\det(A)} & \frac{C_{34}}{\det(A)} & \frac{C_{44}}{\det(A)} & \frac{C_{54}}{\det(A)} \\
\frac{C_{15}}{\det(A)} & \frac{C_{25}}{\det(A)} & \frac{C_{35}}{\det(A)} & \frac{C_{45}}{\det(A)} & \frac{C_{55}}{\det(A)}
\end{bmatrix}
$$

> [!IMPORTANT]
> Operasi pembagian ini hanya dapat didefinisikan apabila matriks bersifat non-singular, yaitu $\det(A) \neq 0$. Jika nilai determinan bernilai nol, pembagian skalar ini tidak dapat dilakukan sehingga matriks tersebut tidak memiliki invers.
