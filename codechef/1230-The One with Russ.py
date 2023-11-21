# condition |aj-bj|<=K
t = int(input())
for i in range(t):
    n,x,k = list(map(int,input().split()))
    arrA = list(map(int,input().split())) #Ross
    arrB = list(map(int,input().split())) #Russ
    
    count = 0
    check = 0
    
    for j in range(n):
        check = abs(arrA[j] - arrB[j])
        if(check<=k):
            count += 1
    if(count>=x):
        print("YES")
    else:
        print("NO")
    
    