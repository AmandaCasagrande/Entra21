"""Exercicio 09
Faça um programa que pegue uma lista de valores e separe em 2 listas. Uma com valores menores que 500.00 e outra com maiores ou igual.
Depois motre o maior e o menor valor da cada lista.
vandas = [100.00, 500.00, 258.50, 710.00, 50.50,750.00, 10.00, 1050.00, 859.75, 199.05, 500.50,750.00, 568.60, 950.00, 950.00, 89.90, 2500.00, 1750.00,500.00]
"""

vendas = [100.00, 500.00, 258.50, 710.00, 50.50,750.00, 10.00, 1050.00, 859.75, 199.05, 500.50,750.00, 568.60, 950.00, 950.00, 89.90, 2500.00, 1750.00,500.00]
listaMaior = [ ]
listaMenor = [ ]

for i in range(len(vendas)):
    if ((vendas[i])  < 500):
        listaMenor.append(vendas[i])
        
    if ((vendas[i]) >= 500):
        listaMaior.append(vendas[i])

listaMenor.sort()
print("Lista 1: ", listaMenor) 
print(f"O menor valor é {listaMenor[0]} e o maior valor é {max(listaMenor)}.\n")
listaMaior.sort()
print("Lista 2: ", listaMaior)
print(f"O menor valor é {listaMaior[0]} e o maior valor é {max(listaMaior)}.")