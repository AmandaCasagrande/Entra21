a, b, c = input("").split()
a = int(a)
b = int(b)
c = int(c)

if (a > b > c):
    print(f"{a}{b}{c}")
elif (a > c > b):
    print("%d\n%d\n%d\n\n", a, c, b)
elif (b > a > c):
    print("%d\n%d\n%d\n\n", b, a, c)
elif (b > c > a):
    print("%d\n%d\n%d\n\n", b, c, a)
elif (c > a > b):
    print("%d\n%d\n%d\n\n", c, a, b)
elif (c > b > a):
    print("%d\n%d\n%d\n\n", c, b, a)

print("%d\n%d\n%d\n\n", a, b, c)
