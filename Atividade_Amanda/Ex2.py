#--- Exercício 2  - Funções
#--- Escreva uma função para cadastro de endereço:
#---       a função deve receber sete parâmetros, id da pessoa, rua, numero, complemento, bairro, cidade e estado
#---       a função deve salvar os dados de endereço em uma lista com escopo global
#---       a função deve permitir o cadastro apenas de endereços com todos os dados preenchidos
#---       a função deve retornar uma mensagem ao final de acordo com a situação
#--- A função deve ser salva em um arquivo diferente do arquivo principal onde será chamada

#Variavel Global;
listaEnderecos = []

#Função para Cadastrar Endereço;
def cadastroEndereco(idPessoa, rua, numero, comp, bairro, cidade, estado) -> str:

    #Validação de dados (não pode ser nulo);
    if (not idPessoa):
        return "Campo 'ID' vazio! Não é possível cadastrar."
    if (not rua):
        return "Campo 'Rua' vazio! Não é possível cadastrar."
    if (not numero):
        return "Campo 'Número' vazio! Não é possível cadastrar."
    if (not comp):
        return "Campo 'Complemento' vazio! Não é possível cadastrar."
    if (not bairro):
        return "Campo 'Bairro' vazio! Não é possível cadastrar."
    if (not cidade):
        return "Campo 'Cidade' vazio! Não é possível cadastrar."
    if (not estado):
        return "Campo 'Estado' vazio! Não é possível cadastrar."

    #Adiciona Endereço na lista;
    endereco = {"ID": idPessoa, "Rua": rua, "Número": numero, "Complemento": comp, "Bairro": bairro, "Cidade": cidade, "Estado": estado}
    listaEnderecos.append(endereco)
    return "Endereço cadastrado com sucesso!"
