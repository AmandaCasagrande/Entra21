cedulas = float(input(""))

notas100 = int(cedulas / 100)
cedulas = cedulas % 100

notas50 = int(cedulas / 50)
cedulas = cedulas % 50

notas20 = int(cedulas / 20)
cedulas = cedulas % 20

notas10 = int(cedulas / 10)
cedulas = cedulas % 10

notas5 = int(cedulas / 5)
cedulas = cedulas % 5

notas2 = int(cedulas / 2)
cedulas = cedulas % 2

notas1 = int(cedulas / 1)

print(f"NOTAS:")
print(f"{notas100} de R$ 100.00")
print(f"{notas50} de R$ 50.00")
print(f"{notas20} de R$ 20.00")
print(f"{notas10} de R$ 10.00")
print(f"{notas5} de R$ 5.00")
print(f"{notas2} de R$ 2.00")
print(f"{notas1} de R$ 1.00")

moedas1 = int(cedulas / 1.0)
cedulas = cedulas % 1.0

moedas50 = int(cedulas / 0.50)
cedulas = cedulas % 0.50

moedas25 = int(cedulas / 0.25)
cedulas = cedulas % 0.25

moedas10 = int(cedulas / 0.10)
cedulas = cedulas % 0.10

moedas05 = int(cedulas / 0.05)
cedulas = cedulas % 0.05

moedas01 = int(cedulas / 0.01)
cedulas = cedulas % 0.01


print(f"MOEDAS:")
print(f"{moedas1} moeda(s) de R$ 1.00")
print(f"{moedas50} moeda(s) de R$ 0.50")
print(f"{moedas25} moeda(s) de R$ 0.25")
print(f"{moedas10} moeda(s) de R$ 0.10")
print(f"{moedas05} moeda(s) de R$ 0.05")
print(f"{moedas01} moeda(s) de R$ 0.01")
