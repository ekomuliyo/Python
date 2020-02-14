# masalah : mencari nilai positif, negatif, dan nol lalu dibagi dengan jumlah array

def plusMinus(array):
    # Solusi 1
    # n = len(array)
    # positif, negatif, nol = 0, 0, 0
    # for bilangan in array:
    #     if bilangan > 0:
    #         positif += 1
    #     elif bilangan < 0:
    #         negatif += 1
    #     else:
    #         nol += 1
    # print(positif / n)
    # print(negatif / n)
    # print(nol / n)

    # Solusi 2 menggunakan list comprehensive
    # n = len(array)
    # positif = len(tuple([bilangan for bilangan in array if bilangan > 0]))
    # negatif = len(tuple([bilangan for bilangan in array if bilangan < 0]))
    # nol = len(tuple([bilangan for bilangan in array if bilangan == 0]))
    # print(positif / n)
    # print(negatif / n)
    # print(nol / n)

    # Solusi 3 menggunakan lambda expression
    n = len(array)
    positif = len(tuple(filter(lambda x : x > 0, array)))
    negatif = len(tuple(filter(lambda x : x < 0, array)))
    nol = len(tuple(filter(lambda x: x == 0, array)))

    print(positif / n)
    print(negatif / n)
    print(nol / n)
    
if __name__ == "__main__":
    array = list(map(int, input().rstrip().split()))

    plusMinus(array)