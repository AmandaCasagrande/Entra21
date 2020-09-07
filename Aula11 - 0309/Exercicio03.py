"""Exercício 3
(use somente o while)
Faça um programa que peça o nome e a idade do cliente e mostre a seguinte mensagem:
Para mairores de 18 anos: Entrada Permitida
Para menores de 18 anos: Entrada proibida.
Depois mostre a lista dos nomes (somente os nomes) das pessoas com entrada permitida.
Regras:
- O programa não pode aceitar nomes em branco. Caso não se digite um nome o programa deve mostrar a mensagem "Nome em branco" e repetir o código.
- Caso o usuário deixe em branco a idade, o progama deve mostrar uma mensagem: "Obrigado pela preferência" e terminar logo em seguida.
"""
listaNome = []
listaIdade = []

print("""
_________________________________________________

***                   MENU                    ***
_________________________________________________

*   Digite a idade '0' caso queira finalizar    *
_________________________________________________
""")

#Inicia a idade para entrar no loop pela primera vez
idadeCliente = 1

# Considera que o usuario "deixe em branco a idade" quando ele digitar 0
while (idadeCliente != 0):
    nomeCliente = str(input("Digite o nome do(a) cliente: "))

    # Considera nome em branco como sem informação, usuário só tecla enter
    while (nomeCliente == ""):
        nomeCliente = str(input("Nome em branco! Digite o nome do(a) cliente: "))

    listaNome.append(nomeCliente)
    idadeCliente = int(input("Digite a idade do(a) cliente: ")) 

    if (idadeCliente != 0):
        listaIdade.append(idadeCliente)

        if (idadeCliente >= 18):
            print("Entrada Permitida!\n")
        else: 
            print("Entrada Proibida!\n")

print("""
_________________________________________________

***   C L I E N T E S      L I B E R A D O S  ***
_________________________________________________
""") 
for i in range(len(listaIdade)):
    if (listaIdade[i] >= 18):
        print(listaNome[i])

print("\nObrigado pela preferência!")