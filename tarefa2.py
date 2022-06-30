n1 = 0
n2 = 1
lista_fibonacci = []
n_usuario = int(input('Digite um número:\n'))

for x in range(n_usuario+1):
    n3 = n1+n2
    lista_fibonacci.append(n1)
    n1 = n2
    n2 = n3

if n_usuario in lista_fibonacci:
    print(f'O numero {n_usuario} esta na sequencia de fibonacci!')
else:
    print(f'O numero {n_usuario} nao esta na squencia de fibonacci!')
