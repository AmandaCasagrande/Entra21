# Exercicio 10
# Faça um programa que peça o nome de 2 produtos, a quantidade comprada de cada produto (inteiro) e o valor (float) de cada um.
# 
# Mostre o nome a quantidade, preço por unidade e o total de cada produto.

produto1 = input("Digite o nome do produto 1: ")
qntd_Produto1 = int(input("Quantidade Produto 1: "))
valor_Produto1 = float(input("Valor Produto 1: "))
valorTotal_1 = (qntd_Produto1 * valor_Produto1)

print("\n")

produto2 =  input("Digite o nome do produto 2: ")
qntd_Produto2 = int(input("Quantidade Produto 2: "))
valor_Produto2 = float(input("Valor Produto 2: "))
valorTotal_2 = (qntd_Produto2 * valor_Produto2)

print("\n\n")

print("Nome: ", produto1)
print("Quantidade: ", qntd_Produto1)
print("Preço por unidade: ", valor_Produto1)
print("Valor total: ",valorTotal_1 )

print("\n")

print("Nome: ", produto2)
print("Quantidade: ", qntd_Produto2)
print("Preço por unidade: ", valor_Produto2)
print("Valor total: ",valorTotal_2)

print("\n\n")