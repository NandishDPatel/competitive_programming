# cook your dish here
t = int(input())
# for i in range(t):
#     n = int(input())
#     arr = list(map(int,input().split()))
#     temp = set(arr)
#     ans = 0
#     if(n==1):
#         ans = arr[0]
#     else:
#         while(len(temp)!=1):
#             small = min(arr)
#             for j in range(n):
#                 if(arr[j]>small):
#                     arr[j] -= small
#             temp = set(arr)
            
#         ans = arr[0]
        
#     print(ans)
import math
for i in range(t):
    n = int(input())
    arr = list(map(int,input().split()))
    
    gcd = arr[0]
    
    for j in arr:
        gcd = math.gcd(gcd,j)
        if(gcd==1):
            break
    print(gcd)