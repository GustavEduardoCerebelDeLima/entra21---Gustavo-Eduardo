nome = input("Digite seu nome: ")
n1 = int(input("Digite a primeira nota: "))
n2 = int(input("Digite a segunda nota: "))
n3 = int(input("Digite a terceira nota: "))
n4 = int(input("Digite a quarta nota: "))
média = (n1+n2+n3+n4)/4

print("A sua média é: ", média)

if média == 10:
    print("Parabéns, SUPER APROVADO")
elif média >= 7:
    print("Parabéns, APROVADO")
elif média >= 5:
    print("Exame")
elif média >= 3:
    print("Tu é burro pakas, REPROVADO")

else:
    print("MLK TU É MT BURRO, REPROVADO DE CTZ")

