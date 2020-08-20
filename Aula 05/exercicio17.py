# Exercicio 17
# crie um programa que peça 4 notas de um aluno e calcule a média "(nota1+nota2+nota3+nota4)/4" e retorne:
# 
# Pra média igual a 10 apareça a mensagem "Aprovado com louvor"
# Pra média maior igual a 7 apareça a mensagem "Aprovado"
# Pra média menor que 7 apareça a mensagem "Reprovado"
# 
print("Digite as notas do aluno(a): \n")
nota1 = float(input("Nota 1: "))
nota2 = float(input("Nota 2: "))
nota3 = float(input("Nota 3: "))
nota4 = float(input("Nota 4: "))
print("\n")

mediaNotas = ((nota1 + nota2 + nota3 + nota4) / 4)

print("Média: ", mediaNotas)
if (mediaNotas == 10):
    print("Aprovado(a) com louvor!")
if (mediaNotas >= 7.0):
    print("Aprovado(a)!")
if (mediaNotas < 7.0):
    print("Reprovado.")
