b = float(input())
 # r2 =.12 , r3 =.10, r4 =.07, r5 = 0.04
if (b<=400.00 and b>=0):
    r =.15
    i = b*r
    nb = b + i
    print(f'Novo salario: {float(nb):.2f}')
    print(f"Reajuste ganho: {float(i):.2f}")
    print(f"Em percentual: {int(r*100)} %")
elif (b>=400.01 and b<=800):
    r =.12
    i = b*r
    nb = b + i
    print(f'Novo salario: {float(nb):.2f}')
    print(f"Reajuste ganho: {float(i):.2f}")
    print(f"Em percentual: {int(r*100)} %")
elif (b>=800.01 and b<=1200):
    r =.10
    i = b*r
    nb = b + i
    print(f'Novo salario: {float(nb):.2f}')
    print(f"Reajuste ganho: {float(i):.2f}")
    print(f"Em percentual: {int(r*100)} %")
elif (b>=1200.01 and b<=2000):
    r =.07
    i = b*r
    nb = b + i
    print(f'Novo salario: {float(nb):.2f}')
    print(f"Reajuste ganho: {float(i):.2f}")
    print(f"Em percentual: {int(r*100)} %")
elif (b>2000):
    r =.04
    i = b*r
    nb = b + i
    print(f'Novo salario: {float(nb):.2f}')
    print(f"Reajuste ganho: {float(i):.2f}")
    print(f"Em percentual: {int(r*100)} %")
