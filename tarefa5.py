def palindromo(palavra):

    palavra_inversa = []

    palavra_normal = []

    for x in palavra.upper()[::-1]:
        palavra_inversa.append(x)

    for c in palavra.upper():
        palavra_normal.append(c)

    if palavra_normal == palavra_inversa:
        print(f'{palavra} é um palíndromo!')

    else:
        print(f'{palavra} não é um palíndromo!')

palindromo(input('Escreva uma palavra:\n'))