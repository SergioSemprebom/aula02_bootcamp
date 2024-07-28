# Desafio extra!

# Qtos bugs esse programa pode gerar!
try:

    nome = input("Digite seu nome: ")

    # verifica se 0o nome está vazio
    if len(nome) == 0:
        raise ValueError("O nome nao pode ser vazio")
    
    # Verifica se a numero no nome
    if any(char.isdigit() for char in nome):
        raise ValueError("O nome nao deve conter numeros.")
    
    else:
        print("nome válido:", nome)
except ValueError as e:
    print(e)
    
# solicita ao usuario que digite o valor do seu salrio e convert para float.

try:
    salario = float(input("Digite o seu salario: "))
    if salario < 0:
        print("Digite um valor positivo para o salario.")
except ValueError:
    print("Entrada inválida para o salario. Por favor, digite um numero.")

# solicita ao usuario que digite o valor do bonus recebido e converte para float
try:
    bonus_recebido = float(input("digite o valor do bonus recebido: "))
    if bonus_recebido < 0:
        print("Por favior, digite um valor positivo para o bonus.")
except ValueError:
   print("Entrada inválida para o bonus. Por favor, digite um numero.")

# Assumindo uma lógica de cálculo para o bonus final e KPI
bonus_final = bonus_recebido * 1/2 # Exemplo, ajuste conforme necessario
kpi = (salario +bonus_recebido) / 1000 # Exemplo simples de KPI

# Imprime as informaçoes para o usuario
print(f"Seu KPI é {kpi:.2f}")
print(f"{nome}, seu salario é R${salario:.2f} e seu bonus final é R${bonus_final:.2f}.")