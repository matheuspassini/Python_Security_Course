import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
print("Cliente Socket criado com sucesso")

host = 'localhost'
porta = 5433
mensage = 'Olá servidor'

try:
    print('Cliente: ' + mensage)
    s.sendto(mensage.encode(), (host, 5432))

    dados, servidor = s.recvfrom(4096)
    dados = dados.decode()
    print('Cliente: ' + dados)
finally:
    print('Cliente: fechando a conexão')
    s.close()