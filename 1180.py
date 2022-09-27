from operator import index


t = int(input())
x = [int(x) for x in input().split()]
y = sorted(x)
min = int(y[0])
for i in range(t):
    if(min==x[i]):
        b=x.index(min)

print(f'Menor valor: {min}')
print(f'Posicao: {b}')