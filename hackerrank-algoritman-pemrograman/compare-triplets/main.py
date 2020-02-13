import os
import sys

# masalah : membandingkan setiap element index array, apabila alice > bob maka nilai alice nambah 1 dan sebaliknya
def compareTriplets(a, b):
    # solusi 1
    # alice = 0
    # bob = 0 
    # for i in range(len(a)):
    #     if a[i] > b[i]:
    #        alice += 1
    #     elif a[i] < b[i]:
    #         bob += 1
    # return alice, bob

    # solusi 2
    alice = 0
    bob = 0
    for x, y in zip(a, b):
        if x > y:
            alice += 1
        elif x < y:
            bob += 1
    return alice, bob

if __name__ == "__main__":
    fptr = sys.stdout

    a = list(map(int, input().rstrip().split()))
    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()