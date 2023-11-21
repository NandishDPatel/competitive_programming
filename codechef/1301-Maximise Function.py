# cook your dish here
t = int(input())
for i in range(t):
    n = int(input())
    arr = list(map(int,input().split()))
    sum = 0
    
    arr1 = sorted(arr)
    
    if(n%2 != 0):
        mid = n//2
    else:
        mid = (n//2)+1
    
    temp1 = abs(arr1[0]-arr1[mid])
    temp2 = abs(arr1[mid]-arr1[n-1])
    temp3 = abs(arr1[0]-arr1[n-1])
    sum = temp1+temp2+temp3
    
    print(sum)