#--- Exercício 3  - Funções
#--- Crie uma função que leia três números float
#--- Armazene cada valor lido em uma variável
#--- Calcule a média entre os três números e armazene em uma quarta variável
#--- Imprima a média e uma mensagem usando f-string

#Entrada de valores;
def entradaVal(entrada):
    result = float(input("Digite o valor de {}: ". format(entrada)))
    return result

#Função de cálculo;
def mediaVal():
    x = entradaVal("x")
    y = entradaVal("y")
    z = entradaVal("z")
    media = float(x + y + z) / 3
    print(f"A média dos valores é {media:.2f}")

#Chamada da Função;
print(f"**      Média de valores        **")
mediaVal()
