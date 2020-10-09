#--- Exercício 1  - Funções - 1
#--- Escreva uma função que imprima um cabeçalho
#--- O cabeçalho deve ser escrito usando a multiplicação de carácter 
#--- resultado esperado: -------------- Cadastro Serasa --------------------------
#--- O cabeçalho deve conter o nome de uma empresa, que será uma variável
#--- Realize a chamada da função na ultima linha do seu programa

def cabecalho(nomeEmpresa):
    print(caracter * 60)
    print("**                CADASTRO DE {}             **".format(nomeEmpresa))
    print(caracter * 60)
    
empresa = "SENIOR SISTEMAS"
caracter = "_"
cabecalho(empresa)
