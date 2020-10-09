#--- Exercício 3  - Funções
#--- Crie uma função que leia três números float
#--- Armazene cada valor lido em uma variável
#--- Calcule a média entre os três números e armazene em uma quarta variável
#--- Imprima a média e uma mensagem usando f-string

print(f"**      Média de valores      **")

x, y, z = input("Digite três valores: ").split()
x = float(x)
y = float(y)
z = float(z)

def declararVar(x, y, z):
    media = float(x + y + z) / 3
    print(f"A média dos valores é {media:.2f}")
    return media

declararVar(x, y, z)