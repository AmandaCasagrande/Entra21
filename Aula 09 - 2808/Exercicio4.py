"""Exercicio 04
Faça um programa de cadastro de pessoas que receba 10 nomes, idades e e-mails e salve cada um em uma lista.
Depois mostre as listas separadamente 
(print (lista) já é o suficiente)
"""

nomesCadastro = [ ]
idadesCadastro = [ ]
emailCadastro = [ ]

for i in range(10): 
    nome = str (input(f"Nome {i+1}: "))
    nomesCadastro.append(nome)

    idade = int (input(f"Idade {nome}: "))
    idadesCadastro.append(idade)

    email = str (input(f"Email {nome}: "))
    emailCadastro.append(email)

print ("\nNomes Cadastrados:", nomesCadastro)
print ("Idades Cadastradas:", idadesCadastro)
print ("E-mails Cadastrados:", emailCadastro)