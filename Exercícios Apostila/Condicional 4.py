'''
5. Leia um número e imprima a raiz quadrada do número caso ele seja positivo ou igual a zero e o quadrado do
número caso ele seja negativo.
'''
import math
a = int(input("Digite valor de A: "))
if (a >= 0):
    print(f"Raiz quadrada de {a} ", math.sqrt(a))
elif (a < 0):
    print(f"{a} ao quadrado é -",(a**2))
