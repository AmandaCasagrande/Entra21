"""Exercicio 03
Faça um programa que peça 10 notas do aluno. Faça a média e mostre as seguintes mensagens:
Para 7 a 10 - Aprovado
Para 5.5 a 7 - Recuperação 
Para menor de 5.5 - Reprovado
"""

notasAlunos = [ ]

for i in range(10): 
    nota = float (input(f"Nota {i+1}: "))
    notasAlunos.append(nota)

media = sum(notasAlunos) / len( notasAlunos )
print("A média do aluno (a) é ", media)

if (media >= 7 and media <= 10):
    print("Parabéns, aprovado(a)!")
elif (media >= 5.5 and media < 7): 
    print("Recuperação.")
elif (media < 5.5): 
    print("Reprovado.")
