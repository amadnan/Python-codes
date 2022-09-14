c = []
c.append(0)
c.append(1)
a1 = 0
a2 = 1
b = 61
sum = 0
for i in range(b+1):
    an = a1 + a2
    c.append(an)
    a1 = a2
    a2 = an


t = int(input())
for i in range(t):
    n = int(input())
    print(f'Fib({int(n)}) = {(c[n])}')