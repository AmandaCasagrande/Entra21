# Exercicio 9
# Faça um programa que peça 3 números inteiros e mostre o os tês em ordem crescente.
# 
# 
num1 = int(input("Digite um número: "))
num2 = int(input("Digite outro número: "))
num3 = int(input("Digite mais um número: "))

if (num1 <= num2) and (num2 <= num3):
    print(num1, num2, num1)
elif (num1 <= num3) and (num3 <= num2):
    print(num1, num3, num2)
elif (num2 <= num1) and (num1<= num3): 
    print(num2, num1, num3)
elif (num2 <= num3) and (num3 <= num1):
    print(num2, num3, num1)
elif (num3 <= num1) and (num1 <= num2):
    print(num3, num1, num2)
elif (num3 <= num2) and (num2 <= num1):
    print(num3, num2, num1)
