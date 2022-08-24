from operator import iconcat


tc = int(input())
ic = 0
oc = 0
for i in range(tc):
    a = int(input())
    if(a>=10 and a<=20):
        ic = ic + 1
    else:
        oc = oc + 1

print("%d in"%ic)
print("%d out"%oc)
