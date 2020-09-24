n1, n2, n3, n4 = input("").split()
n1 = float(n1)
n2 = float(n2)
n3 = float(n3)
n4 = float(n4)
media = ((n1 * 2) + (n2 * 3) + (n3 * 4) + (n4 * 1)) / 10
media = float(media)
print(f"Media: {media:.1f}")

if (media >= 7.0):
    print(f"Aluno aprovado.")

elif (media < 5.0):
    print(f"Aluno reprovado.")

elif (media >= 5.0 and media <= 6.9):
    print(f"Aluno em exame.")

    notaExame = float(input(""))
    print(f"Nota do exame: {notaExame:.1f}")
    novaNota = (notaExame + media) / 2

    if (novaNota >= 5.0):
        print(f"Aluno aprovado.")
        print(f"Media final: {novaNota:.1f}")

    elif (novaNota < 5.0):
        print(f"Aluno reprovado.")
        print(f"Media final: {novaNota:.1f}")
    