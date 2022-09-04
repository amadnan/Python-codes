a=1
b=2
c=3
I=0
for i in range(11):
    for j in range(1):
        print(f'I={I} J={a}')
        print(f'I={I} J={b}')
        print(f'I={I} J={c}')
        I=round(I+.2,1)
        a=round(a+.2,1)
        b=round(b+.2,1)
        c=round(c+.2,1)
        if(I==1.0 or I==2.0):
            I = int(I)
            a = int(a)
            b = int(b)
            c = int(c)