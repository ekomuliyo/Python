import os
import sys

# masalah : menjumlah semua isi array
def simpleArraySum(ar):
    # solusi 1
    # hasil_jumlah = 0
    # for i in range(len(ar)):
    #     hasil_jumlah += ar[i]
    # return hasil_jumlah

    # solusi 2
    # hasi_jumlah = 0
    # for bilangan in ar:
    #     hasi_jumlah += bilangan
    # return hasi_jumlah

    # solusi 3
    return sum(ar)
        
    

if __name__ == "__main__":
    fptr = sys.stdout

    ar_count = int(input())

    ar = list(map(int, input().rstrip().split()))
    
    result = simpleArraySum(ar)

    fptr.write(str(result) + '\n')

    fptr.close()

