a = []
b = []
for i in range(20):
    n = int(input())
    a.append(n)
a.reverse()
for i in range(20):
    print(f'N[{i}] = {a[i]}')
