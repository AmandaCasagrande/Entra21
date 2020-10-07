#--- Exercício 2  - Variáveis
#--- Crie um menu para um sistema de cadastro de funcionários
#--- O menu deve ser impresso com a função format()
#--- As opções devem ser variáveis do tipo inteiro
#--- As descrições das opções serão:
#---    Cadastrar funcionário
#---    Listar funcionários
#---    Editar funcionário
#---    Deletar funcionário
#---    Sair
#--- Além das opções o menu deve conter um cabeçalho e um rodapé
#--- Entre o cabeçalho e o menu e entre o menu e o rodapé deverá ter espaçamento de 3 linhas
#--- Deve ser utilizado os caracteres especiais de quebra de linha e de tabulação

cabecalho = """
_________________________________________________
***                   MENU                    ***
_________________________________________________
*           CADASTRO DE FUNCIONÁRIOS            *
_________________________________________________

[1] Cadastrar;
[2] Listar;
[3] Editar;
[4] Deletar;
[5] Sair;"""

rodape = """
_________________________________________________
***             FIM DO PROGRAMA               ***
_________________________________________________
"""

print(cabecalho.format())
entrada = int(input("Digite a opção desejada: "))

if (entrada == 1):
    nomeFunc = str(input("Digite o nome do(a) cliente: "))
    print("Nome cadastrado: {0}".format(nomeFunc))
elif (entrada == 2):
    print(f"Lista dos funcionários:")
elif (entrada == 3):
    print(f"** MENU EDITAR **")
elif (entrada == 4):
    print(f"** MENU DELETAR **")
elif (entrada == 5):
    print(f"Você finalizou o programa.")
print("\n\n\n")
print(rodape.format())
