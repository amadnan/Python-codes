x = []
for i in range(10):
    a = int(input())
    if(a<=0):
        a = 1
    x.append(a)

for i in range(10):
    print(f'X[{int(i)}] = {int(x[i])}')
