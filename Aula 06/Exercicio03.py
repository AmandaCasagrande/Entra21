#""Execicios 03

#Escreva um programa que contenha um menu com 4 opções:
#A) soma
#B) média
#C) divisão
#D) Sair

#As opções podem ser escolhidas com as letras maiusculas ou minusculas.

#Para a opção soma, deve solicitar 2 números, fazer a soma e mostrar o resultado.

#Para a opção média, deve solicitar 4 números, fazer a média e mostrar os resultados.

#Para a opção divisão, deve solicitar 2 números, dividir o primeiro pelo segundo e montrar o resultado. Caso o segundo for igual a 0, então deve mostrar o a mensagem "Erro! Não pode dividir por ZERO!"

#Para a opção sair, deve aparecer a mensagem: "Muito Obrigado e Volte sempre!"

print("""
A) Soma
B) Média
C) Divisão
D) Sair""")

print("\n")
entrada = input("Digite sua opção: ")

if (entrada == 'A') or (entrada == 'a'):
    num1 =  float(input("Digite um número: "))
    num2 = float(input("Digite outro número: "))
    soma = num1 + num2 
    print("Soma = ", soma)

elif (entrada == 'B') or (entrada == 'b'):
    num1 = float(input("Digite um número: "))
    num2 = float(input("Digite outro número: "))
    num3 = float(input("Digite mais um número: "))
    num4 = float(input("Digite o último número: "))
    media = ((num1 + num2 + num3 + num4) / 4)
    print("Média = ", media)
    
elif (entrada == 'C') or (entrada == 'c'):
    num1 =  float(input("Digite um número: "))
    num2 = float(input("Digite outro número: "))
    divisao = num1/num2
    print("Divisão = ", divisao)
    print("Média = ", media)
    if (divisao == 0):
        print("Erro! Não pode dividir por ZERO!")

elif (entrada == 'D') or (entrada == 'd'):
    print("Muito obrigada e volte sempre!")
