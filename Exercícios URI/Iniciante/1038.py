codigo, qntd = input("").split()
codigo = int(codigo)
qntd = int(qntd)

if (codigo == 1):
    cachorro = qntd * 4
    print(f"Total: R$ {cachorro:.2f}")
elif (codigo == 2):
    x_salada = qntd * 4.5
    print(f"Total: R$ {x_salada:.2f}")
elif (codigo == 3):
    x_bacon = qntd * 5
    print(f"Total: R$ {x_bacon:.2f}")
elif (codigo == 4):
    torrada = qntd * 2
    print(f"Total: R$ {torrada:.2f}")
elif (codigo == 5):
    refri = qntd * 1.5
    print(f"Total: R$ {refri:.2f}")
