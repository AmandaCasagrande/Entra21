n1, n2, n3 = input("").split()
n1 = float(n1)
n2 = float(n2)
n3 = float(n3)

perimetroTriangulo = n1 + n2 + n3
perimetroTriangulo = float(perimetroTriangulo)

areaTrapezio = ((n1 + n2) * n3) / 2
areaTrapezio = float(areaTrapezio)

if ((n2 - n3 < n1) and (n1 < n2 + n3)):
    print(f"Perímetro = {perímetro:.1f}")
elif (n1 - n3 < n2 and n2 < n1 + n3):
    print(f"Perímetro = {perímetro:.1f}")
elif (n1 - n2 < n3 and n3 < n1 + n2):
    print(f"Perímetro = {perímetro:.1f}")
else: 
    print(f"Área = {areaTrapezio:.1f}")

