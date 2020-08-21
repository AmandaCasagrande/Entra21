#"""Execicios 02
#Escreva um programa que receba 4 notas e calcule a média.
#Mostre a seguinte mensagem conforme a media final.
#Media Final
#de 0 a 5 - Reprovado
#de 5 a 6.5 - Recuperação
#de 6.5 a 9 - Aprovado
#Acima de 9 - Aprovado com louvor
#"""

nota1 = float(input("Nota 1: "))
nota2 = float(input("Nota 2: "))
nota3 = float(input("Nota 3: "))
nota4 = float(input("Nota 4: "))
print("\n")

mediaFinal = ((nota1 + nota2 + nota3 + nota4) / 4)

if (mediaFinal >= 0) and (mediaFinal <= 5):
    print("Reprovado.")
elif (mediaFinal > 5) and (mediaFinal <= 6.5):
    print("Recuperação")
elif (mediaFinal > 6.5) and (mediaFinal <= 9):
    print("Aprovado.")
elif (mediaFinal > 9.0):
    print("Aprovado com louvor!")