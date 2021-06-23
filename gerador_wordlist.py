import itertools

string = int(input('Digite o número de dígitos a ser permutado: '))
resultado = itertools.permutations('AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789', string)

for i in resultado:
    print(''.join(i))