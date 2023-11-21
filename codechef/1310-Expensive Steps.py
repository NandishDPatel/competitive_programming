# cook your dish here
t=int(input())
for i in range(t):
    n,x1,y1,x2,y2=list(map(int,input().split()))
    step = abs(x1-x2) + abs(y1-y2)
    if(step<(min(x1,y1,n+1-x1,n+1-y1)+min(x2,y2,n+1-x2,n+1-y2))):
        print(step)
    else:
        print(min(x1,y1,n+1-x1,n+1-y1)+min(x2,y2,n+1-x2,n+1-y2))