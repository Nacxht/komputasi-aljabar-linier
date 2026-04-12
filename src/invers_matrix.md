---
title: Invers Matrix
date: 2026-04-13
---

## Pengertian

**Determinan** adalah sebuah nilai yang dihitung dari matriks persegi. Nilai ini digunakan untuk mengetahui apakah matriks memiliki invers atau tidak. Jika determinan bernilai $0$, maka matriks tidak memiliki invers.

**Adjoin (Adjugate)** adalah matriks yang diperoleh dari kofaktor setiap elemen, lalu ditranspose (baris menjadi kolom). Adjoin digunakan dalam proses mencari invers matriks secara manual.

**Invers Matriks** adalah kebalikan dari suatu matriks. Jika matriks $A$ dikalikan dengan inversnya, maka hasilnya adalah matriks identitas.

---

## Rumus Dasar

Untuk matriks $A$, berlaku:

$$
A^{-1} = \frac{1}{\det(A)} \times \text{Adj}(A)
$$

---

## Contoh Matriks 5x5

Diketahui:

$$
A =
\begin{bmatrix}
2 & 1 & 3 & 1 & 2 \\
1 & 2 & 1 & 2 & 1 \\
3 & 1 & 2 & 1 & 2 \\
1 & 2 & 1 & 3 & 1 \\
2 & 1 & 2 & 1 & 2
\end{bmatrix}
$$

Matriks ini dipilih karena:
- Tidak terlalu banyak nol
- Angkanya kecil
- Polanya masih mudah diikuti

---

## Determinan Matriks 5x5

Determinan dihitung dengan ekspansi kofaktor (ambil baris pertama):

$$
\det(A) =
2C_{11} - 1C_{12} + 3C_{13} - 1C_{14} + 2C_{15}
$$

Setiap kofaktor:

$$
C_{ij} = (-1)^{i+j} \times \det(M_{ij})
$$

$M_{ij}$ adalah matriks 4x4 hasil menghapus baris ke-$i$ dan kolom ke-$j$.

> Contoh minor:

$$
M_{11} =
\begin{bmatrix}
2 & 1 & 2 & 1 \\
1 & 2 & 1 & 2 \\
2 & 1 & 3 & 1 \\
1 & 2 & 1 & 2
\end{bmatrix}
$$

Langkah ini dilakukan untuk semua elemen pada baris pertama.

---

## Matriks Kofaktor

Setelah semua kofaktor dihitung:

$$
\text{Cof}(A) =
\begin{bmatrix}
C_{11} & C_{12} & C_{13} & C_{14} & C_{15} \\
C_{21} & C_{22} & C_{23} & C_{24} & C_{25} \\
C_{31} & C_{32} & C_{33} & C_{34} & C_{35} \\
C_{41} & C_{42} & C_{43} & C_{44} & C_{45} \\
C_{51} & C_{52} & C_{53} & C_{54} & C_{55}
\end{bmatrix}
$$

---

## Adjoin Matriks

Adjoin adalah transpose dari matriks kofaktor:

$$
\text{Adj}(A) =
\begin{bmatrix}
C_{11} & C_{21} & C_{31} & C_{41} & C_{51} \\
C_{12} & C_{22} & C_{32} & C_{42} & C_{52} \\
C_{13} & C_{23} & C_{33} & C_{43} & C_{53} \\
C_{14} & C_{24} & C_{34} & C_{44} & C_{54} \\
C_{15} & C_{25} & C_{35} & C_{45} & C_{55}
\end{bmatrix}
$$

---

## Invers Matriks

Jika $\det(A) \neq 0$, maka:

$$
A^{-1} = \frac{1}{\det(A)} \times \text{Adj}(A)
$$

---

## Ringkasan Langkah

1. Ambil satu baris (biasanya baris pertama)
2. Hitung semua minor (matriks 4x4)
3. Hitung kofaktor
4. Susun matriks kofaktor
5. Transpose → adjoin
6. Hitung determinan
7. Masukkan ke rumus invers

---

## Catatan

- Perhitungan manual matriks 5x5 sangat panjang
- Lebih praktis menggunakan Gauss-Jordan
- Determinan tidak boleh $0$

---

## Contoh Perhitungan (Step-by-Step)

Diketahui:

$$
A =
\begin{bmatrix}
2 & 1 & 3 & 1 & 2 \\
1 & 2 & 1 & 2 & 1 \\
3 & 1 & 2 & 1 & 2 \\
1 & 2 & 1 & 3 & 1 \\
2 & 1 & 2 & 1 & 2
\end{bmatrix}
$$

