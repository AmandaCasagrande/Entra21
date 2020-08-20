
# Exercicio 11
# Faça um programa que peça o sexo do cliente. 
# 
# Se o cliente digitar 'F' deve aparecer a mensagem "Como você está bonita hoje!"
# 
# Se o cliente digitar 'M' deve aparecer a mensagem "Como você está forte? andou malhando?"
# 
# Se o cliente digitar qualquer outra coisa, deve aparecer a mensagem: "opção invalida!"
# 
entrada = str(input("Digite seu gênero: "))

if (entrada == 'F'):
    print("Como você está bonita hoje!")
if (entrada == 'M'):
    print("Como você está forte? andou malhando?")
if (entrada != 'F') and (entrada != 'M'):
    print("Opção Inválida!")
