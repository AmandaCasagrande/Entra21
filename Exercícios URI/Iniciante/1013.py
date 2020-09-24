entrada = input("").split()
valorA, valorB, valorC = entrada
valorA = int(valorA)
valorB = int(valorB)
valorC = int(valorC)

maiorAB = (valorA + valorB + (abs(valorA - valorB))) / 2.0
maiorAC = (maiorAB + valorC + (abs(maiorAB - valorC))) / 2.0

maiorAB = int(maiorAB)
maiorAC = int(maiorAC)

print(f"{maiorAC} eh o maior")
