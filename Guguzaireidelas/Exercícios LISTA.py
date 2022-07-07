print("ORDEM DOS NÚMEROS")
lista = []
while True:
    while True:
        n = input('digite numeros, quando quiser parar digite s: ')
        if n == 's':
            break
        lista.append(n)
    print(lista)
    lista.sort()
    print(lista)
    lista.sort(reverse=True)
    print(lista)
    lista = list(map(int, lista))
    soma = sum(lista)
    print(soma)
    print(f'{sum(lista) / len(lista)}')
    if n == 's':
        break



lista = []
while True:
    while True:
        n = str(input('digite os nomes aqui, quando quiser parar digite stop: '))
        if n == 'stop':
            break
        lista.append(n)
    print(lista)
    lista.sort()
    print(lista)
    lista.sort(reverse=True)
    print(lista)
    print(len(lista))
    print(lista.count('Carlos'))
    break



