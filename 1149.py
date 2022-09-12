x = [int(x) for x in input().split()]
a = x[0]
for i in range(1,len(x)):
    if(x[i]>0):
        b = x[i]
        break

sum = 0
for i in range(1,b+1):
    sum = sum + a
    a= a+1

print(sum)