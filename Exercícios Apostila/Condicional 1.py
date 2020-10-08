'''
1. Escreva um programa que, dados 2 números diferentes (a e b), encontre o menor deles.
'''

a = int(input("Digite valor de A: "))
b = int(input("Digite valor de B: "))

if (a > b):
    print(f"A é maior que b!")
elif (a == b):
    print(f"A e B são iguais.")
else:
    print(f"B é maior que A!")
