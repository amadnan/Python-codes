x = []
x = [int(x) for x in input().split()]  # taking input as integer in list

b = sorted(x)                          # sorting list as mandatory for Binary search
b.reverse()                            # reversing for descending order
print(b)

low, high = 0, len(b)-1                 # declaring low and high for array index
query = int(input())
flag = True
for i in range(low,high):
    mid = (low+high)//2
    print(mid)
    mid_val = b[mid]
    if(mid_val==query):
        print('data found in position: ',mid)
        flag = False
        break
    elif(mid_val<query):
        high = mid - 1
    elif(mid_val>query):
        low = mid+1

if flag:
    print("data not found")