# #### Inteiros (`int`)

# 1. Escreva um programa que soma dois números inteiros inseridos pelo usuário.
def exercicio1():
    num1 = int(input('digite o primeiro numero'))
    num2 = int(input('digite o segundo numero'))
    print(f'A soma dos números é: {num1 + num2} ')
# 2. Crie um programa que receba um número do usuário e calcule o resto da divisão desse número por 5.
def exercicio2():
    num = int(input('digite o numero'))
    print(f'O resto da divisão desse número é: {num % 5}')
# 3. Desenvolva um programa que multiplique dois números fornecidos pelo usuário e mostre o resultado.
def exercicio3():
    num1 = int(input('informe o primeiro numero'))
    num2 = int(input('informe o segundo numero'))
    print(f'a multiplicação é: {num1 * num2}')
# 4. Faça um programa que peça dois números inteiros e imprima a divisão inteira do primeiro pelo segundo.
def exercicio4():
    num1 = int(input('informe o primeiro numero'))
    num2 = int(input('informe o segundo numero'))
    print(f'A divisão inteira do primeiro pelo segundo é: {num1 // num2}')
# 5. Escreva um programa que calcule o quadrado de um número fornecido pelo usuário.
def exercicio5():
    num = int(input('informe o numero'))
    print(f'o quadrado do numero é {num ** 2}')

# #### Números de Ponto Flutuante (`float`)

# 6. Escreva um programa que receba dois números flutuantes e realize sua adição.
def exercicio6():
    num1 = float(input('informe o primeiro numero'))
    num2 = float(input('informe o segundo numero'))
    print(f'a soma deles é: {num1 + num2}')
# 7. Crie um programa que calcule a média de dois números flutuantes fornecidos pelo usuário.
def exercicio7():
    num1 = float(input('informe o primeiro numero:'))
    num2 = float(input('informe o segundo numero: '))
    print(f'a media é: {(num1 + num2) / 2}')
# 8. Desenvolva um programa que calcule a potência de um número (base e expoente fornecidos pelo usuário).
def exercicio8():
    base = float(input('informe a base'))
    exp = float(input('informe o expoente'))
    print(base ** exp)
# 9. Faça um programa que converta a temperatura de Celsius para Fahrenheit.
def exercicio9():
    celsius = float(input('informe a temp em celsius'))
    calculo = (celsius * (9/5)) + 32
    print(calculo)
# 10. Escreva um programa que calcule a área de um círculo, recebendo o raio como entrada.
def exercicio10():
    raio = float(input('informe o raio'))
    print(f'a area do ciruclo é: {3.14 * (raio ** 2)}')
# #### Strings (`str`)

# 11. Escreva um programa que receba uma string do usuário e a converta para maiúsculas.
def exercicio11():
    palavra = str(input('informe a string:'))
    print(palavra.upper())
# 12. Crie um programa que receba o nome completo do usuário e imprima o nome com todas as letras minúsculas.
def exercicio12():
    palavra = str(input('informe a string:'))
    print(palavra.lower())

# 13. Desenvolva um programa que peça ao usuário para inserir uma frase e, em seguida, imprima esta frase sem espaços em branco no início e no final.
def exercicio13():
    palavra = str(input('informe a frase: '))
    print(palavra.strip())
# 14. Faça um programa que peça ao usuário para digitar uma data no formato "dd/mm/aaaa" e, em seguida, imprima o dia, o mês e o ano separadamente.
def exercicio14():
    data = str(input('informe a data no formato dd/mm/aaaa'))
    data = data.split('/')
    print(data)
# 15. Escreva um programa que concatene duas strings fornecidas pelo usuário.
def exercicio15():
    palavra1 = str(input('ifnroem a primeira palavra'))
    palavra2 = str(input('informe a segunda palavra'))
    print(palavra1 + ' ' + palavra2)
# #### Booleanos (`bool`)

# 16. Escreva um programa que avalie duas expressões booleanas inseridas pelo usuário e retorne o resultado da operação AND entre elas.
def exercicio16():
    exp1 = True
    exp2 = False
    print(exp1 and exp2)
# 17. Crie um programa que receba dois valores booleanos do usuário e retorne o resultado da operação OR.
def exercicio17():
    exp1 = False
    exp2 = False
    print(exp1 or exp2)

# 18. Desenvolva um programa que peça ao usuário para inserir um valor booleano e, em seguida, inverta esse valor.
def exercicio18():
    valor = True
    valor = not valor
    print(valor)
# 19. Faça um programa que compare se dois números fornecidos pelo usuário são iguais.
def exercicio19():
    valor = True
    valor2 = False
    print(valor == valor2)

# 20. Escreva um programa que verifique se dois números fornecidos pelo usuário são diferentes.
def exercicio20():
    valor = True
    valor2 = False
    print(valor != valor2)
# #### try-except e if

# 21: Conversor de Temperatura
# 22: Verificador de Palíndromo
# 23: Calculadora Simples
# 24: Classificador de Números
# 25: Conversão de Tipo com Validação

if __name__ == "__main__":
    exercicio20()