'''
2. Para doar sangue é necessário1
:
• Ter entre 16 e 69 anos.
• Pesar mais de 50 kg.
• Estar descansado (ter dormido pelo menos 6 horas nas últimas 24 horas).
Faça um programa que pergunte a idade, o peso e quanto dormiu nas últimas 24 h para uma pessoa e diga se ela
pode doar sangue ou não
'''

cabecalho = """
Para doar sangue é necessário:

• Ter entre 16 e 69 anos.
• Pesar mais de 50 kg.
• Estar descansado (ter dormido pelo menos 6 horas nas últimas 24 horas)
_________________________________________________________________________
Registro de dados do(a) cliente:
"""
print(cabecalho.format())
idade = int(input("• Qual sua idade? "))

if (16 <= idade <= 69):
    peso, horasSono = input("• Digite seu peso e tempo de sono: ").split()
    peso = int(peso)
    horasSono = int(horasSono)

    if (peso > 50 and horasSono >= 6):
        print(f"Você está permitido(a) a doar sangue!")
    else:
        print(f"Você não está permitido(a) a doar sangue!")
else: 
        print(f"Você tem menos de 16 anos, não é permitido doar sangue!")
