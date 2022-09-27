R=12
t = int(input())
b = input()
sum = 0

matrix = []

for i in range(R):          
    a =[]
    for j in range(R):  
        z = float(input())
        a.append(z)
    matrix.append(a)

for i in range(12):
    sum = sum + matrix[t][i]


if(b=='S'):
    print(f'{float(sum):.1f}')
if(b=='M'):
    print(f'{float(sum/12):.1f}')


