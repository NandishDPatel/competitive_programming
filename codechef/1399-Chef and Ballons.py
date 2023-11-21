t = int(input())
for j in range(t):
    r,g,b = list(map(int,input().split()))
    k = int(input())
    ans = 0
    
    lst = []
    lst.append(r)
    lst.append(g)
    lst.append(b)
    # print(lst)
    
    lst1 = sorted(lst)
    # print(lst1)
    
    if(lst1[0]<k and lst1[1]<k):
        ans = lst1[0]+lst1[1]+k
    elif(lst1[0]<k):
        ans = lst1[0]
        ans += (k-1)*2+1
    else:
        ans = (k-1)*3 + 1
    
    print(ans)