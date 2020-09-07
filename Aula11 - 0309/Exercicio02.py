"""Exercício 2

(não usar o continue ou o break)

Crie um menu interativo com as seguintes opções:

A) soma
B) Média
C) Tabuada
S) Sair


Para A: Peça 2 números, some e mostr o resultado
Para B: Peça 4 números, faça a média e mostre o resultado
Para C: Peça um número e mostre a tabuada dele
Para S: Mostre uma mensagem de despidida e encerre o programa.
Para qualquer outro valor: Mostre a mensagem "opção inválida"""

print("""
_________________________________________________

***                   MENU                    ***
_________________________________________________

[A] Soma
[B] Média
[C] Tabuada
[S] Sair do Programa
_________________________________________________""")

entrada = str(input("Qual opção deseja acessar? "))

while (entrada != 'A' and entrada != 'B' and entrada != 'C' and entrada != 'S'):
    entrada = input("Entrada Inválida. Tente novamente: ")

while (entrada == 'A' or entrada == 'B' or entrada == 'C'):

    if (entrada == 'A'):
        num1 = float(input("\nDigite um número: "))
        num2 = float(input("Digite outro número: "))
        print (f"\nResultado da Soma  = ", num1 + num2)

    elif (entrada == 'B'):
        print("Digite 4 números para calcular a média: ")
        soma = 0
        for i in range (4):
            soma = soma + float(input(""))
        print (f"\nResultado da Média = ", (soma/4))

    elif (entrada == 'C'):
        num = int(input("Digite um número para calcular a tabuada: "))
        for i in range (1, 11):
            print(i, "x", num, "=", i * num)

    print("_________________________________________________")
    entrada = str(input("\nQual opção deseja acessar? "))

    while (entrada != 'A' and entrada != 'B' and entrada != 'C' and entrada != 'S'):
        entrada = input("Entrada Inválida. Tente novamente: ")

print("""
_________________________________________________

***             FIM DO PROGRAMA               ***
_________________________________________________
""")