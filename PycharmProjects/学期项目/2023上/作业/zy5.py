for a in range(100, 100000):
    x = a // 100
    y = a // 10 % 10
    z = a % 10
    if x ** 3 + y ** 3 + z ** 3 == a:
        print(f"{x}{y}{z}")
