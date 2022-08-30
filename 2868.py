from posixpath import split


t = int(input())
a = str()
for i in range(t):
    a = input().split()
    x = int(a[0])
    y = int(a[2])
    z = int(a[4])
    if(a[1]=='+'):
        r = x + y
    elif(a[1]=='-'):
        r = x - y
    elif(a[1]=='x'):
        r = x * y
    d = abs(r - z)
    print("E%sou!"%(d*'r'))
    