
"""Exercicio 06
Faça um programa que peça ao usuário que digite o nome de 10 pessoas. Depois mostre cada nome em linhas separadas.
"""
nomeLista = []
for i in range (10):
    nome = str (input(f"Nome: "))
    nomeLista.append(nome)
print("\n")
for n in range (10):
    print("Nome: ", nomeLista[n])
    

