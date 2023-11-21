import math
# cook your dish here
t = int(input())
for i in range(t):
    N,A = list(map(int,input().split()))
    print((math.floor(math.sqrt(N)))*A)
    # power = 0
    # square = 0
    # for i in range(1,N):
    #     power = i*i
    #     if(power<=N):
    #         square = i
    #     else:
    #         break
    # print(square*A)