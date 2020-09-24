entrada1 = input("").split()
cod1, qntd1, valor1 = entrada1
cod1 = float(cod1)
qntd1 = float(qntd1)
valor1 = float(valor1)
entrada2 = input("").split()
cod2, qntd2, valor2 = entrada2
cod2 = float(cod2)
qntd2 = float(qntd2)
valor2 = float(valor2)
soma = (valor1 * qntd1) + (valor2 * qntd2)
print(f"VALOR A PAGAR: R$ {soma:.2f}")
