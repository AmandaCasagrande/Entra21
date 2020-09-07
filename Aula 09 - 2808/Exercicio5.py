"""Exercicio 05
Faça um programa que peça ao usuário digitar a quantidade de vendas do dia. 
Cadastre cada venda separadaemnte e depois mostre a média e o valor total vendido no dia.
"""
produtoCadastro = [ ] 
valorCadastro = [ ]
qntd =  int (input(f"Digite a quantidade de vendas do dia: "))

for i in range(qntd): 
    nome = str (input(f"Produto {i+1}: "))
    produtoCadastro.append(nome)
    valor = float (input(f"Preço de {nome}: "))
    valorCadastro.append(valor)

media = sum(valorCadastro) / qntd
print("\nA média de vendas é ", media, "reais.")
print("O valor total vendindo no dia é de ", sum(valorCadastro), "reais.")