t = int(input())
for i in range(t):
    count = 0
    n = int(input())
    for i in range(2,n):
        if(n%i==0):
            count = count + 1
    if(count>0):
        print(f'{int(n)} nao eh primo')
    if(count==0):
        print(f'{int(n)} eh primo')
