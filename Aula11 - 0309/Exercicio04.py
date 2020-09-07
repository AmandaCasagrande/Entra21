"""Exercício 4
(use o conhecimento que foi passado no curso)
Crie um programa com um menu interativo:
-----
Cadastro de pessoas v1.0
A) Cadastrar Pessoa
B) Ver todos os nomes cadastrados:
C) Ver cadastro pelo nome:
D) Apagar um cadastro pelo nome:
S) Sair
-----
Para A: Cadastre os dados do cliente (Nome, idade, sexo, telefone
Para B: Mostre todos os nomes dos clientes (só os nomes)
Para C: Digite o nome do cliente e mostre todos os dados dele.
Para D: Digite o nome do cliente e o apague do cadastro
Para S: Mostre uma mensagem de despedida e termine o programa
Para qualquer outro valor: Mostre "Opção invalida"
"""
nomeCliente = []
idadeCliente = []
sexoCliente = []
telefoneCliente = []

print("""
_________________________________________________

***                    MENU                   ***
_________________________________________________

[A] Cadastrar Pessoa
[B] Ver todos os nomes cadastrados
[C] Ver cadastro pelo nome
[D] Apagar um cadastro pelo nome
[Sair] Sair
""")

opcao = str(input("Digite a opção desejada: "))

while (opcao != 'A' and opcao != 'B' and opcao != 'C' and opcao != 'D' and opcao != 'Sair'):
    opcao = input("Opção inválida! Digite novamente: ")

while (opcao == 'A' or opcao == 'B' or opcao == 'C' or opcao == 'D'):

    if (opcao == 'A'):
        print("""
_________________________________________________

***                 CADASTRO                  ***
_________________________________________________
        """)

        nome = str(input(f"Nome: "))
        nomeCliente.append(nome)

        idade = int(input(f"Idade: "))
        idadeCliente.append(idade)

        sexo = str(input(f"Sexo: "))
        sexoCliente.append(sexo)

        telefone = str(input(f"Telefone: "))
        telefoneCliente.append(telefone)

    if (opcao == 'B'):
        print("""
_________________________________________________

***             NOMES CADASTRADOS             ***
_________________________________________________
        """)
    
        for i in range(len(nomeCliente)):
            print("Nome ", i + 1, ":", nomeCliente[i])
    
    if (opcao == 'C'):
        print("""
_________________________________________________

***              PESQUISA POR NOME            ***
_________________________________________________
        """)
        pesquisaNome = str(input("Digite o nome a ser pesquisado: "))
        index = nomeCliente.index(pesquisaNome)
        print(f"Cliente pesquisado: ", nomeCliente[index])
        print(f"Idade: ", idadeCliente[index])
        print(f"Sexo: ", sexoCliente[index])
        print(f"Telefone: ", telefoneCliente[index])

    if (opcao == 'D'):
        print("""
_________________________________________________

***             DELETAR CADASTRO              ***
_________________________________________________
        """)
        deletarNome = str(input("Digite o nome a ser deletado: "))
        nomeCliente.remove(deletarNome)
        print("O cadastro de ", deletarNome, "foi apagado.")

    print("""
_________________________________________________

***                    MENU                   ***
_________________________________________________

[A] Cadastrar Pessoa
[B] Ver todos os nomes cadastrados
[C] Ver cadastro pelo nome
[D] Apagar um cadastro pelo nome
[Sair] Sair
    """)

    opcao = str(input("Digite a opção desejada: "))

    while (opcao != 'A' and opcao != 'B' and opcao != 'C' and opcao != 'D' and opcao != 'Sair'):
        opcao = input("Opção inválida! Digite novamente: ")

print("""
_________________________________________________

***         OBRIGADA! FIM DO PROGRAMA         ***
_________________________________________________
""")