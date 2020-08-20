# Exercicio 18
# Crie um programa que solicite o valores (inteiros) de a, b e c para o cálculo do delta
# 
# A fórmula do delta é:
# 
# delta = b²-4ac
# 
# após calcular, mostre o resultado na tela.

valorA = int(input("Digite o valor de 'A': "))
valorB = int(input("Digite o valor de 'B': "))
valorC = int(input("Digite o valor de 'C': "))

delta = (valorB * valorB) - (4 * valorA * valorB)

print("O valor de delta é ", delta)