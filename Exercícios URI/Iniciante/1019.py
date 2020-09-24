tempo = int(input(""))

horas = int(tempo / 3600)
resto = tempo % 3600

minutos = int(resto / 60)
resto = resto % 60

segundos = int(resto / 1)

print(f"{horas}:{minutos}:{segundos}")
