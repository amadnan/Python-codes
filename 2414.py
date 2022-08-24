a = []

for i in range(1):
    j = input().split(" ")
    a.append(j)
    if(j==0):
        break

b = list(map(int,a[0]))
print(max(b))