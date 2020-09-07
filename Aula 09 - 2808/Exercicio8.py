"""Exercicio 08
Faça um programa que pegue a lista e calcule a seguinte formula: 32x+125
Com o resultado desta formula mostre sómente os resultados maiores que 550. Para os resultados menores que 550 mostre "número invalido!"
lista = [1, 6, 9, 1, 5, 4, 8, 9, 15, 23, 14, 54, 82, 91, 45]
"""
lista = [1, 6, 9, 1, 5, 4, 8, 9, 15, 23, 14, 54, 82, 91, 45]

for i in range (len(lista)):
    formula = 32 * lista[i] + 125
    if (formula > 550):
        print(f"Resultado de (32 * {i} + 125) = ", formula)
    else:
        print("Número Inválido! O resultado é menor que 500!")