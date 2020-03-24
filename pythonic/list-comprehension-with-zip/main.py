nama = ['andi', 'budi', 'riko']
umur = [21, 24, 25]

listku = [[item_nama, item_umur] for item_nama, item_umur in zip(nama, umur)]

print(f'listku : {listku}')