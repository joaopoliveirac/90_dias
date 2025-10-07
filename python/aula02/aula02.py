### Desafio - Refatorar o projeto da aula anterior evitando Bugs!

# 1) Solicita ao usuário que digite seu nome

# 2) Solicita ao usuário que digite o valor do seu salário
# Converte a entrada para um número de ponto flutuante

# 3) Solicita ao usuário que digite o valor do bônus recebido
# Converte a entrada para um número de ponto flutuante

# 4) Calcule o valor do bônus final

# 5) Imprime a mensagem personalizada incluindo o nome do usuário, salário e bônus

# Bônus: Quantos bugs e riscos você consegue identificar nesse programa?

try:
    nome = input('digite seu nome: ')

    if not nome:
        raise ValueError('O nome não pode estar vazio.')
    elif not isinstance(nome, str):
        raise ValueError('O nome tem que ser uma string.')
    elif any(char.isdigit() for char in nome): #se qualquer caracter na variavel for numero, ele retorna verdadeiro e vai pro erro.
        raise ValueError('Tem numero no nome.')
    else:
        print(f'{nome} é valido.')
except ValueError as e:
    print(e)
    exit()

try:
    salario = float(input("Digite o valor do seu salário: "))
    if salario < 0:
        raise ValueError("Por favor, digite um valor positivo para o salário.")
except ValueError as e:
    print(e)
    exit()

try:
    bonus = float(input("Digite o valor do bônus recebido: "))
    if bonus < 0:
        raise ValueError("Por favor, digite um valor positivo para o bônus.")
except ValueError as e:
    print(e)
    exit()

bonus_recebido = 1000 + salario * bonus  # Exemplo simples de KPI

# Imprime as informações para o usuário
print(f"{nome}, seu salário é R${salario:.2f} e seu bônus final é R${bonus_recebido:.2f}.")

