t = int(input())
for i in range(t):
    days = int(input())
    d = []
    p = []

    day = 0
    for j in range(days):
        di,pi = list(map(int,input().split()))
        d.append(di)
        p.append(pi)
    
    q = int(input())

    for j in range(q):
        dead,req = list(map(int,input().split()))
        solved = 0
        for k in range(days):
            if(d[k]<=dead):
                solved += p[k]
            else:
                break
        if(solved>=req):
            print("Go Camp")
        else:
            print("Go Sleep")