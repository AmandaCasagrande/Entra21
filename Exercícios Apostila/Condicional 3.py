'''
4. Leia dois números e efetue a adição. Caso o valor somado seja maior que 20, este deverá ser apresentado
somando-se a ele mais 8; caso o valor somado seja menor ou igual a 20, este deverá ser apresentado subtraindose 5.

'''

a, b = input("Digite o valor de A e B, respectivamente: ").split()
a = int(a)
b = int(b)
soma = a + b
if (soma > 20):
    print(f"", (soma + 8))
elif (soma <= 20):
    print(f"", (soma - 5))
    