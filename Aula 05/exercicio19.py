# Exercicio 19
# Faça um programa para calcular a fórmula do bhaskara para equação de segundo grau: ax²+bx+c
# 
# Peça para o usuário digitar os valores de a, b e c
# 
# Calcule o delta "delta = (b**2)-(4*a*c)"
# 
# Se o delta der negativo, então deve aparecer a seguinte mensagem: "Delta negativo! Equação não pode ser resolvida!"
# 
# Se o delta for igual a zero, use esta fórmula "x=-b/(2*a)" e mostre o valor de x
# 
# Se delta for maior que zero, então use estas 2 fórmulas "x =(-b+(delta**(1/2)))/(2*a)" e "x2=(-b-(delta**(1/2)))/(2*a)"
# e mostre o os valores de x1 e x2  
#     
#     
# ________________
# Nota: 
# Para testar se seu programa está certo use estes valores para a, b e c
# delta negativo a=1, b=1, c=1
# delta zero a=1, b=2, c=1
# delta positivo a=1, b=4, c=1

valorA = int(input("Valor de A: "))
valorB = int(input("Valor de B: "))
valorC = int(input("Valor de C: "))
print("\n")

calculoDelta = ((valorB ** 2) - (4 * valorA * valorC))

if (calculoDelta < 0):
    print("Delta negativo! Equação não pode ser resolvida!")
if (calculoDelta == 0):
    valorX = (-valorB / (2 * valorA))
    print("Valor de 'x' =", valorX)
if (calculoDelta > 0):
    print("A equação pode ser resolvida!")
    valorX = ((-valorB + (calculoDelta ** (1/2))) / (2 * valorA))
    valorX_2 = ((-valorB - (calculoDelta ** (1/2))) / (2 * valorA))
    print("Valor de x¹ = ", valorX)
    print("Valor de x² = ", valorX_2)