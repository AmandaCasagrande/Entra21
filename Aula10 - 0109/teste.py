idCliente = [1,2,3]
idPesquisa = int(input("Digite o ID a ser pesquisado: "))

foiLocalizado = False
for i in range(len(idCliente)):
    if (idPesquisa == idCliente[i]):
        index =  i
        foiLocalizado = True

if (foiLocalizado) :
    print(idCliente[index])    
else:
    print("Codigo não localizado")
        
