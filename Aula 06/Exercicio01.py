#Execicios 01

#Escreva um programa que calcule a porcentagem de comissão de vendedores com as seguintes condições

#Venda Total
#de R$ 0.00 a R$ 30000.00 - 0%
#de R$ 30000.01 a R$ 50000.00 - 1.5%
#de R$ 50000.01 a R$ 100000.00 - 2.5%
#Acima de R$ 100000.00 - 3.5%

valorVenda = float(input("Digite o valor da venda para calcular a comissão: "))
if (valorVenda >= 0) and (valorVenda <= 30000):
    print("Sem comissão")
elif (valorVenda >= 30000.01) and (valorVenda <= 50000.00):
    comissao = valorVenda * (1.5/100)
    print("Comissão: ", comissao)
elif (valorVenda >= 50000.01) and (valorVenda <= 100000.00):
    comissao = valorVenda * (2.5/100)
    print("Comissão: ", comissao)
elif (valorVenda > 100000.00):
    comissao = valorVenda * (3.5/100)
    print("Comissão: ", comissao)