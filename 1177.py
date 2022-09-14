t = float(input())
a = []
for i in range(100):
    a.append(t)
    t = t/2

for i in range(100):
    print(f'N[{int(i)}] = {float(a[i]):.4f}')