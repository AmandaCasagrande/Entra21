  
"""Exercício 03
3.1) Crie um programa que cadastre o id, nome, sexo e a idade de 5 clientes.
3.2) Depois mostre os dados dos 5 clientes.
3.3) Peça para que o usuário escolha um id de um cliente e mostre as informações deste cliente.
3.4) Crie um filtro que ao digitar um id de um cliente mostre as seguintes informações:
- Para menores de 17 anos: Entrada Proibida
- Para maiores de 17 anos: Entrada Liberada
- Para o sexo Feminino: 50% de desconto
- Para o sexo Masculino: 5% de desconto
"""
idCliente = []
nomeCliente = []
sexoCliente = []
idadeCliente = []

print("""
_________________________________________________

***              C A D A S T R O              ***
_________________________________________________
""") 
for i in range (5):
    idCadastro = int(input(f"\nID: "))
    idCliente.append(idCadastro)

    nome = str(input(f"Nome: "))
    nomeCliente.append(nome)

    sexo = str(input(f"Sexo: "))
    while (sexo != 'F' and sexo != 'M'):
        print("ERRO! Digite novamente!")
        sexo = str(input(f"Sexo: "))
    sexoCliente.append(sexo)

    idade = int (input(f"Idade: "))
    idadeCliente.append(idade)

entrada = str(input("Deseja acessar os cadastros de clientes? (S/N) "))

if (entrada == 'S' or entrada == 's'):
    print("""
_________________________________________________

*** C L I E N T E S     C A D A S T R A D O S ***
_________________________________________________
    """) 

    tamanho = len(nomeCliente)      
    for i in range (tamanho):
        print(f"\nID Cliente:", idCliente[i])
        print("Nome:", nomeCliente[i])
        print(f"Sexo: ", sexoCliente[i])
        print(f"Idade: ", idadeCliente[i])
        print("_________________________________________________")
        
    escolhaID = input("\n\nDeseja pesquisar o ID de um cliente? (S/N) ")

    if (entrada == 'S' or entrada == 's'):
        print("""\n\n
_________________________________________________

***         P E S Q U I S A        I D        ***
_________________________________________________
        """) 

        idPesquisa = int(input("Digite o ID a ser pesquisado: "))

        localizado = False
        for i in range (len(idCliente)):
            if (idPesquisa == idCliente[i]):
                index = i
                localizado = True

        if (localizado):
            print("\nID Localizado: ", idCliente[index])
            print("Nome: ", nomeCliente[index])
            print("Sexo: ", sexoCliente[index])
            print("Idade: ", idadeCliente[index])

            if (idade <= 17):
                print(f"E N T R A D A    P R O I B I D A !")
            elif (idade > 17):
                print(f"E N T R A D A    P E R M I T I D A !")
                if (sexo == 'F'):
                    print("50%. de desconto!")
                elif (sexo == 'M'):
                    print("5 %. de desconto!")
        else:
            print("*** CADASTRO NÃO ENCONTRADO ***")
    else: 
        print("\n\n** F I M    D O    P R O G R A M A **")
elif (entrada == 'N' or entrada == 'n'):
    print("\n\n** F I M    D O    P R O G R A M A **")
else:
    print("""** E R R O ** 
MOTIVO: Entrada Inválida no sistema!""")

