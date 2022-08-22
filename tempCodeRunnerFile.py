
    print(f'Novo salario: {float(nb):.2f}')
    print(f"Reajuste ganho: {float(i):.2f}")
    print(f"Em percentual: {int(r*100)} %")
elif (b>=1200.01 and b<=1600):
    r =.07
    i = b*r
    nb = b + i