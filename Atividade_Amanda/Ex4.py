#--- Exercício 4  - Funções
#--- Escreva uma função para listar endereços cadastrados:
#--- a função deve retornar todos os endereços cadastrados na função do ex2
#--- Escreva uma função para exibir um endereço específico:
# a função deve retornar um endereço cadastrado na função do ex2 filtrando por 
#id da pessoa

from Ex2 import listaEnderecos

def listarEnderecos():
    for i in range(len(listaEnderecos)):
        #Acessar dicionário;
        endereco = listaEnderecos[i]
        print(endereco.get("Rua"), endereco.get("Número"), endereco.get("Complemento"), 
            endereco.get("Bairro"), endereco.get("Cidade"), endereco.get("Estado"))

def pesquisaEndereco(idPessoa):
    #Chama função de endereço;
    for i in range(len(listaEnderecos)):
        endereco = listaEnderecos[i]
        if (idPessoa == endereco.get("ID")):
            return endereco
    return 

