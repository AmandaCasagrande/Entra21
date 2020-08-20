
# Exercicio 9
# Faça um programa que peça o nome do cliente, a quantidade do produto (inteiro) e o preço (float).
# 
# Mostre o nome do cliente e o valor total da venda.

nomeCliente = input("Digite o seu nome: ")
qntProduto = int(input("Qual a quantidade de produtos? "))
precoProduto = float(input("Qual o valor do produto? "))
valorVenda =  (qntProduto * precoProduto)

print("\n")

print("Nome: ", nomeCliente)
print("Valor total: R$", valorVenda)



