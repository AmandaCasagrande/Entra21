# Exercicio 16
# 
# Crie um programa para uma promoção de um posto de combustivel.
# 
# O programa deve pedir ao usuário quantos litros ele quer abastecer e qual combustivel: álcool, diessel ou gasolina
# 
# A promoção é a seguinte:
#  - Para gasolina: Até 20 litros 0% de desconto e acima de 20 litros 10% de desconto
#  - Para diessel: Até 10 litro 1.5% de desconto e acima de 10 litros 5% de desconto
#  - para álcool: Até 10 litros 5% de desconto e acima de 10 litros 10% de desconto.
#  
# Mostre o combustivel que ele selecionou, o total abastecido e a porcentagem de desconto a ser aplicada.
# 
# Não precisa calcular o valor do combustivel!
# 
print("Bem-vindo(a) ao posto de combustível Entra21!")
print("\n\n")

combutivel = str(input(""""Digite '1' para Álcool
'2' para Diessel ou
'3' para Gasolina:  """))
print("\n")

litros = float(input("Quantos litros? "))
print("\n\n")

if(combutivel == '3') and (litros <= 20.0):
    print("Combustível: Gasolina")
    print("Total abastecido: ", litros)
    print("Desconto aplicado: 0%")

if(combutivel == '3') and (litros > 20.0):
    print("Combustível: Gasolina")
    print("Total abastecido: ", litros)
    print("Desconto aplicado: 10%")

if(combutivel == '2') and (litros <= 10.0):
    print("Combustível: Diessel")
    print("Total abastecido: ", litros)
    print("Desconto aplicado: 1.5%")

if(combutivel == '2') and (litros > 10.0):
    print("Combustível: Diessel")
    print("Total abastecido: ", litros)
    print("Desconto aplicado: 5%")

if(combutivel == '1') and (litros <= 10.0):
    print("Combustível: Álcool")
    print("Total abastecido: ", litros)
    print("Desconto aplicado: 5%")

if(combutivel == '1') and (litros > 10.0):
    print("Combustível: Álcool")
    print("Total abastecido: ", litros)
    print("Desconto aplicado: 10%")
