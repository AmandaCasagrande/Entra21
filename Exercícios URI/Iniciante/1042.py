a, b, c = input("").split()
a = int(a)
b = int(b)
c = int(c)

if (a < b < c):
    print(f"{a}\n{b}\n{c}")
elif (a < c < b):
    print(f"{a}\n{c}\n{b}")
elif (b < a < c):
    print(f"{b}\n{a}\n{c}")
elif (b < c < a):
    print(f"{b}\n{c}\n{a}")
elif (c < a < b):
    print(f"{c}\n{a}\n{b}")
elif (c < b < a):
    print(f"{c}\n{b}\n{a}")

print(f"\n{a}\n{b}\n{c}")
