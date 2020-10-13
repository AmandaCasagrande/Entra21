#--- Exercício 1  - Funções
#--- Escreva uma função para cadastro de pessoa:
#---       a função deve receber três parâmetros, nome, sobrenome e idade
#---       a função deve salvar os dados da pessoa em uma lista com escopo global
#---       a função deve permitir o cadastro apenas de pessoas com idade igual ou superior a 18 anos
#---       a função deve retornar uma mensagem caso a idade informada seja menor que 18
#---       caso a pessoa tenha sido cadastrada com sucesso deve ser retornado um id 
#--- A função deve ser salva em um arquivo diferente do arquivo principal onde será chamada

#Variavel Global;
listaPessoas = []

#Função para Cadastrar Dados Pessoais;
def cadastroPessoa(idPessoa, nome, sobrenome, idade) -> str:

    #Validação de dados;
    if (idade < 18):
        return "Idade não permitida! Cadastro apenas para +18."
    elif (idade >= 18):
        return "Dados pessoais cadastrados com sucesso!"

    #Adiciona Endereço na lista;
    pessoa = {"ID": idPessoa, "Nome": nome, "Sobrenome": sobrenome, "Idade": idade}
    listaPessoas.append(pessoa)
    return "ID"

    #Adicionar Códigos com função da Luana rsrsrs
    