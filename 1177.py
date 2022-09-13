t = int(input())
n = 0
a = []
for i in range(1000):
    a.append(n)
    n = n+1
    if(n==t):
        n = 0

for i in range(1000):
    print(f'N[{int(i)}] = {int(a[i])}')