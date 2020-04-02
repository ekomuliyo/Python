# Switch case dengan memanfaatkan Dictionary

def one():
    print('satu')

def two():
    print('dua')

def three():
    print('tiga')

case = 'tiga'

switch = {
    'satu': one,
    'dua': two,
    'tiga': three
}

switch[case]()