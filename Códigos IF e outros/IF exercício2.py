"""
Programa de casa de câmbio. Crie um programa que pergunte qual moeda deseja obter, e qual moeda irá dar em troca
Moedas a considerar: Dólar, Real, Euro e Libra esterlina
informar as cotações das moedas em uma variável, já no início do código
EX1:
Quero: Euro
Tenho: Real
Valor desejado: 100 Euros
Valor necessário: 578,00 reais
EX2:
Quero: Libra esterlina
Tenho: Euro
Valor desejado: 100 Libras
Valor necessário: 120 Euros
"""
print("-"*50)
print("CASA DE CÂMBIO".center(50))
print("-"*50)
# dolar, real, euro, libra
moedas = [4.82, 1, 5.17, 6.04]
tipo_moedas = ['Dólares', 'Reais', 'Euros', 'Libras Esterlinas']
entrada = int(input("""
(1)Dólar
(2)Real
(3)Euro
(4)Libra esterlina
TENHO: """))
saida = int(input("""
(1)Dólar
(2)Real
(3)Euro
(4)Libra esterlina
QUERO: """))
valor_necessario = float(input(f'Quantos {tipo_moedas[saida-1]} você deseja?: '))
print(f'Você precisa de: {valor_necessario/moedas[entrada-1]*moedas[saida-1]:.2f} {tipo_moedas[entrada-1]}')
