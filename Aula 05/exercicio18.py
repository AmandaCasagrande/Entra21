# Exercicio 18
# Peça para o usuário digitar os valores de a, b e c
# 
# Calcule o delta "delta = (b**2)-(4*a*c)"
# 
# Se o delta der negativo, então deve aparecer a seguinte mensagem: "Delta negativo! Equação não pode ser resolvida!"
# 
# Se o delta der igual a zero, então deve aparecer a seguinte mensagem: "Delta igual a zero!"
# 
# Se o delta der positivo, então deve aparecer a seguinte mensagem: "A equação pode ser resolvida!"

valorA = int(input("Valor de A: "))
valorB = int(input("Valor de B: "))
valorC = int(input("Valor de C: "))
print("\n")

calculoDelta = ((valorB ** 2) - (4 * valorA * valorC))

if (calculoDelta < 0):
    print("Delta negativo! Equação não pode ser resolvida!")
if (calculoDelta == 0):
    print("Delta igual a zero!")
if (calculoDelta > 0):
    print("A equação pode ser resolvida!")