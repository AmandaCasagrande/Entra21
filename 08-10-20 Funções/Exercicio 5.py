#--- Exercício 5 - Funções
#--- Crie uma função para calculo de raiz
#--- A função deve ter uma variável que deternine qual é o indice da raiz(raiz quadrada, raiz cubica...)
#--- Leia um número do console, armazene em uma variável e passe para a função
#--- Realize o calculo da raiz e armazene em uma segunda variável e retorne 
#--- Imprima o resultado e uma mensagem usando f-string, fora da função

import math
def calcularRaiz():
    num = float("Digite o valor: ")
    indice = int(input("Determine o índice da raiz: "))
    raiz = math.pow(num, 1/indice)
    return num, raiz

calcularRaiz()
print(f"A raiz de {num} é {raiz}")
