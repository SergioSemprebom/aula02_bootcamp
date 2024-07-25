import math

#### Exercícios #####
#Inteiros (int)

# 1 Escreva um programa que soma dois números inteiros inseridos pelo usuário.
print("1)Escreva um programa que soma dois números inteiros inseridos pelo usuário.")
n1 = int(input("Digite o primeiro numero: "))
n2 = int(input("Digite o segundo nuemero: "))

print(f"A soma de {n1} + {n2} = {n1+n2}")
print('==========================================================================================')

# 2 Crie um programa que receba um número do usuário e calcule o resto da divisão desse número por 5.
print("2)Crie um programa que receba um número do usuário e calcule o resto da divisão desse número por 5.")
ns1 = float(input("Digite um numero: "))
print(f"O resto da divisão por 5 é igual: {ns1 % 5}")
print('==========================================================================================')

# 3 Desenvolva um programa que multiplique dois números fornecidos pelo usuário e mostre o resultado.
print("3)Desenvolva um programa que multiplique dois números fornecidos pelo usuário e mostre o resultado.")
m1 = int(input("Digite o primeiro numero: "))
m2 = int(input("Digite o segundo numero: "))

print(f"{m1} X {m2} = {m1 * m2}")
print('==========================================================================================')

# 4 Faça um programa que peça dois números inteiros e imprima a divisão inteira do primeiro pelo segundo.
print("4Faça um programa que peça dois números inteiros e imprima a divisão inteira do primeiro pelo segundo.")
q1 = float(input("Digite o primeiro numero: "))
q2 = float(input("Digite o segundo numero: "))

print(f"{q1} // {q2} = {q1 // q2} ")
print('==========================================================================================')
# 5 Escreva um programa que calcule o quadrado de um número fornecido pelo usuário.

#### Números de Ponto Flutuante (float) #####
# 6 Escreva um programa que receba dois números flutuantes e realize sua adição.
print
# 7 Crie um programa que calcule a média de dois números flutuantes fornecidos pelo usuário.
# 8 Desenvolva um programa que calcule a potência de um número (base e expoente fornecidos pelo usuário).
# 9 Faça um programa que converta a temperatura de Celsius para Fahrenheit.
# 10 Escreva um programa que calcule a área de um círculo, recebendo o raio como entrada.
print("10 Escreva um programa que calcule a área de um círculo, recebendo o raio como entrada.")
area = float(input('Digite um numero: '))
# area_formatada = "{:.2f}".format(area_do_circulo)
print(f"A area do circulo é de: {math.pi} * {area} ** 2")

#Strings (str)
# 11 Escreva um programa que receba uma string do usuário e a converta para maiúsculas.
# 12 Crie um programa que receba o nome completo do usuário e imprima o nome com todas as letras minúsculas.
# 13 Desenvolva um programa que peça ao usuário para inserir uma frase e, em seguida, imprima esta frase sem espaços em branco no início e no final.
# 14 Faça um programa que peça ao usuário para digitar uma data no formato "dd/mm/aaaa" e, em seguida, imprima o dia, o mês e o ano separadamente.
print("14) Faça um programa que peça ao usuário para digitar uma data no formato "dd/mm/aaaa" e, em seguida, imprima o dia, o mês e o ano separadamente.")

data = input("Insira uma data no formato dd/mm/aaa")
lista_de_dia_mes_ano = data.split("/")
print(f"O elemento 1 e o: {lista_de_dia_mes_ano[0]}")
print(f"O elemento 2 e o: {lista_de_dia_mes_ano[1]}")
print(f"O elemento 1 e o: {lista_de_dia_mes_ano[2]}")

# 15 Escreva um programa que concatene duas strings fornecidas pelo usuário.
#Booleanos (bool)
#Escreva um programa que avalie duas expressões booleanas inseridas pelo usuário e retorne o resultado da operação AND entre elas.
#Crie um programa que receba dois valores booleanos do usuário e retorne o resultado da operação OR.
#Desenvolva um programa que peça ao usuário para inserir um valor booleano e, em seguida, inverta esse valor.
#Faça um programa que compare se dois números fornecidos pelo usuário são iguais.
#Escreva um programa que verifique se dois números fornecidos pelo usuário são diferentes.
