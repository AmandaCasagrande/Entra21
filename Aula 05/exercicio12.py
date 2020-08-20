# Exercicio 12
# 
# Crie um programa que peça 2 números.
# 
# Depois mostre um menu interativo contendo 5 operações matemáticas do python
# (adição, subtração, multiplicação, divisão e expoente)
# 
# Peça para o usuário escolher uma destas opções e mostre o resultado da operação escolhida.

num1 = int(input("Digite um número: "))
num2 = int(input("Digite outro número: "))
print("\n")

adicao = num1 + num2
subtracao = num1 - num2
multiplicacao = num1 * num2
divisao = num1/num2
expoente = num1 ** num2

print("Adição: ", adicao)
print("Subtração: ", subtracao)
print("Multiplicação: ", multiplicacao)
print("Divisão: ", divisao)
print("Expoente: ", expoente)
