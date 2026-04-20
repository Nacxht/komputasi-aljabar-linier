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
&= 2
$$

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
1 & 1 & 1 \\
1 & 1 & -3
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
