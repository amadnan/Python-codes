sum = 1
e = 2
for i in range(3,40,2):
    sum = sum + i/e
    e = e*2

print(f'{float(sum):.2f}')