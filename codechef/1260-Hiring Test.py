# >=(x)-fully | (x-1)-fully and >=y-(partially) =>1-pass,0-fail
import sys

t = int(input())
for i in range(t):
    n,m = list(map(int,input().split()))
    x,y = list(map(int,input().split()))
    lst = []
    for j in range(n):
        inp = input()
        inpList = list(inp)
        ans = 0
        fully = 0
        partially = 0
        u = 0
        for k in range(m):
            if(inpList[k]=='F'):
                fully += 1
            if(inpList[k]=='P'):
                partially += 1
        
        if(fully>=x or (fully>=(x-1) and partially>=y)):
            lst.append(1)
        else:
            lst.append(0)
            
    for z in range(len(lst)):
            print(lst[z],end="")   
    print()