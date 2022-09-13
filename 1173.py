n = int(input())
x = []
for i in range(10):
    x.append(n)
    n = 2*n

for i in range(10):
    print(f'N[{int(i)}] = {int(x[i])}')
