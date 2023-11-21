# cook your dish here
t = int(input())
for i in range(t):
    n,c = list(map(int,input().split()))
    arr = list(map(int,input().split()))
    rqrC = 0
    for j in range(n):
        rqrC += arr[j]
    if(rqrC>c):
        print('No')
    else:
        print("Yes")