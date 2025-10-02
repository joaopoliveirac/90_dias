# Escreva um programa em Python que solicita ao usuário para digitar seu nome, o valor do seu salário mensal e o valor do bônus que recebeu. 
# O programa deve, então, imprimir uma mensagem saudando o usuário pelo nome e informando o valor do salário em comparação com o bônus recebido.

nome = str(input('Informe seu nome: '))
salario = float(input('Informe o seu salário mensal: '))
bonus = float(input('Informe o seu bonus: '))
valor_bonus = (1000 + salario) * bonus

print(f'Olá {nome}! O valor do seu bônus é de {valor_bonus}')