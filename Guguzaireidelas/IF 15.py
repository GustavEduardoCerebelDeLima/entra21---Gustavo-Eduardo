nome = input("Digite seu nome: ")
print(" ")
cargo = input("Escolha seu cargo 1)Professor 2)Coordenador 3)Zelador")
print(" ")
salario = float(input("Digite seu salário: "))
print(" ")
salarionovo = salario * 1.1
bonificação = salarionovo * 0.05

if salarionovo < 1999:
    irrf = 0
elif salarionovo < 2967:
    irrf = salarionovo * 0.75
elif salarionovo < 3938:
    irrf = salarionovo * 0.15
elif salarionovo < 4987:
    irrf = salarionovo * 0.225
else:
    irrf = salarionovo * 0.275

print(nome.upper())

if cargo == "1":
      print("Professor")
elif cargo == "2":
      print("Coordenador")
else:
      print("Zelador")

print("Salario novo é: ", salarionovo)
print("Bonificação é: ", bonificação)
print("IRRF é: ", irrf)

