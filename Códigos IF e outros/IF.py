nome = input(" Digite seu nome")
n1 = int(input(" Digite a 1 nota"))
n2 = int(input(" Digite a 2 nota"))
n3 = int(input(" Digite a 3 nota"))
n4 = int(input(" Digite a 4 nota"))
media = (n1+n2+n3+n4)/4

print(" sua média é", media)

if media >=7:

    print(nome, "foi aprovado")
elif media >= 5:
    print(nome,",você ficou em exame")
else:
    print(nome, "Deu ruim pru c")