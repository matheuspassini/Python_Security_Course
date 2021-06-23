import hashlib

menu = int(input('Escolha o tipo de Hash a ser utilizada \n 1 - MD5 \n 2 - SHA1 \n 3 - SHA256 \n 4 - SHA512 \n Digite o número: '))
string = input('\n Digite o texto a ser convertido: ')

if menu == 1:
    print('A hash escolhida é -> MD5 \n')
    resultado = hashlib.md5(string.encode('utf-8'))
    print('O hash da string ', string, 'é: ', resultado.hexdigest())
elif menu == 2:
    print('A hash escolhida é -> SHA1 \n')
    resultado = hashlib.sha1(string.encode('utf-8'))
    print('O hash da string ', string, 'é: ', resultado.hexdigest())
elif menu == 3:
    print('A hash escolhida é -> SHA256 \n')
    resultado = hashlib.sha256(string.encode('utf-8'))
    print('O hash da string ', string, 'é: ', resultado.hexdigest())
elif menu == 4:
    string = print('A hash escolhida é -> SHA512 ')
    resultado = hashlib.sha512(string.encode('utf-8'))
    print('O hash da string ', string, 'é: ', resultado.hexdigest())
else:
    print('Há algo errado, tente novamente')


