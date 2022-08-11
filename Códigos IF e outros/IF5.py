print(30*"-")
txt = "MONTE DE OPÇÕES"
txt = txt.center (36)
print(txt)
print(30*"-")
print("1-Converter de Celsius para Kelvin")
print("2-Converter de Celsius para Fahrenheit")
print("3-Converter de Kelvin para Celsius")
print("4-Converter de Kelvin para Fahrenheit")
print("5-Converter de Fahrenheit para Celsius")
print("6-Converter de Fahrenheit para Kelvin")
print(" ")
op1 = int(input("Seleciona uma das opções: "))

if op1 == 1:
    print(" ")
    num1 = int(input("Quantos Celsius?: "))
    print(" ")
    print("De Celsiu para Kelvin é: ", num1 + 273.15, "K")
    print(" ")

elif op1 == 2:
    print(" ")
    num1 = int(input("Quantos Celsius?: "))
    print(" ")
    print("De Celsiu para Fahrenheit é: ", (num1 * 9/5)+32, "ºF")
    print(" ")

elif op1 == 3:
    print(" ")
    num1 = int(input("Quantos Kelvins?: "))
    print(" ")
    print("De Kelvins para Celsius é: ", num1 - 273.15, "ºC")
    print(" ")

elif op1 == 4:
    print(" ")
    num1 = int(input("Quantos Kelvins?: "))
    print(" ")
    print("De Kelvins para  é: ", (num1 - 273.15)*9/5 + 32, "ºF")
    print(" ")

elif op1 == 5:
    print(" ")
    num1 = int(input("Quantos Fahrenheit?: "))
    print(" ")
    print("De Fahrenheit para Celsius é: ", (num1 - 32) * 5/9, "ºC")
    print(" ")

elif op1 == 6:
    print(" ")
    num1 = int(input("Quantos Fahrenheit?: "))
    print(" ")
    print("De Fahrenheit para Kelvin é: ", (num1 - 32) * 5/9 + 273.15, "ºK")
    print(" ")

