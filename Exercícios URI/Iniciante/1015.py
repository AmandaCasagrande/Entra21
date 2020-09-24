entrada1 = input().split(" ")
x1, y1 = entrada1
entrada2 = input().split(" ")
x2, y2 = entrada2

x1 = float(x1)
y1 = float(y1)
x2 = float(x2)
y2 = float(y2)

distancia = ((x2-x1)**2.0) + ((y2-y1)**2.0)
raiz = distancia**(0.5)

print(f"{raiz:.4f}")
