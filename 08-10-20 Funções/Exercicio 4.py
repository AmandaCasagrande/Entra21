#--- Exercício 4  - Funções
#--- Crie uma função que imprima um cabeçalho de acordo com uma variável de nome da empresa (passada por parametro)
#--- A impressão deve ocorrer via multiplicação de strings
#--- A multiplicação deve ser feita com base em uma variável que contenha o caracter a ser multiplicado
#--- Crie uma segunda função que imprima um rodapé utilizando a mesma técnica
#--- Crie uma chamada para as duas função, para exibir o resultado no console


#Declarações de Variáveis
empresa = "HBSIS"
caracter = "_"

#Desenvolvimento de Funções
def multiCaracter(caracter):
    print(caracter * 30)

def cabecalho(nomeEmpresa):
    multiCaracter(caracter)
    print("\n**    CADASTRO DE {}     **".format(nomeEmpresa))
    multiCaracter(caracter)
    
def rodape():
    print("\n**      FIM DO PROGRAMA    **" )
    multiCaracter(caracter)

#Chamada de funções;
cabecalho(empresa)
rodape()
