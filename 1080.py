a = []
for i in range(5):
    j = int(input())
    a.append(j)
b = max(a)
print(b)
for i in range(len(a)):
    if(b==a[i]):
        print(i+1)
