R=12
r=12
t = 12

b = input()
diagsum = 0
totalsum = 0
diagcout = 0
totalcout = 0
matrix = []

for i in range(R):          
    a =[]
    for j in range(R):  
        z = float(input())
        a.append(z)
    matrix.append(a)

for i in range(r):
    for j in range(t):
        diagsum = diagsum + matrix[i][j]
        diagcout = diagcout + 1
    t=t-1

for i in range(R):
    for j in range(R):
        totalsum = totalsum + matrix[i][j]
        totalcout = totalcout + 1

realsum = totalsum - diagsum
realcout = totalcout - diagcout

if(b=='S'):
    print(f'{float(realsum):.1f}')
if(b=='M'):
    print(f'{float(realsum/realcout):.1f}')
