# Reverse list
listmu = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# ada 3 parameter slicing yang setiap element nya dipisahkan dengan tanda :
# parameter pertama dan kedua kosong, artinya adalah data list index start dan end nya 0, yaitu seluruh index list
# parameter ketiga, -1 menandakan dari jumlah index akan di kurang 1 dan di masukan ke listku dari nilai index tsb
listku = listmu[::-1] 
print(f'listku : {listku}')

# Reverse string
kata = 'SEMANGAT'
print(kata[::-1])

