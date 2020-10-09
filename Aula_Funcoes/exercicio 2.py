#--- Exercício 2  - Funções
#--- Escreva uma função que leia dois números do console
#--- Armazene cada número em uma variável
#--- Realize a divisão entre os dois números e armazene o resultado em uma terceira variável
#--- Imprima o resultado e uma mensagem usando f-string

print(f"**      Divisão de números      **")
x, y = input("Digite os valores de 'x' e 'y': ").split()
x = float(x)
y = float(y)

def dividirNumeros(x, y):
    divisao = float(x) / float(y)
    print(f"O resultado da divisão de {x} e {y} é {divisao:.2f}")

dividirNumeros(x, y)
