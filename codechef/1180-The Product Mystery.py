import math
# cook your dish here
t = int(input())
for i in range(t):
    b,c = list(map(int,input().split()))
    print(int(c/math.gcd(b,c)))
    
    # a = 1
    # if(c%b == 0):
    #     print(c//b)
    # else:
    #     for j in range(2,c+1):
    #         if((b*j)%c == 0):
    #             a = j
    #             break
    #     print(int(a))
        