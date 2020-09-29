"""
'1' = 2
'2' = 5
'3' = 5
'4' = 4
'5' = 5
'6' = 6
'7' = 3
'8' = 7
'9' = 6
'0' = 6"""

entrada = int(input(""))
totalLeds = 0 #Inicia a variável

for i in range (entrada):
    numero = str(input(""))
    lista = list(numero)

    for i in range (len(lista)):
        if (lista[i] == '1'):
            totalLeds = totalLeds + 2

        elif (lista[i] == '2'):
            totalLeds = totalLeds + 5

        elif (lista[i] == '3'):
            totalLeds = totalLeds + 5

        elif (lista[i] == '4'):
            totalLeds = totalLeds + 4

        elif (lista[i] == '5'):
            totalLeds = totalLeds + 5

        elif (lista[i] == '6'):
            totalLeds = totalLeds + 6

        elif (lista[i] == '7'):
            totalLeds = totalLeds + 3

        elif (lista[i] == '8'):
            totalLeds = totalLeds + 7

        elif (lista[i] == '9'):
            totalLeds = totalLeds + 6

        elif (lista[i] == '0'):
            totalLeds = totalLeds + 6

    print(f"{totalLeds} leds")
    totalLeds = 0