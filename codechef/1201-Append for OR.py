t = int(input())
for i in range(t):
    n,y = list(map(int,input().split()))
    z = list(map(int,input().split()))
    ans = 0
    x = 0
    for j in range(n):
        ans |= z[j]
    x = y-ans
    if((x&y)==x):
        print(x)
    else:
        print(-1)