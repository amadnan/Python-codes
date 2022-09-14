t = int(input())
for i in range(t):
    a = int(input())
    sum = 0
    for i in range(1,a+1):
        if(a%i==0):
            sum = sum + i
    nsum = sum - a
    if(nsum == a):
        print(f'{int(a)} eh perfeito')
    else:
        print(f'{int(a)} nao eh perfeito')
