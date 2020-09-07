"""
Exercício 01

Crie um programa que cadastre 5 clientes. 

Cada cliente possui: Nome, sexo, Telefone
(Guarde estes dados em listas separadas).

Depois mostre os dados cadastrados no seguinte formato:



***********************************
Relatório de clientes cadastrados 
***********************************
Nome: 
Sexo:
Telefone:
***********************************
"""

nomeCadastro = []
sexoCadastro = []
telefoneCadastro = []

print("""
_________________________________________________

***              C A D A S T R O              ***
_________________________________________________
""") 

for i in range (5):
    nome = str(input(f"\nNome {i + 1}: "))
    nomeCadastro.append(nome)

    sexo = str(input(f"Sexo: "))
    sexoCadastro.append(sexo)

    telefone = str(input(f"Telefone: "))
    telefoneCadastro.append(telefone)

tamanho = len(nomeCadastro)

print("""
________________________________________

**         R E L A T Ó R I O         **
________________________________________
""") 
for i in range (tamanho):
    print("\nNome:", nomeCadastro[i])
    print("Sexo: ", sexoCadastro[i])
    print("Telefone: ", telefoneCadastro[i])
    print("________________________________________")
