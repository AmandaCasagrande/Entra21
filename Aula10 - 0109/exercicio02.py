"""Exercício 02
O id de um cliente é um código único (só aquela pessoa tem) composto por números inteiros que inicia do número 1 e vai aumentando de 1 em 1 enquanto for necessário.
Exemplo:
id: 1
Nome: Dudu
id: 2
Nome: Marta
id: 3
Nome: Pedro
ATENÇÃO!!!!
O id é um número atribuido automáticamente! O cliente não escolhe o número. O seu programa deve fazer o cadastro deste id automaticamente.
Com isso, crie um cadastro de clientes que receba o id, nome e idade. Depois mostre os dados dos clientes individualmente.
(cadastre no minimo 4 clientes)
"""
nomeCliente = []
idCliente = []

print("""
_________________________________________________

***              C A D A S T R O              ***
_________________________________________________
""")

qtdCadastro = int (input("Quantos clientes deseja cadastrar? "))

for i in range (qtdCadastro):
    idAutomatico = i + 1
    print ("ID: ", idAutomatico)
    idCliente.append(idAutomatico)
    nome = input(f"Nome: ")
    nomeCliente.append(nome)


entrada = str (input("Deseja acessar os cadastros de clientes? (S/N) "))

if (entrada == 'S' or entrada == 's'):
    print("""
_________________________________________________

*** C L I E N T E S     C A D A S T R A D O S ***
_________________________________________________
    """) 

    tamanho = len(nomeCliente)
    for i in range (tamanho):
        print(f"ID Cliente: {idCliente[i]}")
        print("\nNome:", nomeCliente[i])
        print(" _________________________________________________")
elif (entrada == 'N' or entrada == 'n'):
    print("\n\n** F I M    D O    P R O G R A M A **")
else:
    print("""       ** E R R O ** 
        MOTIVO: Entrada Inválida no sistema!""")
