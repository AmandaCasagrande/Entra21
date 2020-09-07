# 2) Crie uma lista com 10 números qualquer.
# 
# Usando as funções da lista responda:
# 
# Quantos itens tem a lista?
# Qual é o número maior?
# Qual é o número menor?
# Qual é o resultado da soma da lista?

lista = [2, 6, 10, 14, 18, 22, 26, 30, 34, 38] 

itensLista = len(lista)
numeroMaior = max(lista)
numeroMenor = min(lista)
resultSoma = sum(lista)

print("Lista = ", lista)

print("\nQuantidade itens da lista: ", itensLista)
print("O maior número da lista: ", numeroMaior)
print("O menor número da lista: ", numeroMenor)
print("Soma de elementos: ", resultSoma)