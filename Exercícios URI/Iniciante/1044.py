valorA, valorB = input("").split()
valorA = int(valorA)
valorB = int(valorB)

resto1 = valorA % valorB
resto2 = valorB % valorA

if (resto1 == 0 or resto2 == 0):
    print(f"Sao Multiplos")
else:
    print(f"Nao sao Multiplos")
