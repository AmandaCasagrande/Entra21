"""Exercício 1
(não usar o continue ou o break)
Crie um programa que mostre um menu com as seguites opções:
1) Soma
2) Subtração
3) Multiplicação
S) Para sair!
Para número 1: Peça 2 números e mostre a soma deles
Para número 2: Peça 2 números e mostre a subtração deles
Para número 3: Peça 2 números e mostre a multiplicação deles
Para S: Mostre uma mensagem de despedida e termine o programa.
Para qualquer outra opção deve aparecer a mensagem "Opção Inválida"
"""

print("""
_________________________________________________

***                   MENU                    ***
_________________________________________________

[1] Soma
[2] Subtração
[3] Multiplicação
[S] Sair do Programa
_________________________________________________""")

entrada = str(input("Qual opção deseja acessar? "))

while (entrada != '1' and entrada != '2' and entrada != '3' and entrada != 'S'):
    entrada = str(input("Entrada Inválida. Tente novamente: "))

while (entrada == '1' or entrada == '2' or entrada == '3'):

    if (entrada == '1'):
        num1 = float(input("\nDigite um número: "))
        num2 = float(input("Digite outro número: "))
        print (f"\nResultado da Soma  = ", num1 + num2)
    elif (entrada == '2'):
        num1 = float(input("\nDigite um número: "))
        num2 = float(input("Digite outro número: "))
        print (f"\nResultado da Subtração = ", num1 - num2)
    elif (entrada == '3'):
        num1 = float(input("\nDigite um número: "))
        num2 = float(input("Digite outro número: "))
        print (f"\nResultado da Multiplicação = ", num1 * num2)
    
    print("_________________________________________________")
    entrada = str(input("\nQual opção deseja acessar? "))

    while (entrada != '1' and entrada != '2' and entrada != '3' and entrada != 'S'):
        entrada = str(input("Entrada Inválida. Tente novamente: "))

print("""
_________________________________________________

***             FIM DO PROGRAMA               ***
_________________________________________________
    """)
    