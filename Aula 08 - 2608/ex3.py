# 3) Estas 3 listas:
# vendas_armando = [100.00, 500.00, 258.50, 710.00, 50.50,750.00 ]
# vendas_eduardo = [10.00, 1050.00, 859.75, 199.05, 500.50,750.00, 568.60, 950.00 ]
# vendas_paulo = [950.00, 89.90, 2500.00, 1750.00,500.00]
# 
# Estas listas são referente as vendas dos vendedores Armando, Paulo e Eduardo.
# 
# 3.1) Com base nelas e usando funções da lista mostradas em aula, mostre:
# A média de vendas de cada um;
# A venda total de cada vendedor;
# A quantidade de vendas de cada vendedor.
# 
# 3.2) Calcule o valor de comissão que o dono da loja deve pagar para seus funcionários seguindo a regra:
# 
# Para total de vendas de 0.00 a 1000.00 Reais - 1%
# Para total de vendas de 1000.01 a 2500.00 Reais - 1.5%
# Para total de vendas de 2500.01 a 5000.00 Reais - 2%
# Para total de vendas a cima de 5000.01 Reais - 3%

vendasArmando = [100.00, 500.00, 258.50, 710.00, 50.50, 750.00]
totalVendas_A = sum(vendasArmando)
itensArmando = len(vendasArmando)
print("Armando: ", "\nMédia: R$", (totalVendas_A / itensArmando), "\nTotal: R$", totalVendas_A, "\nQuantidade de itens: ", itensArmando)

if (totalVendas_A > 0 and totalVendas_A <= 1000):
    comissao = totalVendas_A * (1/100)
    print("Comissão Armando: R$", comissao)
elif (totalVendas_A > 1000 and totalVendas_A <= 2500):
    comissao = totalVendas_A * (1.5/100)
    print("Comissão Armando: R$", comissao)
elif (totalVendas_A > 2500 and totalVendas_A <= 5000):
    comissao = totalVendas_A * (2/100)
    print("Comissão Armando: R$", comissao)
elif (totalVendas_A > 5000):
    comissao = totalVendas_A * (3/100)
    print("Comissão Armando: R$", comissao)

vendasEduardo = [10.00, 1050.00, 859.75, 199.05, 500.50,750.00, 568.60, 950.00]
totalVendas_E = sum(vendasEduardo)
itensEduardo = len(vendasEduardo)

print("\n\nEduardo: ", "\nMédia: R$ %2.f" % (totalVendas_E / itensEduardo), "\nTotal: R$", totalVendas_E, "\nQuantidade de itens: ", itensEduardo)

if (totalVendas_E > 0 and totalVendas_E <= 1000):
    comissao = totalVendas_E * (1/100)
    print("Comissão Eduardo: R$", comissao)
elif (totalVendas_E > 1000 and totalVendas_E <= 2500):
    comissao = totalVendas_E * (1.5/100)
    print("Comissão Eduardo: R$", comissao)
elif (totalVendas_E > 2500 and totalVendas_E <= 5000):
    comissao = totalVendas_E * (2/100)
    print("Comissão Eduardo: R$", comissao)
elif (totalVendas_E > 5000):
    comissao = totalVendas_E * (3/100)
    print("Comissão Eduardo: R$", comissao)

vendasPaulo = [950.00, 89.90, 2500.00, 1750.00,500.00]
totalVendas_P = sum(vendasPaulo)
itensPaulo = len(vendasPaulo)

print("\n\nPaulo: ", "\nMédia: R$ %2.f" % (totalVendas_P / itensPaulo), "\nTotal: R$", totalVendas_P, "\nQuantidade de itens: ", itensPaulo)

if (totalVendas_P > 0 and totalVendas_P <= 1000):
    comissao = totalVendas_P * (1/100)
    print("Comissão Paulo: R$", comissao)
elif (totalVendas_P > 1000 and totalVendas_P <= 2500):
    comissao = totalVendas_P * (1.5/100)
    print("Comissão Paulo: R$", comissao)
elif (totalVendas_P > 2500 and totalVendas_P <= 5000):
    comissao = totalVendas_P * (2/100)
    print("Comissão Paulo: R$", comissao)
elif (totalVendas_P > 5000):
    comissao = totalVendas_P * (3/100)
    print("Comissão Paulo: R$", comissao)