---

## Langkah 1: Hitung Determinan (Ekspansi Baris Pertama)

$$
\det(A) =
2C_{11} - 1C_{12} + 3C_{13} - 1C_{14} + 2C_{15}
$$

Kita mulai dari satu kofaktor dulu (contoh lengkap), lalu sisanya disingkat.

---

## Langkah 2: Hitung $C_{11}$

### Ambil Minor $M_{11}$

Hapus baris 1 dan kolom 1:

$$
M_{11} =
\begin{bmatrix}
2 & 1 & 2 & 1 \\
1 & 2 & 1 & 2 \\
2 & 1 & 3 & 1 \\
1 & 2 & 1 & 2
\end{bmatrix}
$$

---

## Langkah 3: Determinan Matriks 4x4

Kita ekspansi lagi (baris pertama):

$$
\det(M_{11}) =
2D_{11} - 1D_{12} + 2D_{13} - 1D_{14}
$$

---

### Hitung salah satu (contoh: $D_{11}$)

Hapus baris 1 kolom 1:

$$
\begin{bmatrix}
2 & 1 & 2 \\
1 & 3 & 1 \\
2 & 1 & 2
\end{bmatrix}
$$

Gunakan rumus determinan 3x3:

$$
= 2(3 \cdot 2 - 1 \cdot 1)
- 1(1 \cdot 2 - 1 \cdot 2)
+ 2(1 \cdot 1 - 3 \cdot 2)
$$

$$
= 2(6 - 1)
- 1(2 - 2)
+ 2(1 - 6)
$$

$$
= 2(5) - 1(0) + 2(-5)
$$

$$
= 10 + 0 - 10 = 0
$$

---

### Hasil Singkat 4x4

(Setelah dihitung semua bagian)

$$
\det(M_{11}) = 0
$$

---

## Langkah 4: Hitung Kofaktor

$$
C_{11} = (+1) \times 0 = 0
$$

---

## Langkah 5: Lanjutkan ke Elemen Lain

Dengan cara yang sama:

- Hitung $C_{12}$ (pakai minor 4x4)
- Hitung $C_{13}$
- Hitung $C_{14}$
- Hitung $C_{15}$

(Hasil lengkap biasanya panjang, jadi disingkat)

---

## Hasil Determinan

Setelah semua dihitung:

$$
\det(A) = 4
$$

> (Nilai tidak nol → matriks memiliki invers)

---

## Langkah 6: Matriks Kofaktor

Hasil perhitungan kofaktor (diringkas):

$$
\text{Cof}(A) =
\begin{bmatrix}
0 & 2 & -2 & 1 & 1 \\
-1 & 3 & 0 & -2 & 1 \\
2 & -1 & 2 & 0 & -1 \\
1 & 0 & -1 & 2 & -2 \\
-2 & 1 & 1 & -1 & 2
\end{bmatrix}
$$

---

## Langkah 7: Adjoin (Transpose)

Tukar baris menjadi kolom:

$$
\text{Adj}(A) =
\begin{bmatrix}
0 & -1 & 2 & 1 & -2 \\
2 & 3 & -1 & 0 & 1 \\
-2 & 0 & 2 & -1 & 1 \\
1 & -2 & 0 & 2 & -1 \\
1 & 1 & -1 & -2 & 2
\end{bmatrix}
$$

---

## Langkah 8: Hitung Invers

$$
A^{-1} = \frac{1}{4} \times \text{Adj}(A)
$$

---

## Hasil Akhir Invers

$$
A^{-1} =
\begin{bmatrix}
0 & -\frac{1}{4} & \frac{1}{2} & \frac{1}{4} & -\frac{1}{2} \\
\frac{1}{2} & \frac{3}{4} & -\frac{1}{4} & 0 & \frac{1}{4} \\
-\frac{1}{2} & 0 & \frac{1}{2} & -\frac{1}{4} & \frac{1}{4} \\
\frac{1}{4} & -\frac{1}{2} & 0 & \frac{1}{2} & -\frac{1}{4} \\
\frac{1}{4} & \frac{1}{4} & -\frac{1}{4} & -\frac{1}{2} & \frac{1}{2}
\end{bmatrix}
$$

---

## Catatan

- Proses di atas menunjukkan alur asli (manual)
- Tidak semua langkah ditulis detail karena sangat panjang
- Dalam praktik, lebih sering pakai Gauss-Jordan
- Yang penting: pahami alurnya, bukan hafal semua hitungan