idade = int(input(""))

anos = int(idade / 365)
resto = idade % 365

meses = int(resto / 30)

dias = resto % 30

print(f"{anos} ano(s)")
print(f"{meses} mes(es)")
print(f"{dias} dia(s)")
