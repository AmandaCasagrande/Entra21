#--- Exercício 3  - Funções
#--- Escreva uma função para listar pessoas cadastradas:
#---    a função deve retornar todas as pessoas cadastradas na função do ex1
#--- Escreva uma função para exibi uma pessoa específica:
#        a função deve retornar uma pessoa cadastrada na função do ex1 filtrando por id

from Ex1 import listaPessoas

def listarPessoas():
    for i in range(len(listaPessoas)):
        #Acessar dicionário;
        pessoa = listaPessoas[i]
        print(pessoa.get("Nome"), pessoa.get("Sobrenome"), pessoa.get("Idade"))

def pesquisaPessoa(idPessoa):
    #Chama função de endereço;
    for i in range(len(listaPessoas)):
        pessoa = listaPessoas[i]
        if (idPessoa == pessoa.get("ID")):
            return pessoa
    return 
