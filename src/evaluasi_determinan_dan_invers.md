---
title: Evaluasi Determinan dan Invers
date: 2026-04-13
---

## Soal 1

$$
A =
\begin{bmatrix}
-7 & -5 \\
1 & 4
\end{bmatrix}
$$

### Jawaban

$$
det (\text{A}) &= (-7 \times 4) - (1 \times 4) \\
&= -28 - (-5)
= -23
$$

---

## Soal 2

$$
A =
\begin{bmatrix}
0 & 2 & -3 \\
1 & -2 & -1 \\
0 & 0 & 1
\end{bmatrix}
$$

### Jawaban

$$
det (\text{A}) &= 0 \cdot M_{11} - 2 \cdot M_{12} + (-3) \cdot M_{13} \\ \\
% 
&= 0 \cdot
\begin{bmatrix}-2 & -1 \\ 0 & 1\end{bmatrix}
- 2 \cdot
\begin{bmatrix}1 & -1 \\ 0 & 1\end{bmatrix}
- 3 \cdot
\begin{bmatrix}1 & -2 \\ 0 & 0\end{bmatrix} \\ \\
% 
&= 0 \cdot
\begin{bmatrix}-2 & -1 \\ 0 & 1\end{bmatrix}
- 2 \cdot
\begin{bmatrix}1 & -1 \\ 0 & 1\end{bmatrix}
- 3 \cdot
\begin{bmatrix}1 & -2 \\ 0 & 0\end{bmatrix}
$$

Hitung determinan $2\times2$:

$$
\begin{bmatrix}-2 & -1 \\ 0 & 1\end{bmatrix}
&= (-2 \times 1) - (-1 \times 0) = -2 \\ \\
\begin{bmatrix}1 & -1 \\ 0 & 1\end{bmatrix}
&= (1 \times 1) - (-1 \times 0) = 1 \\ \\
\begin{bmatrix}1 & -2 \\ 0 & 0\end{bmatrix}
&= (1 \times 0) - (-2 \times 0)= 0
$$

Maka:

$$
det (\text{a}) &= 0 (-2) - 2 (1) - 3 (0) \\
&= 0 - 2 - 0 \\
&= -2
$$

---

## Soal 3

$$
A = \begin{bmatrix} 1 & -3 & 1 & 1 \\ -3 & 1 & 1 & 1 \\ 1 & 1 & -3 & 1 \\ 1 & 1 & 1 & -3 \end{bmatrix}
$$

### Jawaban

$$
det (\text{A}) &= 1 \cdot M_{11} - (-3) \cdot M_{12} + 1 \cdot M_{13} - 1 \cdot M_{14}
$$

Maka:

$$
1 \cdot M_{11} &= 1 \cdot
\begin{bmatrix}
1 & 1 & 1 \\
1 & -3 & 1 \\
1 & 1 & -3
\end{bmatrix} \\
% 
3 \cdot M_{12} &= 3 \cdot
\begin{bmatrix}-3 & 1 & 1 \\
1 & -3 & 1 \\
1 & 1 & -3
\end{bmatrix} \\
% 
1 \cdot M_{13} &= 1 \cdot
\begin{bmatrix}-3 & 1 & 1 \\
1 & 1 & 1 \\
1 & 1 & -3
\end{bmatrix} \\
% 
1 \cdot M_{14} &= 1 \cdot
\begin{bmatrix}
-3 & 1 & 1 \\
1 & 1 & -3 \\
1 & 1 & 1
\end{bmatrix} \\
$$

Pertama, hitung "$1 \cdot M_{11}$":

