m1 = float(input("Informe a primeira medida do triângulo: "))
m2 = float(input("Informe a segunda medida do triângulo: "))
m3 = float(input("Informe a terceira medida do triângulo: "))


if m1 == m2 and m1 == m3 and  m2==m3:
    print("Seu triângulo é um Equilátero.")

elif m1 > m2+m3 or m2 > m1+m3 or m3 > m1+m2:
    print("Isso não é um triângulo.")

elif m1 != m2 and m1 == m3 and m3 != m2 or m1 == m2:
    print("Seu triângulo é um isósceles.")

elif m1 != m2 and m2 != m3 and m3 != m1:
    print("Seu triângulo é um Escaleno.")


