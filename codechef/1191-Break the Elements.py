t = int(input())
for i in range(t):
    n = int(input())
    arrA = list(map(int,input().split()))
    ans = 0
    odd = 0
    even = 0
    for j in range(n):
        if((arrA[j]%2)!=0):
            odd += 1

    if(odd == n or odd==0):
        print(0)
    else:
        print(n-odd)
    # print(ans)