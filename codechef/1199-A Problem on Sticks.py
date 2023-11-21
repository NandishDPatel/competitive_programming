# cook your dish here
t = int(input())
for i in range(t):
    n = int(input())
    arrA = list(map(int,input().split()))
    ans=0
    
    ans = list(set(arrA))
    if 0 in ans:
        print(len(ans)-1)
    else:
        print(len(ans))