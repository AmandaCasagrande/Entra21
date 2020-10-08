#--- Exercício 1  - Funções - 1
#--- Escreva uma função que imprima um cabeçalho
#--- O cabeçalho deve ser escrito usando a multiplicação de carácter 
#--- resultado esperado: -------------- Cadastro Serasa --------------------------
#--- O cabeçalho deve conter o nome de uma empresa, que será uma variável
#--- Realize a chamada da função na ultima linha do seu programa

#Declarações de Variáveis utilizadas na função;
caracter = "_"
empresa = "SENIOR SISTEMAS"

def multiCaracter(caracter):
    print(caracter * 60)

def cabecalho(nomeEmpresa):
    multiCaracter(caracter)
    print("**                CADASTRO DE {}             **".format(nomeEmpresa))
    multiCaracter(caracter)

#Chamada da função;
cabecalho(empresa)
