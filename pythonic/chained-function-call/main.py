def tambah(a, b):
    return a + b

def kali(a, b):
    return a * b

a, b = 10, 30

kondisi = False

hasil = (tambah if kondisi else kali)(a,b)
print(f'hasil : {hasil}')