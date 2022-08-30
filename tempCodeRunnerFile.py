a = int(input())
b = int(input())
sum = 0
for i in range(a,b+1):
    if(i%13!=0):
        sum = sum + i 

print(sum)