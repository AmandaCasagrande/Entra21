"""arquivo = open('cadastro.txt', 'a')
arquivo.write(f"{dict_person['first']}; {dict_person['last']}; {dict_person['age']}; \n")
arquivo.close()"""

arquivo = open('cadastro.txt', 'r')
for linha in arquivo:
    linha_limpa = linha.strip()
    lista_dados = linha_limpa.split(';')
    print(f"nome: {lista_dados[0]} - sobrenome {lista_dados[1]}, idade: {lista_dados[2]}")
arquivo.close()