#--- Exercício 2  - Funções
#--- Escreva uma função para cadastro de endereço:
#---       a função deve receber sete parâmetros, id da pessoa, rua, numero, complemento, bairro, cidade e estado
#---       a função deve salvar os dados de endereço em uma lista com escopo global
#---       a função deve permitir o cadastro apenas de endereços com todos os dados preenchidos
#---       a função deve retornar uma mensagem ao final de acordo com a situação
#--- A função deve ser salva em um arquivo diferente do arquivo principal onde será chamada
#--- Exercício 4  - Funções
#--- Escreva uma função para listar endereços cadastrados:
#---    a função deve retornar todos os endereços cadastrados na função do ex2
#--- Escreva uma função para exibir um endereço específico:
#        a função deve retornar um endereço cadastrado na função do ex2 filtrando por 
#            id da pessoa

from Ex1 import cadastro_Pessoa

enderecos = []
id_pessoa = 0

def cadastro_Endereco(rua, numero, comp, bairro, cidade, estado):
    global id_pessoa
    id_pessoa += 1
    endereco = {"id_pessoa": id_pessoa}
    endereco['rua'] = rua
    endereco['numero'] = numero
    endereco['comp'] = comp
    endereco['bairro'] = bairro
    endereco['cidade'] = cidade
    endereco['estado'] = estado
    
    #Gera arquivo txt
    cadastro = {"rua": rua, "numero": numero, "comp": comp, "bairro": bairro, "cidade": cidade, "estado": estado}
    arq_Enderecos = open('cadastro.txt', 'a')
    arq_Enderecos.write(f"\n\nEndereço: {cadastro['rua']}, {cadastro['numero']} {cadastro['comp']}\nBairro: {cadastro['bairro']}\nCidade: {cadastro['cidade']} - {cadastro['estado']}")
    arq_Enderecos.close()

    enderecos.append(endereco)
    return id_pessoa

def mostrar_Endereco():
    for i in enderecos:
        print(f"ID: {i['id_pessoa']}")
        print(f"Rua: {i['rua']}")
        print(f"Número: {i['numero']}")
        print(f"Complemento: {i['comp']}")
        print(f"Bairro: {i['bairro']}")
        print(f"Cidade: {i['cidade']}")
        print(f"Estado: {i['estado']}")

def pesquisa_Endereco():
    endereco_especifico = int(input("Insira o ID do endereço a ser pesquisado: "))
    if id_pessoa == endereco_especifico:
        arq_Pessoa = open('cadastro.txt', 'r')
        for i in arq_Pessoa:
            mostrar_Dados = i.split(';')
            mostrar_Dados()
        arq_Pessoa.close()
        mostrar_Endereco()
    else:
        print("Id não encontrado")