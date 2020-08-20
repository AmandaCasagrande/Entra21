# Exercicio 13
# 
# Crie um programa que peça o nome do cliente, idade, endereço, email e telefone.
# 
# Depois crie um menu interativo com as seguintes opções: Dados, Endereço, Contato.
# 
# Se o usuário selecionar "Dados" deve aparecer o nome do cliente e a idade
# 
# Se o usuário selecionar "Endereço" deve aparecer o nome do cliente e o endereço
# 
# Se o usuário selecionar "Contato" deve aparecer o nome do cliente, email e o telefone


nomeCliente = str(input("Digite seu nome: "))
idadeCliente = str(input("Digite sua idade: "))
enderecoCliente = str(input("Digite seu endereço: "))
emailCliente = str(input("Digite seu email: "))
telefoneCliente = str(input("Digite seu telefone: "))

print("\n\n")

opcao = input("""Digite a opção: 
Dados
Endereço
Contato\n\n""")

if (opcao == 'Dados'): 
    print("Nome:", nomeCliente)
    print("Idade:", idadeCliente)
else:
    if (opcao == 'Endereço'):
        print("Nome:", nomeCliente)
        print("Endereço:", enderecoCliente)
    else:
        if (opcao == 'Contato'):
            print("Nome:", nomeCliente)
            print("E-mail:", emailCliente)
            print("Telefone:", telefoneCliente)

