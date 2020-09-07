"""
Faça um programa que receba 10 idades e mostre a seguinte mensagem:
Para maiores de 18 anos: Ingreços da Rave liberado!
De 16 a 18 anos: Ingreços de cinema liberado 
De 13 a 16 anos: Ingreços para fliperama liberado
Menores de 13 anos: Psicina de bolinhas liberado
"""
idadesCadastro = [ ]

for i in range(10): 
  idade = int (input(f"Idade {i + 1}: "))
  if (idade > 18):
    print("Uau! Ingressos da Rave liberado!")
  elif (idade > 16 and idade <= 18): 
    print("Legal! Ingressos de cinema liberado!")
  elif (idade > 13 and idade <= 16):
    print("Show! Ingressos para fliperama liberado!")
  else: 
    print("Oba! Piscina de bolinhas liberado!")