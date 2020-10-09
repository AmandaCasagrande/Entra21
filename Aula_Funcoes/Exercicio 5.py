#--- Exercício 5 - Funções
#--- Crie uma função para calculo de raiz
#--- A função deve ter uma variável que deternine qual é o indice da raiz(raiz quadrada, raiz cubica...)
#--- Leia um número do console, armazene em uma variável e passe para a função
#--- Realize o calculo da raiz e armazene em uma segunda variável e retorne 
#--- Imprima o resultado e uma mensagem usando f-string, fora da função

#Importa biblioteca e define função;
import math
def calcularRaiz(num, indice):
    raiz = float(math.pow(num, 1/indice))
    return raiz

#Entrada de parâmetros;
print(f"**      Cálculo de raiz        **")
num = float(input("Digite o valor: "))
indice = int(input("Determine o índice da raiz: "))

#chamada da função;
raiz = calcularRaiz(num, indice)
print(f"A raiz é {raiz:.2f}")
