
#"""Execicios 04
#Exercicio retirado do site <https://wiki.python.org.br/EstruturaDeDecisao>

#Faça um Programa que peça os 3 lados de um triângulo. O programa deverá informar se os valores podem ser um triângulo. Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.
#Dicas:

#Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;

#Triângulo Equilátero: três lados iguais;

#Triângulo Isósceles: quaisquer dois lados iguais;

#Triângulo Escaleno: três lados diferentes;
#

lado1 = input("Digite o lado 1 de um triângulo: ")
lado2 = input("Digite o lado 2 de um triângulo: ")
lado3 = input("Digite o lado 3 de um triângulo: ")

if (lado1 + lado2 > lado3) or (lado1 + lado3 > lado2) or (lado2 + lado3 > lado1):
    print("É triângulo!")

    if (lado1 == lado2 != lado3) or (lado1 == lado3 != lado2) or (lado2 == lado3 != lado1):
        print("Triângulo Isósceles!")
    elif (lado1 == lado2 == lado3):
        print("Triângulo Equilátero!")
    elif (lado1 != lado2) or (lado1 != lado3) or (lado2 != lado3):
        print("Triângulo Escaleno!")
        
else:
    print("Ops... não é triangulo!")