x = int(input())
i=1
while i>-1:
    y = int(input())
    if(y>x):
        break
    else:
        continue

sum = 0
j=1
while j>0:
    sum = sum + x
    x = x+1
    j = j + 1
    if(sum>y):
        print(j-1)
        break

