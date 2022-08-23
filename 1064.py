count = 0
sum = 0
for i in range(1,7):
    a = float(input())
    if(a>0):
        count = count + 1
        sum = sum + a
print("%d valores positivos"%count)
print(f'{float(sum/count):.1f}')