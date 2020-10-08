#--- Exercício 2  - Funções
#--- Escreva uma função que leia dois números do console
#--- Armazene cada número em uma variável
#--- Realize a divisão entre os dois números e armazene o resultado em uma terceira variável
#--- Imprima o resultado e uma mensagem usando f-string


#Função de entrada de valores;
def entradaVal(entrada):
    result = float(input("Digite o valor de {}: ".format(entrada)))
    return result

#Função de cálculo;
def dividirNumeros():
    x = entradaVal("x")
    y = entradaVal("y")
    divisao = x / y
    print(f"O resultado da divisão de {x} e {y} é {divisao:.2f}")

#Chamada da função;
print(f"**      Cálculo de divisão      **")
dividirNumeros()
