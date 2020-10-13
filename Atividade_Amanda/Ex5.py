#--- Exercício 5  - Funções
#--- Escreva um programa para cadastro de pessoas e endereços:
#---       o programa deve solicitar os dados de pessoa utilizados na função do ex1
#---       o programa deve solicitar os dados de endereços utilizados na função do ex2
#---       o programa deve passar o id obtido na função do ex1 para a função do ex2
#---       o programa deve mostrar ao final os dados de todos as pessoas cadastradas 
#          com seus respectivos endereços utilizando as funções do ex3 e ex4

from Ex1 import listaPessoas
from Ex2 import listaEnderecos
from Ex3 import pesquisaPessoa
from Ex4 import pesquisaEndereco
caracter = "_"

#Desenvolvimento de Funções para cabeçalho e rodapé;
def multiCaracter(caracter):
    print(caracter * 30)

def cabecalho(tipo_de_cadastro):
    multiCaracter(caracter)
    print("\n**    CADASTRO DE {}     **".format(tipo_de_cadastro))
    multiCaracter(caracter)

def rodape():
    print("\n**      FIM DO PROGRAMA    **" )
    multiCaracter(caracter)

entrada = input("Deseja fazer um novo cadastro? ")

#Loop de cadastros;
while (entrada == 'S'):

    #Entrada de Dados Pessoais;
    cabecalho("DADOS PESSOAIS")
    nome = input("Nome: ")
    sobrenome = input("Sobrenome: ")
    idade = int(input("Idade: "))
    cadastroPessoa(nome, sobrenome, idade)

    #Entrada de Endereço:
    cabecalho("ENDEREÇO")
    rua = input("Rua: ")
    numero = input("Número: ")
    comp = input("Complemento: ")
    bairro = input("Bairro: ")
    cidade = input("Cidade: ")
    estado = input("Estado: ")
    endereco = cadastroEndereco(rua, numero, comp, bairro, cidade, estado)

if (entrada == 'N'):
    rodape()