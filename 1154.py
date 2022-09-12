i=1
sum = 0
count = 0
while i>-1:
    a = int(input())
    if(a>0):
        sum = sum + a
        count = count + 1
    else:
        break

avg = sum/count
print(f'{float(avg):.2f}')