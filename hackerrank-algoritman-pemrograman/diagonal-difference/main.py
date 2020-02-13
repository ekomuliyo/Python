import os
import sys

# masalah : menjumlahkan 2 diagonal dari sebuah matriks

def diagonalDifference(array):
    d1, d2 = 0, 0
    n = len(array)
    for i in range(n):
        d1 += array[i][i]
        d2 += array[i][n-i-1]

    return abs(d1-d2) # abs adalah absolute untuk menghidari bilangan negatif dari perbandingan

if __name__ == "__main__":
    fptr = sys.stdout

    n = int(input().strip())

    array = []

    for _ in range(n):
        array.append(list(map(int, input().strip().split())))

    result = diagonalDifference(array)

    fptr.write(str(result) + '\n')
    fptr.close()