$$
1 \cdot M_{11} &= 1 \cdot
\begin{bmatrix}
1 & 1 & 1 \\
1 & -3 & 1 \\
1 & 1 & -3
\end{bmatrix} \\\\
% 
&= 1 \cdot
\left( 1 \cdot
\begin{bmatrix}
-3 & 1 \\
1 & -3
\end{bmatrix}
- 1 \cdot
\begin{bmatrix}
1 & 1 \\
1 & -3
\end{bmatrix}
+ 1 \cdot
\begin{bmatrix}
1 & 1 \\
1 & -3
\end{bmatrix} \right) \\\\
% 
&= 1 \cdot (1 \cdot ((-3 \cdot -3) - (1 \cdot 1)) - 1 \cdot ((1 \cdot -3) - (1 \cdot 1)) + 1 \cdot ((1 \cdot -3) - (1 \cdot 1)) \\\\
% 
&= 1 \cdot (1 \cdot (9 - 1) - 1 \cdot (-3 - 1) + 1 \cdot (-3 - 1)) \\\\
% 
&= 1 \cdot (1 \cdot 8 - 1 \cdot (-4) + 1 \cdot (-4)) \\\\
% 
&= 1 \cdot ( 8 + 4 - 4) \\\\
% 
&= 1 \cdot 8 \\\\
% 
&= 8
$$

Kedua, hitung "$3 \cdot M_{12}$":

$$
3 \cdot M_{12} &= 3 \cdot
\begin{bmatrix}
-3 & 1 & 1 \\
1 & -3 & 1 \\
1 & 1 & -3
\end{bmatrix} \\\\
% 
&= 3 \cdot
\left( -3 \cdot
\begin{bmatrix}
-3 & 1 \\
1 & -3
\end{bmatrix}
- 1 \cdot
\begin{bmatrix}
1 & 1 \\
1 & -3
\end{bmatrix}
+ 1 \cdot
\begin{bmatrix}
1 & -3 \\
1 & 1
\end{bmatrix} \right) \\\\
% 
&= 3 \cdot \left( -3 \cdot ((-3 \cdot -3) - (1 \cdot 1)) - 1 \cdot ((1 \cdot -3) - (1 \cdot 1)) + 1 \cdot ((1 \cdot 1) - (1 \cdot -3)) \right) \\\\
% 
&= 3 \cdot \left( -3 \cdot (9 - 1) - 1 \cdot (-3 - 1) + 1 \cdot (1 - (-3)) \right) \\\\
% 
&= 3 \cdot \left( -3 \cdot 8 - 1 \cdot (-4) + 1 \cdot (4) \right) \\\\
% 
&= 3 \cdot \left( -24 + 4 + 4 \right) \\\\
% 
&= 3 \cdot (-16) \\\\
% 
&= -48
$$

Ketiga, hitung "$1 \cdot M_{13}$":

$$
1 \cdot M_{13} &= 1 \cdot
\begin{bmatrix}
-3 & 1 & 1 \\
1 & 1 & 1 \\
1 & 1 & -3
\end{bmatrix} \\\\
% 
&= 1 \cdot
\left( -3 \cdot
\begin{bmatrix}1 & 1 \\
1 & -3
\end{bmatrix}
- 1 \cdot
\begin{bmatrix}1 & 1 \\
1 & -3
\end{bmatrix}
+ 1 \cdot
\begin{bmatrix}1 & 1 \\
1 & 1
\end{bmatrix} \right) \\\\
% 
&= 1 \cdot \left( -3 \cdot ((1 \cdot -3) - (1 \cdot 1)) - 1 \cdot ((1 \cdot -3) - (1 \cdot 1)) + 1 \cdot ((1 \cdot 1) - (1 \cdot 1)) \right) \\\\
% 
&= 1 \cdot \left( -3 \cdot (-3 - 1) - 1 \cdot (-3 - 1) + 1 \cdot (1 - 1) \right) \\\\
% 
&= 1 \cdot \left( -3 \cdot (-4) - 1 \cdot (-4) + 1 \cdot (0) \right) \\\\
% 
&= 1 \cdot \left( 12 + 4 + 0 \right) \\\\
% 
&= 1 \cdot 16 \\\\
% 
&= 16
$$ 

Keempat, hitung "$1 \cdot M_{14}$":

$$
1 \cdot M_{14} &= 1 \cdot
\begin{bmatrix}
-3 & 1 & 1 \\
1 & 1 & -3 \\
1 & 1 & 1
\end{bmatrix} \\\\
% 
&= 1 \cdot
\left( -3 \cdot
\begin{bmatrix}
1 & -3 \\
1 & 1
\end{bmatrix}
- 1 \cdot
\begin{bmatrix}
1 & -3 \\
1 & 1
\end{bmatrix}
+ 1 \cdot
\begin{bmatrix}
1 & 1 \\
1 & 1
\end{bmatrix} \right) \\\\
% 
&= 1 \cdot \left( -3 \cdot ((1 \cdot 1) - (-3 \cdot 1)) - 1 \cdot ((1 \cdot 1) - (-3 \cdot 1)) + 1 \cdot ((1 \cdot 1) - (1 \cdot 1)) \right) \\\\
% 
&= 1 \cdot \left( -3 \cdot (1 + 3) - 1 \cdot (1 + 3) + 1 \cdot (0) \right) \\\\
% 
&= 1 \cdot \left( -3 \cdot 4 - 1 \cdot 4 + 0 \right) \\\\
% 
&= 1 \cdot (-12 - 4) \\\\
% 
&= 1 \cdot (-16) \\\\
% 
&= -16
$$

Setelah mendapatkan determinan dari setiap minor, kita dapat menghitung determinan dari matriks $A$:

$$
det (\text{A}) &= 1 \cdot M_{11} - (-3) \cdot M_{12} + 1 \cdot M_{13} - 1 \cdot M_{14} \\\\
&= 1 \cdot 8 - (-3) \cdot (-48) + 1 \cdot 16 - 1 \cdot (-16) \\\\
&= 8 - 144 + 16 + 16 \\\\
&= -104
$$

---
---

## Soal 4 (Adjoin dan Invers)

$$
A =
\begin{bmatrix}
-7 & -5 \\
1 & 4
\end{bmatrix}
$$

### Jawaban

Langkah pertama adalah menghitung adjoin dari matriks $A$:

$$
\text{adj}(\text{A})
% 
&= 
\begin{bmatrix}
-7 & -5 \\
1 & 4
\end{bmatrix}\\\\
% 
&=
\begin{bmatrix}
4 & -1 \\
5 & -7
\end{bmatrix}\\\\
% 
&=
\begin{bmatrix}
4 & 5 \\
-1 & -7
\end{bmatrix}
$$

Selanjutnya, hitung invers dari matriks $A$:

$$
A^{-1} &= \frac{1}{det(\text{A})} \cdot \text{adj}(\text{A})\\\\
% 
&= \frac{1}{-23} \cdot
\begin{bmatrix}
4 & 5 \\
-1 & -7
\end{bmatrix}\\\\
%
&=
\begin{bmatrix}
-\frac{4}{23} & -\frac{5}{23} \\
\frac{1}{23} & \frac{7}{23}
\end{bmatrix}
$$

---

## Soal 5 (Adjoin dan Invers)

$$
A =
\begin{bmatrix}
0 & 2 & -3 \\
1 & -2 & -1 \\
0 & 0 & 1
\end{bmatrix}
$$

### Jawaban

Langkah pertama adalah menghitung kofaktor dari setiap elemen pada matriks $A$:

$$
C_{11} &= (-1)^{1+1} \cdot
\begin{bmatrix}
-2 & -1 \\
0 & 1
\end{bmatrix}
% 
= 1 \cdot ((-2 \cdot 1) - (-1 \cdot 0)) = -2 \\\\
%
C_{12} &= (-1)^{1+2} \cdot
\begin{bmatrix}1 & -1 \\
0 & 1
\end{bmatrix}
%
= -1 \cdot ((1 \cdot 1) - (-1 \cdot 0)) = -1 \\\\
%
C_{13} &= (-1)^{1+3} \cdot
\begin{bmatrix}1 & -2 \\
0 & 0
\end{bmatrix}
%
= 1 \cdot ((1 \cdot 0) - (-2 \cdot 0)) = 0 \\\\
%
C_{21} &= (-1)^{2+1} \cdot
\begin{bmatrix}2 & -3 \\
0 & 1
\end{bmatrix}
%
= -1 \cdot ((2 \cdot 1) - (-3 \cdot 0)) = -2 \\\\
%
C_{22} &= (-1)^{2+2} \cdot
\begin{bmatrix}0 & -3 \\
0 & 1
\end{bmatrix}
%
= 1 \cdot ((0 \cdot 1) - (-3 \cdot 0)) = 0 \\\\
%
C_{23} &= (-1)^{2+3} \cdot
\begin{bmatrix}0 & 2 \\
0 & 0
\end{bmatrix}
%
= -1 \cdot ((0 \cdot 0) - (2 \cdot 0)) = 0 \\\\
%
C_{31} &= (-1)^{3+1} \cdot
\begin{bmatrix}2 & -3 \\
-2 & -1
\end{bmatrix}
%
= 1 \cdot ((2 \cdot -1) - (-3 \cdot -2)) = 4 \\\\
%
C_{32} &= (-1)^{3+2} \cdot
\begin{bmatrix}0 & -3 \\
1 & -1
\end{bmatrix}
%
= -1 \cdot ((0 \cdot -1) - (-3 \cdot 1)) = -3 \\\\
%
C_{33} &= (-1)^{3+3} \cdot
\begin{bmatrix}0 & 2 \\
1 & -2
\end{bmatrix}
%
= 1 \cdot ((0 \cdot -2) - (2 \cdot 1)) = -2
$$

Maka, matriks kofaktor adalah:

$$
C =
\begin{bmatrix}
-2 & -1 & 0 \\
-2 & 0 & 0 \\
4 & -3 & -2
\end{bmatrix}
$$

Setelah didapatkan matriks kofaktor, kita dapat menghitung adjoin dari matriks $A$ dengan mentranspose matriks kofaktor:

$$
\text{adj}(\text{A}) = C^T =
\begin{bmatrix}
-2 & -2 & 4 \\
-1 & 0 & -3 \\
0 & 0 & -2
\end{bmatrix}
$$

Baru setelah itu, kita dapat menghitung invers dari matriks $A$:

$$
A^{-1} &= \frac{1}{det(\text{A})} \cdot \text{adj}(\text{A})\\\\
&= \frac{1}{2} \cdot
\begin{bmatrix}
-2 & -2 & 4 \\
-1 & 0 & -3 \\
0 & 0 & -2
\end{bmatrix}\\\\
&=
\begin{bmatrix}
-1 & -1 & 2 \\
-\frac{1}{2} & 0 & -\frac{3}{2} \\
0 & 0 & -1
\end{bmatrix}
$$

---

## Soal 6 (Adjoin dan Invers)

$$
A = \begin{bmatrix}
1 & -3 & 1 & 1 \\
-3 & 1 & 1 & 1 \\
1 & 1 & -3 & 1 \\
1 & 1 & 1 & -3
\end{bmatrix}
$$

### Jawaban

Langkah pertama, adalah menghitung kofaktor dari setiap elemen pada matriks $A$:

$$
C_{11} &= (-1)^{1+1} \cdot
\begin{bmatrix}
1 & 1 & 1 \\
1 & -3 & 1 \\
1 & 1 & -3
\end{bmatrix}
%
= 1 \cdot ((1 \cdot ((-3 \cdot -3) - (1 \cdot 1))) - 1 \cdot ((1 \cdot -3) - (1 \cdot 1)) + 1 \cdot ((1 \cdot 1) - (1 \cdot -3))) = 8 \\\\
%
C_{12} &= (-1)^{1+2} \cdot
\begin{bmatrix}
-3 & 1 & 1 \\
1 & -3 & 1 \\
1 & 1 & -3
\end{bmatrix}
%
= -1 \cdot ((-3 \cdot ((-3 \cdot -3) - (1 \cdot 1))) - 1 \cdot ((1 \cdot -3) - (1 \cdot 1)) + 1 \cdot ((1 \cdot 1) - (1 \cdot -3))) = -48 \\\\
%
C_{13} &= (-1)^{1+3} \cdot
\begin{bmatrix}-3 & 1 & 1 \\
1 & 1 & 1 \\
1 & 1 & -3
\end{bmatrix}
%
= 1 \cdot ((-3 \cdot ((1 \cdot -3) - (1 \cdot 1))) - 1 \cdot ((1 \cdot -3) - (1 \cdot 1)) + 1 \cdot ((1 \cdot 1) - (1 \cdot 1))) = 16 \\\\
%
C_{14} &= (-1)^{1+4} \cdot
\begin{bmatrix}
-3 & 1 & 1 \\
1 & 1 & -3 \\
1 & 1 & 1
\end{bmatrix}
%
= -1 \cdot ((-3 \cdot ((1 \cdot 1) - (1 \cdot -3))) - 1 \cdot ((1 \cdot 1) - (1 \cdot -3)) + 1 \cdot ((1 \cdot 1) - (1 \cdot 1))) = -16 \\\\
%
C_{21} &= (-1)^{2+1} \cdot
\begin{bmatrix}
-3 & 1 & 1 \\
1 & -3 & 1 \\
1 & 1 & -3
\end{bmatrix}
%
= -1 \cdot ((-3 \cdot ((-3 \cdot -3) - (1 \cdot 1))) - 1 \cdot ((1 \cdot -3) - (1 \cdot 1)) + 1 \cdot ((1 \cdot 1) - (1 \cdot -3))) = -48 \\\\
%
C_{22} &= (-1)^{2+2} \cdot
\begin{bmatrix}
1 & 1 & 1 \\
1 & -3 & 1 \\
1 & 1 & -3
\end{bmatrix}
%
= 1 \cdot ((1 \cdot ((-3 \cdot -3) - (1 \cdot 1))) - 1 \cdot ((1 \cdot -3) - (1 \cdot 1)) + 1 \cdot ((1 \cdot 1) - (1 \cdot -3))) = 8 \\\\
%
C_{23} &= (-1)^{2+3} \cdot
\begin{bmatrix}
1 & -3 & 1 \\
1 & 1 & 1 \\
1 & 1 & -3
\end{bmatrix}
%
= -1 \cdot ((1 \cdot ((1 \cdot -3) - (1 \cdot 1))) - (-3) \cdot ((1 \cdot -3) - (1 \cdot 1)) + 1 \cdot ((1 \cdot 1) - (1 \cdot 1))) = -16 \\\\
%
C_{24} &= (-1)^{2+4} \cdot
\begin{bmatrix}
1 & -3 & 1 \\
1 & 1 & -3 \\
1 & 1 & 1
\end{bmatrix}
%
= 1 \cdot ((1 \cdot ((1 \cdot 1) - (1 \cdot -3))) - (-3) \cdot ((1 \cdot 1) - (1 \cdot -3)) + 1 \cdot ((1 \cdot 1) - (1 \cdot 1))) = 16 \\\\
%
C_{31} &= (-1)^{3+1} \cdot
\begin{bmatrix}
-3 & 1 & 1 \\
1 & 1 & 1 \\
1 & 1 & -3
\end{bmatrix}
%
= 1 \cdot ((-3 \cdot ((1 \cdot -3) - (1 \cdot 1))) - 1 \cdot ((1 \cdot -3) - (1 \cdot 1)) + 1 \cdot ((1 \cdot 1) - (1 \cdot 1))) = 16 \\\\
%
C_{32} &= (-1)^{3+2} \cdot
\begin{bmatrix}
1 & 1 & 1 \\
1 & 1 & 1 \\
1 & 1 & -3
\end{bmatrix}
%
= -1 \cdot ((1 \cdot ((1 \cdot -3) - (1 \cdot 1))) - 1 \cdot ((1 \cdot -3) - (1 \cdot 1)) + 1 \cdot ((1 \cdot 1) - (1 \cdot 1))) = -16 \\\\
%
C_{33} &= (-1)^{3+3} \cdot
\begin{bmatrix}
1 & -3 & 1 \\
1 & 1 & 1 \\
1 & 1 & -3
\end{bmatrix}
%
= 1 \cdot ((1 \cdot ((1 \cdot -3) - (1 \cdot 1))) - (-3) \cdot ((1 \cdot -3) - (1 \cdot 1)) + 1 \cdot ((1 \cdot 1) - (1 \cdot 1))) = 16 \\\\
%
C_{34} &= (-1)^{3+4} \cdot
\begin{bmatrix}
1 & -3 & 1 \\
1 & 1 & 1 \\
1 & 1 & 1
\end{bmatrix}
%
= -1 \cdot ((1 \cdot ((1 \cdot 1) - (1 \cdot 1))) - (-3) \cdot ((1 \cdot 1) - (1 \cdot 1)) + 1 \cdot ((1 \cdot 1) - (1 \cdot 1))) = 0 \\\\
C_{41} &= (-1)^{4+1} \cdot
\begin{bmatrix}
-3 & 1 & 1 \\
1 & -3 & 1 \\
1 & 1 & -3
\end{bmatrix}
%
= -1 \cdot ((-3 \cdot ((-3 \cdot -3) - (1 \cdot 1))) - 1 \cdot ((1 \cdot -3) - (1 \cdot 1)) + 1 \cdot ((1 \cdot 1) - (1 \cdot -3))) = -16 \\\\
C_{42} &= (-1)^{4+2} \cdot
\begin{bmatrix}
1 & 1 & 1 \\
1 & -3 & 1 \\
1 & 1 & -3
\end{bmatrix}
%
= 1 \cdot ((1 \cdot ((-3 \cdot -3) - (1 \cdot 1))) - 1 \cdot ((1 \cdot -3) - (1 \cdot 1)) + 1 \cdot ((1 \cdot 1) - (1 \cdot -3))) = 8 \\\\
C_{43} &= (-1)^{4+3} \cdot
\begin{bmatrix}
1 & -3 & 1 \\
1 & 1 & 1 \\
1 & 1 & -3
\end{bmatrix}
%
= -1 \cdot ((1 \cdot ((1 \cdot -3) - (1 \cdot 1))) - (-3) \cdot ((1 \cdot -3) - (1 \cdot 1)) + 1 \cdot ((1 \cdot 1) - (1 \cdot 1))) = -16 \\\\
C_{44} &= (-1)^{4+4} \cdot
\begin{bmatrix}
1 & -3 & 1 \\
1 & 1 & 1 \\
1 & 1 & -3
\end{bmatrix}
%
= 1 \cdot ((1 \cdot ((1 \cdot -3) - (1 \cdot 1))) - (-3) \cdot ((1 \cdot -3) - (1 \cdot 1)) + 1 \cdot ((1 \cdot 1) - (1 \cdot 1))) = 0
$$

Selanjutnya, kita dapat menyusun matriks kofaktor:

$$
C =
\begin{bmatrix}
8 & -48 & 16 & -16 \\
-48 & 8 & -16 & 16 \\
16 & -16 & 16 & 0 \\
-16 & 16 & 0 & 0
\end{bmatrix}
$$

Setelah didapat matriks kofaktor, selanjutnya adalah menghitung adjoin dari matriks $A$ dengan mentranspose matriks kofaktor:

$$
\text{adj}(\text{A}) = C^T =
\begin{bmatrix}
8 & -48 & 16 & -16 \\
-48 & 8 & -16 & 16 \\
16 & -16 & 16 & 0 \\
-16 & 16 & 0 & 0
\end{bmatrix}^T =
\begin{bmatrix}
8 & -48 & 16 & -16 \\
-48 & 8 & -16 & 16 \\
16 & -16 & 16 & 0 \\
-16 & 16 & 0 & 0
\end{bmatrix}
$$

Setelah didapatkan adjoin dari matriks $A$, kita dapat menghitung invers dari matriks $A$:

$$
A^{-1} &= \frac{1}{det(\text{A})} \cdot \text{adj}(\text{A})\\\\
&= \frac{1}{-104} \cdot
\begin{bmatrix}
8 & -48 & 16 & -16 \\
-48 & 8 & -16 & 16 \\
16 & -16 & 16 & 0 \\
-16 & 16 & 0 & 0
\end{bmatrix}\\\\
&=
\begin{bmatrix}
-\frac{1}{13} & \frac{12}{13} & -\frac{4}{13} & \frac{4}{13} \\
\frac{12}{13} & -\frac{1}{13} & \frac{4}{13} & -\frac{4}{13} \\
-\frac{4}{13} & \frac{4}{13} & -\frac{4}{13} & 0 \\
\frac{4}{13} & -\frac{4}{13} & 0 & 0
\end{bmatrix}
$$