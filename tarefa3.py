import json

with open('dados.json', 'r') as arquivo:
    objeto = json.load(arquivo)

menor_faturamento_dia = 0
maior_faturamento_dia = objeto[0]['valor']
soma_faturamento = 0
dias_faturamento_superior_media_mensal = 0

for y in range(30):
    soma_faturamento += objeto[y]['valor']

media_faturamento = soma_faturamento/30

for y in range(30):
    if objeto[y]['valor'] < menor_faturamento_dia:
        menor_faturamento_dia = objeto[y]['valor']

    if objeto[y]['valor'] > maior_faturamento_dia:
        maior_faturamento_dia = objeto[y]['valor']

    if objeto[y]['valor'] > media_faturamento:
        dias_faturamento_superior_media_mensal += 1

    else:
        pass

print(f'A media de faturamento desse mes foi de {media_faturamento}\nOcorreram {dias_faturamento_superior_media_mensal} dias que o faturamento foi superior a media diaria\nO maior faturamento em um dia foi de {maior_faturamento_dia}\nO menor faturamento em um dia foi de {menor_faturamento_dia}')






