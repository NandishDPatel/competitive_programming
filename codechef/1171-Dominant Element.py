from collections import Counter
# cook your dish here
t = int(input())
for i in range(t):
    n = int(input())
    arr = list(map(int,input().split()))
    x = dict(Counter(arr))
    
    if(len(set(arr))==1):
        print("YES")
    elif(len(set(arr))==len(arr)):
        print("NO")
    else:
        values = list(x.values())
        # print(values)
        highest = max(values)
        # print(highest)
        freq = values.count(highest)
        if(freq!=1):
            print("NO")
        else:
            print("YES")
        