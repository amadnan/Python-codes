t = int(input())
for i in range(t):
    A,B,C,D = input().split()
    a = int(A)
    b = int(B)
    c = float(C)
    d = float(D)
    j = 1
    while True:
        pa = int(a*c/100) + a
        pb = int(b*d/100) + b
        if(pa>pb):
            if(j<=100):
                print(f'{j} anos.')
            break
        else:
            j = j + 1
            if(j>100):
                print(f'Mais de 1 seculo.')
                break
            a = pa
            b = pb
